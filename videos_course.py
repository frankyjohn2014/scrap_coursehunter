from bs4 import BeautifulSoup
import requests
import lxml
import codecs
import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import geckodriver_autoinstaller
import ast


def get_html(site):
# https://curl.trillworks.com/
    r = requests.get(site, headers=headers, data=data)
    return r.text

def get_page_data(html):                         #sources
    soup = BeautifulSoup(html, 'lxml')           #(format_in, parser)
    script = soup.find_all('script')[2]
    dic = []
    for i in script:
        s = i.find('"title": "1')
        file_x = i[s-1:]
        spli_x = file_x.split(',')
        for o in spli_x:
            z = o.lstrip()
            dic.append(z)
        i = 0
        f = 1
        '''В массиве 1 title , в два link'''
        while True:
            try:
                print(dic[i].split(': ')[1].strip('"'))
                print(dic[f].split(': ')[1].strip('"'))
                i += 4
                f += 4
            except:
                break


def main():
    with open("1.html", "r") as read_file:
        ss = {}
        data = read_file.read()
        clear_data=data.replace('\'', '')
        clear_data1 = clear_data.strip('[ ]')
        clear_data2 = clear_data1.split(',')
        ''' Вставить перебор для получения всех ссылок текущего урока'''
        print(clear_data2[1])
        get_page_data(get_html(clear_data2[1]))

if __name__ == '__main__':
    main()