"""
@project:GithubAPISpider
@author:zlh
@file:jiaju分词.py
@time:2021/1/25 9:20
"""
import jiagu

#jiagu.init() # 可手动初始化，也可以动态初始化

text = '厦门明天会不会下雨'

words = jiagu.seg(text) # 分词
print(words)

pos = jiagu.pos(words) # 词性标注
print(pos)

ner = jiagu.ner(words) # 命名实体识别
print(ner)
# 独立标准模型路径
# msr：test/extra_data/model/msr.model
# pku：test/extra_data/model/pku.model
# cnc：test/extra_data/model/cnc.model
jiagu.load_model('test/extra_data/model/cnc.model') # 使用国家语委分词标准

words = jiagu.cut('天下无贼是一部电影')

print(words)

# 分词各种模式使用方式


text = '汉服和服装、知识图谱机器人'

words = jiagu.cut(text) # 深度学习分词
print(words)

words = jiagu.seg(text) # 字典分词
print(words)

# jiagu.load_userdict('dict/user.dict') # 加载自定义字典，支持字典路径、字典列表形式。
jiagu.load_userdict(['知识图谱机器人'])

words = jiagu.seg(text) # 自定义分词，字典分词模式有效
print(words)


# 知识图谱关系抽取

# 吻别是由张学友演唱的一首歌曲。
# 苏州大学（Soochow University），简称“苏大”，坐落于历史文化名城苏州。
# 《盗墓笔记》是2014年欢瑞世纪影视传媒股份有限公司出品的一部网络季播剧，改编自南派三叔所著的同名小说，由郑保瑞和罗永昌联合导演，李易峰、杨洋、唐嫣、刘天佐、张智尧、魏巍等主演。
# 姚明（Yao Ming），1980年9月12日出生于上海市徐汇区，祖籍江苏省苏州市吴江区震泽镇，前中国职业篮球运动员，司职中锋，现任中职联公司董事长兼总经理。
text = '吻别是由张学友演唱的一首歌曲'
knowledge = jiagu.knowledge(text)
print(knowledge)

# 情感分析
text = '我找到女朋友啦'
sentiment = jiagu.sentiment(text)
print(sentiment)
# 文本聚类
docs = [
        "百度深度学习中文情感分析工具Senta试用及在线测试",
        "情感分析是自然语言处理里面一个热门话题",
        "AI Challenger 2018 文本挖掘类竞赛相关解决方案及代码汇总",
        "深度学习实践：从零开始做电影评论文本情感分析",
        "BERT相关论文、文章和代码资源汇总",
        "将不同长度的句子用BERT预训练模型编码，映射到一个固定长度的向量上",
        "自然语言处理工具包spaCy介绍",
        "现在可以快速测试一下spaCy的相关功能，我们以英文数据为例，spaCy目前主要支持英文和德文"
    ]
cluster = jiagu.text_cluster(docs)
print(cluster)