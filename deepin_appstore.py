# -*- coding:utf-8 -*-
#import urllib2
import re
import os
import sys
from selenium import webdriver



###网页用js写的，需要用js引擎来获取网页内容
URL_ROOT = "http://appstore.deepin.org"  
path = "C:/Users/iscas/Desktop/deepin"


###test program
def get_html(url):
    response = webdriver.PhantomJS(executable_path="C:/Python27/Scripts/phantomjs.exe")
#   response.page_source 功能类似于下面一行
    response.get(url) 
    try:
      #  category = response.find_element_by_id('Aside').find_element_by_xpath('section/ul/li[3]').get_attribute("href")
      #  category = response.find_element_by_id('WebView').get_attribute("href")#可以找到所有名称
      #  print category
      
      #  print type(category)
       ## category = str(category)
        #category = category.split("\n")
       # print category
       ## length = len(category)
        #print length  /div/ng-view/div/div/ul/ng-transclude/li[1]/div[2]/div/a/span
        #category_ = response.find_element_by_xpath('html/body/div[2]') #可以找到第一个元素
        category_ = response.find_element_by_class_name('app-list-list').find_element_by_xpath('ng-transclude/li[]')
      #  pattern = '\"zh_CN\":{\"name\":'
      ##  index = category_.find(pattern)
      #  category_ = category_[index+len(pattern):]
      ##  index = category_.find("}")
        #category_ = category_[:index]
        
    except Exception as e:
        print(e)
    print category_


def get_html_(url): 
    response = webdriver.PhantomJS(executable_path="C:/Python27/Scripts/phantomjs.exe")   
    return response

###第一页元素获取
def get_category_html():
    url = URL_ROOT
    response = get_html_(url)
    response.get(url)
    ###find category name_num
    category = response.find_element_by_id('Aside').text
   # print category
    category_list = category.split("\n")
    length = len(category_list)
    name_url_list = []
    ###循环读取href属性
    for i in xrange(1,length):  ###第一个深度商店中没有href属性
        href = response.find_element_by_xpath('html/body/aside/section/ul/li'+str([i])).get_attribute("href")
        #print href
        href = url + href
        name_url_list.append((category_list[i],href))
  #  print name_url_list
    return name_url_list  

def get_application_list():
    res = get_category_html()
    for i in xrange(1,len(res)):
   # for i in xrange(0,1):
        j = 1
        print i
        category_name = res[i][0]
        category_name = category_name.encode("utf-8")
        category_html = res[i][1]
        print category_name,category_html
        response = get_html_(category_html)
        response.get(category_html)
        f = open(os.path.join(path, "test.txt"), 'a')
        ###获取二级页面的所有app名称，地址待解析
        while j >0:
            try:
                app = response.find_element_by_class_name('app-list-list').find_element_by_xpath('ng-transclude/li'+str([j])).get_attribute("data-app")
                if app:
                    j += 1
                    #获取app名字
                    pattern = '\"zh_CN\":{\"name\":'
                    index = app.find(pattern)
                    name = app[index+len(pattern):]
                    index = name.find("}")
                    name = name[:index]
                    name = name.encode("utf-8")
                    #获取app的标语
                    pattern_ = '\"zh_CN\":{\"slogan\":'
                    index = app.find(pattern_)
                    slogan = app[index+len(pattern_):]
                    index = slogan.find("}")
                    slogan = slogan[:index]   
                    slogan = slogan.encode("utf-8")
                    slogan = slogan.strip("\n")
                    #写入txt
                    print category_name,name,slogan
                    f.write(category_name+"\t"+name+"\t"+slogan+"\n")
                    continue
            except Exception as e:
                print(e)
            f.close()
            break
            

if __name__ == "__main__":
   # get_html("http://appstore.deepin.org/" )
   # get_category_html()
    get_application_list()