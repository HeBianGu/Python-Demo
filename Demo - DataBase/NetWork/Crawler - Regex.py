# coding=utf-8
import urllib.request
import re

"""
 应用正则表达式筛选html脚本
"""

def gethtml(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode("utf-8")

    return html


url = "http://www.mzitu.com/"

url1 = "http://www.mzitu.com/150207/2"

html = gethtml(url1)

regex_img = r"""<div class="main-image">[\s\S]*?</div>"""

matchs = re.findall(regex_img, html)

for match in matchs:
    imgs = re.findall("<img[\\s\\S]*?/>", match)

    for img in imgs:
       url= str(img).split('"')[1]
       print("爬去到图片URL:")
       print(url)



