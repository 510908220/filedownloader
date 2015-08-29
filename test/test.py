__author__ = 'Administrator'

from pathlib import Path
import sys
import os

cur_dir = os.path.abspath(os.path.dirname(__file__))

sys.path.append(os.path.abspath(os.path.join(cur_dir, "..")))

urls = [
	"http://dlsw.baidu.com/sw-search-sp/soft/6e/10644/QQGame_setup_xzq_20000.1437033234.EXE",
	"http://dlsw.baidu.com/sw-search-sp/soft/b9/14497/UCBrowser_V5.2.3937.21_setup.1439966963.exe",
	"http://dlsw.baidu.com/sw-search-sp/soft/55/11339/bdbrowserSetup-7.6.100.2089-1212_11000003.1437029629.exe",
	"http://dlsw.baidu.com/sw-search-sp/soft/0d/14754/sogou_explorer_V6.0.5.17838_setup.1440558302.exe",
	"http://dlsw.baidu.com/sw-search-sp/soft/a6/15895/KSbrowser_V5.3.100.10349_setup.1438916510.exe"
]

from  filedownloader import http_downloads,http_download

results = http_downloads(urls,[],2)

for result in results:
	print(result)
