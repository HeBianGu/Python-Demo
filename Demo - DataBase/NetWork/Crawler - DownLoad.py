# coding=utf-8
import urllib.request


jpg_link = 'http://i.meizitu.net/2018/09/12b01.jpg'  #图片链接

urllib.request.urlretrieve(jpg_link, 'F:/python/00001.jpg')

print("下載完成")
