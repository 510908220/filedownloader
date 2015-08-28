# -*- encoding:utf-8 -*-
import logging
import threading
from multiprocessing import cpu_count
from collections import namedtuple
from queue import Queue, Empty
import time
import urllib.request
import socket

logger = logging.getLogger(__name__)
Param = namedtuple("Param", ["url", "output"])
Result = namedtuple("Result", ["success", "result", "url"])

timeout = 10
socket.setdefaulttimeout(timeout)


def download(url, output=None):
	output = url.split('/')[-1] if output == None else output
	try:
		rv = urllib.request.urlretrieve(url, output)
	except Exception as e:
		return Result(False, str(e), url)
	return Result(True, rv, url)


class Worker(threading.Thread):
	def __init__(self, job, result, exit):
		threading.Thread.__init__(self)
		self.setDaemon(True)
		self.job = job
		self.result = result
		self.exit = exit

	def run(self):
		while 1:
			try:
				param = self.job.get_nowait()
				result = download(param.url, param.output)
				self.result.put(result)
				time.sleep(1)
			except Empty:
				logger.info("no task........")
				if not self.exit.empty():
					logger.info("thread  will exit.".format(id=self.ident))
					break
			time.sleep(1)


def downloads(urls, outputs=[], concurrency=cpu_count()):
	# 用于线程同步的队列
	exit_queue = Queue(1)
	job_queue = Queue()
	result_queue = Queue()

	# 创建下载任务，并加入到任务队列
	outputs = [None for _ in urls] if not outputs else outputs
	for url, output in zip(urls, outputs):
		job_queue.put(Param(url, output))

	job_size = job_queue.qsize()
	works = []

	# 创建工作线程并启动
	for _ in range(concurrency):
		t = Worker(job_queue, result_queue, exit_queue)
		works.append(t)
		t.start()

	# 检测任务是否完成，主要有两种情况
	# 1.所有任务都执行了
	# 2.用户主动按ctrl+c结束任务,这里会等待已经运行的任务继续运行
	alive = True
	try:
		while alive:
			for work in works:
				if work.isAlive():
					alive = True
					break
			else:
				alive = False
			if result_queue.qsize() == job_size and exit_queue.qsize() == 0:
				exit_queue.put(1)
	except KeyboardInterrupt:
		logger.warning("ctrl + c is precessed!wait running task to complate..")
		exit_queue.put(1)
		for work in works:
			if work.isAlive():
				work.join()

	# 结果收集并返回
	results = []
	while job_queue.qsize() > 0:
		param = job_queue.get_nowait()
		results.append(Result(False, "task not excute", param.url))
	while result_queue.qsize() > 0:
		result = result_queue.get_nowait()
		results.append(result)
	return results
