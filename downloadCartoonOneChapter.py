# -*- coding: utf-8 -*-
# @Date    : 2017-9-18 22:01:06
# @Author  : 王星南 (wxn1905@163.com)
# @Link    : ${link}
# @Version : $Id$

# discribe :
	# 下载一个漫画的一个章节

import os
import re
import math
import threading

from urllib import request
from bs4 import BeautifulSoup



class downloadCartoonOneChapter(object):
	def __init__(self, argv):
		self.__argv = argv
		self.__errorPage = []	# 下载错误的页码 如[3, 5, 6]
		self.__mutex = threading.Lock()	# 多线程向errorPage中添加错误页码的互斥量

	# 下载当前页的这一张图片
	def __downloadOnePicture(self, savePath, cartoonLink):
		opener = request.build_opener()
		opener.addheaders = self.__argv['headers']
		response = opener.open(cartoonLink)
		html = response.read() 
		response.close()  
		contents = html.decode(self.__argv['encode'], "ignore")  
		soup = BeautifulSoup(contents, "html.parser") 

		parentAttrName    = self.__argv['imgTag']['parent']['attrName']
		parentTag         = self.__argv['imgTag']['parent']['tag']
		parentAttrContent = self.__argv['imgTag']['parent']['attrContent']
		selfTag           = self.__argv['imgTag']['self']['tag']
		selfOrder         = self.__argv['imgTag']['self']['order']

		if parentAttrName == 'class':
			imgSoup = soup.find(parentTag, class_=parentAttrContent).find_all(selfTag)
		elif parentAttrName == 'id':
			imgSoup = soup.find(parentTag, id=parentAttrContent).find_all(selfTag)
		elif parentAttrName == 'style':
			imgSoup = soup.find(parentTag, style=parentAttrContent).find_all(selfTag)
		else:
			print('error tag name: class, id, style only')
			exit(0)
		if imgSoup:
			pictureLink = imgSoup[selfOrder].get('src')
			request.urlretrieve(pictureLink, savePath)
		else:
			print('not found imgSoup')

	# 下载一部分页码的页面图片
	def __downloadFewPage(self, *pageList):
		for page in pageList:
			try:
				self.__downloadOnePicture(os.path.join(self.__argv['savePath'], self.__argv['chapter'] + str(page) + '.' + self.__argv['picType']), self.__argv['url']['pre'] + str(page) + self.__argv['url']['post'])
			except Exception as result:
				print('appearing error: downloading chapter {} page {} '.format(self.__argv['chapter'], page))
				if self.__mutex.acquire():
					self.__errorPage.append(page)
					self.__mutex.release()

	# 重新下载错误的页码
	def __downloadErrorPage(self):
		for index, page in enumerate(self.__errorPage):
			try:
				self.__downloadOnePicture(os.path.join(self.__argv['savePath'], self.__argv['chapter'] + str(page) + '.' + self.__argv['picType']), self.__argv['url']['pre'] + str(page) + self.__argv['url']['post'])
			except Exception as result:
				print('repeatly error: downloading chapter {} page {} '.format(self.__argv['chapter'], page))
			else:
				self.__errorPage[index] = 0	# 重新下载好的错误页码标记为已完成：0
				print('error page {} downloaded'.format(page))


	# 开始下载
	def run(self):

		# 当前漫画的文件保存目录
		if not os.path.exists(self.__argv['savePath']):
			os.makedirs(self.__argv['savePath'])

		#### 多线程下载图片

		# 设置 线程数、每个线程负责的页码数
		threadCount = math.ceil(len(self.__argv['page']) / self.__argv['everyThreadPage'])
		# 开始为线程分配下载页码范围
		pageIndex = 0
		threads = []

		if threadCount > 1:
			for i in range(0, threadCount-1):
				threads.append(threading.Thread(target=self.__downloadFewPage, args=(self.__argv['page'][pageIndex : pageIndex+self.__argv['everyThreadPage']])))
				pageIndex += self.__argv['everyThreadPage']
		threads.append(threading.Thread(target=self.__downloadFewPage, args=(self.__argv['page'][pageIndex : ])))

		# 线程开始下载
		for i in range(0, threadCount):
			threads[i].start()
		for i in range(0, threadCount):
			threads[i].join()

		#### 多线程下载图片完毕

		# 重新下载错误的页码
		self.__downloadErrorPage()
		if self.__errorPage.count(0) < len(self.__errorPage):
			print('chapter {} still existed error Page:-----------------'.format(self.__argv['chapter']))
			for page in self.__errorPage:
				if page > 0:
					print(page, ' ', end='')
			print()
		else:
			print('All picture downloaded')


if __name__ == "__main__":
	config = {
		'encode': 'utf-8',	# 编码
		'headers': [('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')],
		'url': {'pre': 'http://m.uuumh.com/manhua/2018/0105/5217_', 'page': 2, 'post': '.html'}, # 漫画url格式
		'savePath': 'E:/document/picture/cartoon/test', 
		'chapter': '1_',
		'page': [1,2,3,4,5], # 需要下载的页数
		'everyThreadPage': 5,
		'picType': 'jpg', # 图片格式
		'imgTag': {
			'parent': {
				'tag': 'div', # 图片img标签的父级标签
				'attrName': 'id', # 父级标签属性是class还是id...
				'attrContent': 'imgString', # 父级标签的属性内容
			},
			'self': {
				'tag': 'img',
				'order': 0,
			},
		},
	}
	obj = downloadCartoonOneChapter(config)
	obj.run()