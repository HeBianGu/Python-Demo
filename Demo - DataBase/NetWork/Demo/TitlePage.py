# coding:utf - 8
from urllib.request import urlopen
from urllib.request import Request
import random
import os
from bs4 import BeautifulSoup

def gethtml(url):
    """
     获取网页
      """
    page = urlopen(url)
    html = page.read().decode("utf-8")
    return html

def getIndexPage(urlcontent):
    """
      获取首页子页面
          """
    collection=[]
    soup = BeautifulSoup(urlcontent, 'html.parser')
    img_src = soup.findAll("a")  # 抓取a标签
    for img in img_src:
        lazy = img.findAll('img', class_='lazy')
        if(len(lazy) > 0):
            k = img.get('href')
            collection.append(k)
        # for k in img:
        #     k = k.get('src')
        #     print(k)

    return  collection

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

def getImageFolder(filePath):
    """
     获取图片名字
      """
    return str(filePath).split('http://www.mzitu.com/')[1].split('/')[0]

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
    respose= urlopen(req,None,10)

    if respose is None:
        return ''
    print(respose.getcode())
    # if str(req.getcode()) =='200':
    content = respose.read()
    return content
    # return ''

def downLoad(url,name,folder):
    """
     下载图片
      """
    my_headers = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"]
    path="F:/python/image/"+str(folder)
    if not os.path.exists(path):
        os.makedirs(path)
    path=path + "/" + str(name)
    content=getContent(url, my_headers)
    if content=='':
        return
    with open(path, 'wb') as f:
          f.write(content)

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
            return c.get("href")
    return  ''

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
            return c.get("href")
    return ''

def downLoadPage(url):
    print("当前页：" + url)
    imagePath = getImage(url)
    imageName = getImageName(imagePath)
    imageFolder=getImageFolder(url)
    downLoad(imagePath, imageName,imageFolder)
    nextPage = getNextPage(url)
    if nextPage =='':
        return
    downLoadPage(nextPage)

def downloadTitle(url):
    print("首页："+url)
    content = gethtml(url)
    collection = getIndexPage(content)
    for item in collection:
        downLoadPage(item)
    titleNextPage= getTitleNextPage(url)

    if titleNextPage == '':
        return
    downloadTitle(titleNextPage)

url = "http://www.mzitu.com/"

downloadTitle('http://www.mzitu.com/page/14/')

print("下完了！")


