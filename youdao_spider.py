__author__ = 'hugowen'
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import tornado.httpclient

def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False


if __name__ == "__main__":
    cli = tornado.httpclient.HTTPClient()
    link = 'http://dict.youdao.com/search?q='
    search = raw_input('search: ')
    link += search
    #print link
    data = cli.fetch(link)
    body = data.body.decode('utf8')
    soup = BeautifulSoup(body)

    group = soup.find_all(class_ = 'trans-container')
    if is_chinese(search.decode('utf8')):
        content = group[0].find('ul').find('p')
        print content.find_all('span')[0].get_text()
        for ele in content.find_all(class_ = 'contentTitle'):
            print ele.find('a').get_text()
    else:
        content = group[0].find('ul').find_all('li')
        for ele in content:
            print ele.get_text()

