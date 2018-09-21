# coding=utf-8
"""
 网络文件下载
"""
import urllib.request


jpg_link = 'http://i.meizitu.net/2018/09/12b01.jpg'  #图片链接

urllib.request.urlretrieve(jpg_link, 'F:/python/00001.jpg')

print("下載完成")


# def getUrl(url):
#     html = urlopen(url).read().decode()
#     imreg = re.compile('https://pic[0-9]\.zhimg\.com/[a-z 0-9]*_b\.jpg')
#     links = re.findall(imreg, html)
#
#     i = 0
#     for link in links:
#         i += 1
#         print(link)
#         path = 'F:/python/%d.jpg' % i
#         urlretrieve(link, path)
#
# getUrl('https://www.zhihu.com/question/40007169#answer-29511584')

# print("下載完成")
#
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
#
# req = urllib.request.Request(url = 'http://i.meizitu.net/2018/09/12b01.jpg', headers = headers)
#
# feeddata = urllib.request.urlopen(req).read()
#
# print(feeddata)
#
# print("下載完成")