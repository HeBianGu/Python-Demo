# coding=utf-8
import urllib.request

"""
 爬取html脚本
"""
def gethtml(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode("utf-8")

    return html

url1 = "http://www.mzitu.com/150384/12"

html = gethtml(url1)

print(html)
