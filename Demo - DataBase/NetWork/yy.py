# coding=utf-8
import urllib.request


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

req = urllib.request.Request(url = 'http://i.meizitu.net/2018/09/12b01.jpg', headers = headers)

feeddata = urllib.request.urlopen(req).read()

print(feeddata)

print("下載完成")