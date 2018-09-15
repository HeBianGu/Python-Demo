from urllib.request import urlopen
from urllib.request import urlretrieve
import re


def getUrl(url):
    html = urlopen(url).read().decode()
    imreg = re.compile('https://pic[0-9]\.zhimg\.com/[a-z 0-9]*_b\.jpg')
    links = re.findall(imreg, html)

    i = 0
    for link in links:
        i += 1
        print(link)
        path = 'F:/python/%d.jpg' % i
        urlretrieve(link, path)

getUrl('https://www.zhihu.com/question/40007169#answer-29511584')