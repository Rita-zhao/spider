# -*- coding:utf-8 -*-
import urllib2
import re
import os
import sys
#from selenium import webdriver

#网页用html写时的做法
URL_ROOT = "http://appstore.deepin.org"  
path = "C:/Users/iscas/Desktop/deepin"


def get_html(url):
    response = urllib2.urlopen(url)
    return response.read()    

def get_category_html():
    url = URL_ROOT
    html = get_html(url)
    print html

    #find category name
    pattern = r"text=\"(.+)\""
    category_list = re.findall(pattern, html)
    print category_list
    #find category html
    pattern = r"ng-href=\"(.+)\""
    category_html_list = re.findall(pattern, html)


    assert len(category_list) == len(category_html_list)  
    
    #create array to store name and html
    res = []
    for i in range(len(category_list)):
        res.append((category_list[i], category_html_list[i]))
    return res    

def get_application_list():
    res = get_category_html()
    print res
    for i in xrange(len(res)):
        category_name = res[i][0]
        category_html = res[i][1]
        category_html = URL_ROOT + category_html
        html = get_html(category_html)
        
        pattern = r"<span ng-bind=\":: getLanguageProperty(item.pkg, \'name\')\">\"(.+)\"</span>"
        app_list = re.findall(pattern, html)
    
        f = open(os.path.join(path, "test.txt"), 'w+')
        for x in name1_name2_version_list:
            f.write(category_name+"\t"+app_list+"\n")   
        f.close()

if __name__ == "__main__":
    get_html("http://appstore.deepin.org" )
 #   get_category_html()
  #  get_application_list()