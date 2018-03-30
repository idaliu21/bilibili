
# coding: utf-8
#python violet_danmu.py

import re
import requests
from bs4 import BeautifulSoup as bs
import xml.etree.ElementTree as ET

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

cid =[29662087,30111683,30655086,30936929,31420238,31933194,32377215,32954880,33480964,34011933,34529031,35104565]

def get_dm(cid):

    #get xml 
    cidnow=cid[0]
    url= "http://comment.bilibili.com/"+str(cidnow)+".xml"
    headers = {'User-Agent':"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36"}
    xml = requests.get(url = url, headers = headers)
    xmldata = xml.text
    tree  = ET.fromstring(xmldata)
    rawlist = tree.findall('d')

    #parsing 
    dmlist=[]
    i=0
    for entry in rawlist:
        #print(entry.text)
        dmlist.append([entry.text])
        attr = entry.get("p").split(',')
        dmlist[i].append(attr)
        i=i+1
    return dmlist
    #print (dmlist)

data = get_dm(cid)

def draw(data):

    #selecting time
    r_time = []
    a_time = []
    for entry in data:
        r_time.append(float(entry[1][0]))

        a_time.append(float(entry[1][4]))
    #print (r_time)

    


    #drawing relative time
    fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(8, 4))

    ax0.hist(r_time, 20, normed=1, histtype='stepfilled', facecolor='g', alpha=0.75)
    ax0.set_title('danmu & relative time in video')

    #drawing absolute time

    ax1.hist(a_time, 20, normed=1, histtype='stepfilled', facecolor='g', alpha=0.75)
    ax1.set_title('danmu & absolute time in the real world')

    fig.tight_layout()
    plt.show()

draw(data)

'''
第一个参数是弹幕出现的时间以秒数为单位。 
第二个参数是弹幕的模式1..3 滚动弹幕 4底端弹幕 5顶端弹幕 6.逆向弹幕 7精准定位 8高级弹幕 
第三个参数是字号， 12非常小,16特小,18小,25中,36大,45很大,64特别大 
第四个参数是字体的颜色以HTML颜色的十进制为准 
第五个参数是Unix格式的时间戳。基准时间为 1970-1-1 08:00:00 
第六个参数是弹幕池 0普通池 1字幕池 2特殊池【目前特殊池为高级弹幕专用】 
第七个参数是发送者的ID，用于“屏蔽此弹幕的发送者”功能 
第八个参数是弹幕在弹幕数据库中rowID 用于“历史弹幕”功能。
'''


'''
def clean_dm(dm):
    dm1 = re.sub(r'\<.*"\>', '', str(dm))
    dm2 = re.sub(r'\</d\>', '', str(dm1))
    return dm2



def print_dm(dmlist,av):
    filename = "av"+str(av)+'.txt'
    with open(filename,'w',encoding='utf-8') as f:
        for dm in dmlist:
            #new_dm = clean_dm(dm)
            f.write(str(dm)+'\n')
    print('Done!')


# In[9]:


def scrape_dm(av):
    if isinstance(av,list):
        for i in av:
            cid = get_cid(i)
            #print(cid)
            #dmlist = get_dm(cid)
            #print_dm(dmlist,i)
    else:
        cid = get_cid(av)
        dmlist = get_dm(cid)
        for d in dmlist:
            print(d)


# In[10]:


av = 21293335


# In[11]:


scrape_dm(av)
'''
