# coding:utf - 8
from urllib.request import urlopen
from urllib.request import Request
import random
import re
from bs4 import BeautifulSoup

def gethtml(url):
    """
     获取网页
      """
    page = urlopen(url)
    html = page.read().decode("utf-8")
    return html

item="http://www.mzitu.com/151787"

def getImage(url):
    """
     获取图片下载地址
      """
    content = gethtml(url)
    soup = BeautifulSoup(content, 'html.parser')
    c = soup.find('img')
    c= c.get('src')
    return c

def getImageName(filePath):
    """
     获取图片名字
      """
    return str(filePath).split('/')[-1]

def getContent(url, headers):
    """
    此函数用于抓取返回403禁止访问的网页
    """
    random_header = random.choice(headers)

    """
    对于Request中的第二个参数headers，它是字典型参数，所以在传入时
    也可以直接将个字典传入，字典中就是下面元组的键值对应
    """
    req = Request(url)
    req.add_header("User-Agent", random_header)
    req.add_header("GET", url)
    # req.add_header("Host", "www.mzitu.com")
    req.add_header("Referer", "http://www.mzitu.com/")
    content = urlopen(req).read()
    return content

def downLoad(url,name):
    """
     下载图片
      """
    my_headers = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"]
    open("F:/python/image/" + str(name), 'wb').write(getContent(url, my_headers))

def getNextPage(url):
    """
    获取下一页
    :return:
    """
    content = gethtml(url)
    soup = BeautifulSoup(content, 'html.parser')
    collection = soup.findAll('a')
    for c in collection:
        if(str(c.find('span')).count("下一页»")>0):
            print(c.get("href"))
            return c.get("href")
    return ''
def downLoadPage(url):
    imagePath = getImage(url)
    print(imagePath)
    imageName = getImageName(imagePath)
    print(imageName)
    downLoad(imagePath, imageName)
    nextPage = getNextPage(url)
    print(nextPage)
    if (nextPage ==''):
        return
    downLoadPage(nextPage)

def getTitleNextPage(url):
    """
    获取下一页
    :return:
    """
    content = gethtml(url)
    soup = BeautifulSoup(content, 'html.parser')
    collection = soup.findAll('a')
    for c in collection:
        if(str(c).count("下一页»")>0):
            print(c.get("href"))
            return c.get("href")
    return ''

print(getTitleNextPage("http://www.mzitu.com/"))

count=1
def downloadTitle(count=None):
    print(count)

for c in range(10):
    count+=1
    downloadTitle(count)
# downLoadPage(item)

# imagePath=getImage(item)
# print(imagePath)
# imageName=getImageName(imagePath)
# print(imageName)
# downLoad(imagePath,imageName)
