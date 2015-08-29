# filedownloader
![文件下载器](http://7xk7ho.com1.z0.glb.clouddn.com/download.jpg)

##下载协议
###http
开始准备使用python3的concurrent.futures模块，比如实现多线程下载可以有如下的方式:
```
import concurrent.futures
import urllib.request

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']

# Retrieve a single page and report the url and contents
def load_url(url, timeout):
    conn = urllib.request.urlopen(url, timeout=timeout)
    return conn.readall()

# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))

```
- 问题1:这种方式有个问题是如果想取消任务呢？因为一旦执行，主线程是会进行等待的，即使按ctrl+c也无法停止(主线程无法响应中断).
因为是利用线程池，所以在主线程想取消任务是直接取消不了的，所以还是利用threading模块重新写一个.

- 问题2:无论是使用requests模块还是urllib进行文件下载，都会遇到卡死的情况. 尤其是在多线程里如果卡死的话很不好处理，解决办法是:
```
timeout = 10
socket.setdefaulttimeout(timeout)
```

