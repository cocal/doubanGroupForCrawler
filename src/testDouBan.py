# coding = utf-8
import urllib.request
import re
# import sys
# import 
 
#url = 'http://www.douban.com/group/dbapi/discussion?start=50'


url = 'http://www.douban.com/group/shanghaizufang/'
#proxy_handler = urllib.request.ProxyHandler({'http':'172.21.126.246:8080'})
proxy_handler = urllib.request.ProxyHandler({'http':'172.17.18.80:8080'})
opener = urllib.request.build_opener(urllib.request.HTTPHandler, proxy_handler)
f = opener.open(url)
s_content = f.read()
s_content = s_content.decode('utf-8')
#p = re.compile(r'<h2>.+?"(.+?)href=',re.DOTALL)
p = re.compile(r'<tr class="".+?<a.+?href="(.+?)" title="(.+?)".+?</a>', re.DOTALL)

p2 = re.compile(r'<h3>.+?<p>(.+?)</p>', re.DOTALL)
title = []
urls = []
i = 0
#print(p.findall(s_content))
for x in p.findall(s_content):
    #print(x[0])
    urls.append(x[0])
    title.append(x[1])
    i = i + 1
print('-----title--------' , i)
f_data = open('netdata', 'w', encoding='UTF-8')
f_urls = open('neturl', 'w', encoding='UTF-8')
for m in range(0, len(title)):
    print(title[m])
    f_data.write(title[m] + '\n')
    f_urls.write(urls[m] + '\n')

f_data.close()
f_urls.close()
"""
for n in range(0,len(title)):
    print(n,'---title : ', title[n])
    topic_conten = opener.open(urls[n]).read()
    topic_conten = topic_conten.decode('UTF-8')
    print(p2.findall(topic_conten))
	#for 
 """ 
