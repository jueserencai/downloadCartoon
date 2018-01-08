# -*- coding: utf-8 -*-
# @Date    : 2018-1-8 22:01:06
# @Author  : 王星南 (wxn1905@163.com)
# @Link    : ${link}
# @Version : $Id$

# discribe :
	# 下载一个漫画

import downloadCartoonOneChapter

class downloadCartoon(object):
	def __init__(self, argv):
		self.__argv = argv
		self.__chapter = {
			'1':{
				'urlPre': 'http://m.962760.com/wanghong/2017/0822/2188_', 
				'page': [2, 3, 5, 8, 10],
				}, 
			}
		self.__urlPost = '.html'

	def __confirmTitle(self):
		pass
	def __confirmSavePath(self):
		pass
	def __confirmChapter(self):
		pass


	def run(self):
		self.__confirmTitle()
		self.__confirmSavePath()

		self.__confirmChapter()

		argv = self.__argv
		argv['url'] = {}
		for chapter, chapterContent in self.__chapter.items():
			argv['chapter'] = chapter + '_'
			argv['page'] = chapterContent['page']
			argv['url']['pre'] = chapterContent['urlPre']
			argv['url']['post'] = self.__urlPost

			downloadOneChapterObj = downloadCartoonOneChapter.downloadCartoonOneChapter(argv)
			downloadOneChapterObj.run()


if __name__ == "__main__":
	config = {
		'encode': 'utf-8',	# 编码
		'headers': [('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')],
		'homePage': 'http', # 漫画url格式
		'savePath': 'E:/document/picture/cartoon/manhua', 
		'title': 'manhua', 
		'everyThreadPage': 5,
		'picType': 'jpg', # 图片格式
		'imgTag': {
			'parent': {
				'tag': 'div', # 图片img标签的父级标签
				'attrName': 'class', # 父级标签属性是class还是id...
				'attrContent': 'pic', # 父级标签的属性内容
			},
			'self': {
				'tag': 'img',
				'order': 0,
			},
		},
	}
	obj = downloadCartoon(config)
	obj.run()