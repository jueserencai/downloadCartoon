# -*- coding: UTF-8 -*-

from tkinter import *  

class MainWindow:  
    def __init__(self):  
        self.frame = Tk()  

        # 控件
        self.label_firstPageUrl = Label(self.frame,text = "firstPageUrl:")  
        self.text_firstPageUrl = Text(self.frame,height = "1",width = 30)  
        self.label_firstPageUrl.grid(row = 0,column = 0)  
        self.text_firstPageUrl.grid(row = 0,column = 1)  


        self.label_url = Label(self.frame,text = "url:")  
        self.text_url_pre = Text(self.frame,height = "1",width = 30)  
        self.text_url_post = Text(self.frame,height = "1",width = 10)  
        self.label_url.grid(row = 1,column = 0)  
        self.text_url_pre.grid(row = 1,column = 1)  
        self.text_url_post.grid(row = 1,column = 2)  


        self.label_savePath = Label(self.frame,text = "savePath:")  
        self.text_savePath = Text(self.frame,height = "1",width = 30)  
        self.label_savePath.grid(row = 2,column = 0)  
        self.text_savePath.grid(row = 2,column = 1)  

        self.label_picType = Label(self.frame,text = "picType:")  
        self.text_picType = Text(self.frame,height = "1",width = 30)  
        self.label_picType.grid(row = 3,column = 0)  
        self.text_picType.grid(row = 3,column = 1)  

        self.label_pageCount = Label(self.frame,text = "pageCount:")  
        self.text_pageCount = Text(self.frame,height = "1",width = 30)  
        self.label_pageCount.grid(row = 4,column = 0)  
        self.text_pageCount.grid(row = 4,column = 1)  

        self.label_title = Label(self.frame,text = "title:")  
        self.text_title = Text(self.frame,height = "1",width = 30)  
        self.label_title.grid(row = 5,column = 0)  
        self.text_title.grid(row = 5,column = 1)  

        self.label_imgTag = Label(self.frame, height = '7', text = 'imgTag')
        self.label_imgTag_parent = Label(self.frame, height = '3', text = 'parent')
        self.label_imgTag_parent_tag = Label(self.frame, height = '1', text = 'tag')
        self.label_imgTag_parent_attrName = Label(self.frame, height = '1', text = 'attrName')
        self.label_imgTag_parent_attrContent = Label(self.frame, height = '1', text = 'attrContent')
        self.text_imgTag_parent_tag = Text(self.frame, height = '1', width = 15)
        self.text_imgTag_parent_attrName = Text(self.frame, height = '1', width = 15)
        self.text_imgTag_parent_attrContent = Text(self.frame, height = '1', width = 15)
        self.label_imgTag.grid(row = 6, rowspan = 5, column = 0)
        self.label_imgTag_parent.grid(row = 6, rowspan = 3, column = 1)
        self.label_imgTag_parent_tag.grid(row = 6, column = 2)
        self.label_imgTag_parent_attrName.grid(row = 7, column = 2)
        self.label_imgTag_parent_attrContent.grid(row = 8, column = 2)
        self.text_imgTag_parent_tag.grid(row = 6, column = 3)
        self.text_imgTag_parent_attrName.grid(row = 7, column = 3)
        self.text_imgTag_parent_attrContent.grid(row = 8, column = 3)


        self.label_imgTag_self = Label(self.frame, height = '2', text = 'self')
        self.label_imgTag_self_tag = Label(self.frame, height = '1', text = 'tag')
        self.label_imgTag_self_order = Label(self.frame, height = '1', text = 'order')
        self.text_imgTag_self_tag = Text(self.frame, height = '1', width = 15)
        self.text_imgTag_self_order = Text(self.frame, height = '1', width = 15)

        self.label_imgTag_self.grid(row = 9, rowspan = 2, column = 1)
        self.label_imgTag_self_tag.grid(row = 9, column = 2)
        self.label_imgTag_self_order.grid(row = 10, column = 2)
        self.text_imgTag_self_tag.grid(row = 9, column = 3)
        self.text_imgTag_self_order.grid(row = 10, column = 3)


        self.button_download = Button(self.frame,text = "download",width = 10, command = self.getInfo)  
        self.button_download.grid(row = 11, column = 0)

        self.frame.mainloop()  

    def getInfo(self):
    	url = self.text_firstPageUrl.get("0.0", "end")
    	print(url)
  
frame = MainWindow()  