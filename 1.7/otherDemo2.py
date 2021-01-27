"""
@project:1.7
@author:zlh
@file:spider.py
@time:2021/1/8 8:55
"""
import threading
import time

from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt
import sqlite3

import requests
from lxml import etree


def main():
    #1.爬取网页
    baseurl = "https://search.gitee.com/?skin=rec&type=repository&q=%E6%AF%95%E4%B8%9A%E8%AE%BA%E6%96%87%E7%B3%BB%E7%BB%9F&repo=&reponame=&pageno="
    datalist = getData(baseurl)
    savepath = ".\\豆瓣电影Top250.xsl"
    #askURL(baseurl)
    print(getData(baseurl))

#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,1):
        #url = baseurl + str(i*25)
        html = askURL(baseurl)
        #print(html)
        # 2.解析数据
        detail_eroot = etree.HTML(html)
        print("++++++++++++++++",detail_eroot)
        skills_list_divs = detail_eroot.xpath('//*[@id="hits-list"]/div/div[1]/div/a/@href')
        print(skills_list_divs)
        items = []
        #嵌套获取网页
        for skill_div in skills_list_divs:
            item = {}
            html2 = askURL(skill_div)
            soup = BeautifulSoup(html2, "html.parser")
            #1.获取star数
            find_class = soup.find(attrs={'class':'desc action-social-count'})
            #print(find_class)
            star = find_class.string
            nStr = ""
            nStr = nStr.join(star)
            starr = int(nStr)
            print("star数",starr)

            print("--------------")
            # 2.获取简介
            find_span = soup.find_all('span',class_="git-project-desc-text")[0]
            # print(find_class)
            introduction = find_span.text

            print("简介",introduction)

            '''
            detail_page = etree.HTML(html2)
            #print(detail_page)
            watch = detail_page.xpath('//*[@id="git-project-branch"]/div[1]/span')
            print(watch)
            item["wat"] = watch
            star = detail_page.xpath('/html/body/div[3]/div[1]/div[2]/div/div/div/span[2]/a[2]')
            item["st"] = star
            fork = detail_page.xpath('/html/body/div[3]/div[1]/div[2]/div/div/div/span[3]/a[2]')
            item["fo"] = fork
            print(item)
            items.append(item)
            '''
    return items



def askURL(url):
    head = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
    }
    request = urllib.request.Request(url=url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html



if __name__ == '__main__':
    main()
