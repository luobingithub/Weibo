
# coding: utf-8

# In[147]:

import re
import json
import requests
from bs4 import BeautifulSoup

import pandas as pd
import numpy as np
from pandas import DataFrame
from pandas import Series
from bs4 import BeautifulSoup


# In[125]:

cookie = {"Cookie": "_T_WM=13e8125ac705b1f30deae994b1945f84; SUB=_2A257-94jDeRxGedG4lIS8S_FzT2IHXVZB-JrrDV6PUJbrdBeLVndkW1LHetz12M_Ehor3QpKl-kQvldy6x2olA..; SUHB=0jBJD-MwWKmVHU; SSOLoginState=1459596915; _TTT_USER_CONFIG_H5=%7B%22ShowMblogPic%22%3A1%2C%22ShowUserInfo%22%3A1%2C%22MBlogPageSize%22%3A%2250%22%2C%22ShowPortrait%22%3A1%2C%22CssType%22%3A0%2C%22Lang%22%3A1%7D; gsid_CTandWM=4uUgCpOz5gZEejhk0SZIx7VKTfv; _T_WL=1; _WEIBO_UID=1890311961; M_WEIBOCN_PARAMS=uicode%3D20000174"}
a = 1
r = requests.get('http://weibo.cn/kaifulee?filter=1&page='+str(a), cookies = cookie)


# In[134]:

# 用bs来解析html
soup = BeautifulSoup(r.text)


# In[77]:

print soup.prettify()


# In[ ]:

\xe8\xb5\x9e
\xe8\xbd\xac\xe5\x8f\x91
\xe8\xaf\x84\xe8\xae\xba


# In[219]:

spans = soup.find_all('a') #tag 为 a 的取出来，用正则匹配
like = re.findall('赞\[\d+\]', str(spans))
repost = re.findall('转发\[\d+\]', str(spans))
comment = re.findall('评论\[\d+\]', str(spans))


# In[220]:

like_list = re.findall('\d+', str(like)) #str 转化为 int list
repost_list = re.findall('\d+', str(repost))
comment_list = re.findall('\d+', str(comment))


# In[224]:

like_df = like_list[3:40:4] #间隔4个取数
repost_df = repost_list[4:50:5]
comment_df = comment_list[3:40:4]


# In[238]:

date = soup.find_all('span', attrs={'class':'ct'}) #获取时间
date_df = pd.Series(list(date)).map(lambda x: x.string) 


# In[240]:

df = pd.DataFrame() #建立空df，添加数据
df['like'] = like_df
df['repost'] = repost_df
df['comment'] = comment_df
df['date'] = date_df
df


# In[284]:

# 先做一个，建好dataframe
cookie = {"Cookie": "_T_WM=13e8125ac705b1f30deae994b1945f84; SUB=_2A257-94jDeRxGedG4lIS8S_FzT2IHXVZB-JrrDV6PUJbrdBeLVndkW1LHetz12M_Ehor3QpKl-kQvldy6x2olA..; SUHB=0jBJD-MwWKmVHU; SSOLoginState=1459596915; _TTT_USER_CONFIG_H5=%7B%22ShowMblogPic%22%3A1%2C%22ShowUserInfo%22%3A1%2C%22MBlogPageSize%22%3A%2250%22%2C%22ShowPortrait%22%3A1%2C%22CssType%22%3A0%2C%22Lang%22%3A1%7D; gsid_CTandWM=4uUgCpOz5gZEejhk0SZIx7VKTfv; _T_WL=1; _WEIBO_UID=1890311961; M_WEIBOCN_PARAMS=uicode%3D20000174"}
a = 1
r = requests.get('http://weibo.cn/kaifulee?filter=1&page='+str(a), cookies = cookie)
soup = BeautifulSoup(r.text)

spans = soup.find_all('a') #tag 为 a 的取出来，用正则匹配
like = re.findall('赞\[\d+\]', str(spans))
repost = re.findall('转发\[\d+\]', str(spans))
comment = re.findall('评论\[\d+\]', str(spans))

like_list = re.findall('\d+', str(like)) #str 转化为 int list
repost_list = re.findall('\d+', str(repost))
comment_list = re.findall('\d+', str(comment))

like_df = like_list[3:40:4] #间隔4个取数
repost_df = repost_list[4:50:5]
comment_df = comment_list[3:40:4]

date = soup.find_all('span', attrs={'class':'ct'}) #获取时间
date_df = pd.Series(list(date)).map(lambda x: x.string) 

df = pd.DataFrame() #建立空df，添加数据
df['like'] = like_df
df['repost'] = repost_df
df['comment'] = comment_df
df['date'] = date_df


# In[285]:

for a in range(2,72): #一共71页
    r = requests.get('http://weibo.cn/kaifulee?filter=1&page='+str(a), cookies = cookie)
    soup = BeautifulSoup(r.text)
    
    spans = soup.find_all('a') #tag 为 a 的取出来，用正则匹配
    like = re.findall('赞\[\d+\]', str(spans))
    repost = re.findall('转发\[\d+\]', str(spans))
    comment = re.findall('评论\[\d+\]', str(spans))

    like_list = re.findall('\d+', str(like)) #str 转化为 int list
    repost_list = re.findall('\d+', str(repost))
    comment_list = re.findall('\d+', str(comment))

    like_df = like_list[3::4] #间隔4个取数
    repost_df = repost_list[4::5]
    comment_df = comment_list[3::4]

    date = soup.find_all('span', attrs={'class':'ct'}) #获取时间
    date_df = pd.Series(list(date)).map(lambda x: x.string) 

    df_new = pd.DataFrame() #建立空df，添加数据
    df_new['like'] = like_df
    df_new['repost'] = repost_df
    df_new['comment'] = comment_df
    df_new['date'] = date_df
    
    df = pd.concat([df,df_new],ignore_index=True)


# In[286]:

df


# In[287]:

df.to_csv('/Users/stepovers/Downloads/lkf.csv',sep=';', encoding='utf-8')


# In[ ]:



