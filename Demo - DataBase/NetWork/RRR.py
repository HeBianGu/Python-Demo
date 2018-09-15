# -*- coding:utf-8 -*-
#__author__ :kusy
#__content__:文件说明
#__date__:2018/7/23 17:01
import urllib.request
import re

def getHtml(url):
    # 如果不加上下面的这行出现会出现urllib.error.HTTPError: HTTP Error 403: Forbidden错误
    # 主要是由于该网站禁止爬虫导致的，可以在请求加上头信息，伪装成浏览器访问User-Agent,具体的信息可以通过火狐的FireBug插件查询
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=url,headers=headers)
    page = urllib.request.urlopen(req)
    html = page.read()
    # print(html)
    return html

def getImg(reg,savePath):
    iCnt = 0
    def giveImg(html):
        imgre = re.compile(reg)
        imglist = re.findall(imgre, html.decode('utf-8'))
        nonlocal iCnt
        for imgurl in imglist:
            urllib.request.urlretrieve(imgurl, savePath + '%s.gif' % iCnt)
            iCnt += 1
    return giveImg


# html = getHtml("http://pic.sogou.com/")
# reg = r'"image":"(.+?)"'  #sougou

reg = r'data-original="(.+?\.gif)"'
savePath = 'F:/python/image/'
g = getImg(reg,savePath)
for i in range(10):
    if i >1:
        print("http://www.budejie.com/" + str(i))
        html = getHtml("http://www.budejie.com/" + str(i))
    else:
        html = getHtml("http://www.budejie.com/")
    g(html)