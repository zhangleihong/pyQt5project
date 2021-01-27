import requests
import json
import argparse
import numpy as np
import csv
import pandas as pd


# 获取指定接口的数据
def fetchUrl(url,repo_full_name):
    '''
    功能：访问 url 的网页，获取网页内容并返回
    参数：目标网页的 url
    返回：目标网页的 html 内容
    '''

    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Authorization': 'token b5958055635de014872bc1c5b135cd7becbe9ffa',
        'Content-Type': 'application/json',
        'method': 'GET',
        'Accept': 'application/json'
    }

    rr = requests.get(url, headers=headers)
    rr.raise_for_status()
    rr.encoding = rr.apparent_encoding
    r = rr.json()
    count = len(r)
    for i in range(count):
        s = []
        s.append(repo_full_name)
        s.append(r[i]['login'])
        #s.append(r[i]['id'])
        #s.append(r[i]['url'])
        #s.append(r[i]['html_url'])
        #s.append(r[i]['followers_url'])
        #s.append(r[i]['following_url'])
        #s.append(r[i]['followers'])
        #s.append(r[i]['following'])
        #s.append(r[i]['name'])
        #csv_list = [repo_full_name, s]
        print(s)
        writer.writerow(s)
    #result = json.loads(r.text)  # json字符串转换成字典

    #return s


if __name__ == '__main__':
    '''
    主函数：程序入口
    '''
    file =  'sa.csv'
    #writer = open('../爬虫/repo2.txt', 'w', encoding='utf-8')
    j = 0
    #csv_list = [[]*3]*len(arr)
    data_list = ['u-login', 'f-login']
    fp_csv = open('user-followings29.csv', 'w', newline='', encoding='utf-8-sig')
    writer = csv.writer(fp_csv)
    # 写入表头标题
    writer.writerow(data_list)
    for line in open(file, encoding='utf-8').readlines()[47360:]:

        conditions = line.strip().split(',')[0]
        #count = int(line.strip().split(',')[5])
        #s_login = line.strip().split(',')[0]
        query_url = 'https://api.github.com/users/' + conditions + '/following'

        fetchUrl(query_url,conditions)

       #print(csv_list)
        #print(fetch_result)
        #writer.write('%s,\n' % (fetch_result))
    #writer.close()

    # 写入表内容

    fp_csv.close()