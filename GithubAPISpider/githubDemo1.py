"""
@project:GithubAPISpider
@author:zlh
@file:githubDemo1.py
@time:2021/1/23 22:09
"""
from urllib.request import urlopen
from urllib.request import Request
import datetime
import json


def get_statistics(owner, name, headers):
    #https://api.github.com/repos/{ownthink}/{name}/stats/contributors?page=1&per_page=10
    url = 'https://api.github.com/repos/{owner}/{name}/stats/contributors?page=1&per_page=10'.format(owner=owner,
                                                                                                      name=name)
    req = Request(url, headers=headers)
    response = urlopen(req).read()
    if len(response) == 0:
        return response
    else:
        result = json.loads(response.decode())
        print("resultlen", len(result))
        return result


def get_results(search, headers):
    print("adsg")
    # https://api.github.com/search/repositories?q=KnowledgeGraphData&page=1&per_page=10&sort=stars&order=desc
    url = 'https://api.github.com/search/repositories?q={search}&page=1&per_page=10&sort=stars&order=desc'.format(
        search=search)
    req = Request(url, headers=headers)
    response = urlopen(req).read()
    result = json.loads(response.decode())

    return result


if __name__ == '__main__':
    # 这里用不用转义符没差别
    search = '"KnowledgeGraphData"'

    headers = {'User-Agent': 'Mozilla/5.0',
               'Authorization': 'token b5958055635de014872bc1c5b135cd7becbe9ffa',
               'Content-Type': 'application/json',
               'Accept': 'application/json'
               }

    results = get_results(search, headers)
    print("results",results)

    f = open('ContributorsInfo4.txt', 'w')
    i = 0
    for item in results['items']:
        i= i+1
        print(i)
        #仓库名字
        name = item['name']
        #星星数
        star = item['stargazers_count']
        #仓库拥有者
        owner = item['owner']['login']

        language = str('0')
        user = str('0')
        commits = 0
        #开发语言
        language = item['language']

        stats = get_statistics(owner, name, headers)
        contributor_list = []
        count = len(stats)
        for i in range(0, count):
            user = stats[i]['author']['login']
            commits = stats[i]['total']
            deletions = 0
            additions = 0
            first_commit = None
            last_commit = None
            for week in stats[i]['weeks']:
                deletions += week['d']
                additions += week['a']
                # assume that weeks are ordered
                if first_commit is None and week['c'] > 0:
                    first_commit = week['w']
                if week['c'] > 0:
                    last_commit = week['w']
            contributor_list.append([name,
                                     owner,
                                     star,
                                     language,
                                     count,
                                     user,
                                     commits,
                                     additions,
                                     deletions,
                                     datetime.datetime.fromtimestamp(first_commit).strftime('%Y-%m-%d'),
                                     datetime.datetime.fromtimestamp(last_commit).strftime('%Y-%m-%d')
                                     ])
        for contributor in contributor_list:
            print(contributor, file=f)