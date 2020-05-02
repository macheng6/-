#coding:utf8

from bs4 import BeautifulSoup
import re
import urllib.parse

class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        #https://baike.baidu.com/item/Python/407313
        links = soup.find_all('a', href = re.compile(r"/item/"))
        #find()和find_all()函数的用法
        #find(name,attrs,recursive,text,**wargs)：
        #查找标签，基于name参数
        #查找文本，基于text参数
        #基于正则表达式的查找
        #查找标签的属性，以及基于attrs参数
        #基于函数的查找
        #find()返回第一个符合条件的元素，find_all()返回所有符合条件的结果
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)  # 拼接成新的URL
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        res_data['url'] = page_url

        #标题
        #<dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()
        #get_text():获得标签里面的文本内容，在括号里面加"strip=True"可以去除文本前后多余的空格

        #摘要
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        # ‘html.parser’是解析器的名称，意思是选择用html的解析器来解析html_cont
        # soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        soup = BeautifulSoup(html_cont, 'html.parser')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)   #字典
        return new_urls, new_data


