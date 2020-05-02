# coding:utf-8

import urllib
from urllib import request
from urllib.parse import quote
import requests
import string

class HtmlDownLoader(object):

    def download(self,url):

        if url is None:
            return None

        #urlopen()函数的返回值是一个类文件对象，这个类文件对象有下列函数：
        #read()：读取整个文件，返回一个str
        #readline()：读取文件的一行，返回一个str
        #readlines()：每次按行读取整个文件，将读取的内容放到一个列表中，返回list
        #fileno()：
        #close()：关闭文件流
        #info()：返回服务器返回的头信息
        #getcode()：返回状态码
        #geturl()：返回请求的url地址

        # r = quote(url, safe=string.printable)   #用这个函数处理含有中文的url
        # # r = urllib.request.urlopen(r)
        #
        # # http的状态码，200表示服务器成功返回请求
        # if r.getcode() != 200:
        #     return None
        # return r.read()

        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
        }

        reponse = requests.get(url, headers=header)
        reponse.encoding = 'utf-8'
        return reponse.text
