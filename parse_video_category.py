from bs4 import BeautifulSoup
import requests
import lxml
import codecs
import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import geckodriver_autoinstaller

def get_html(site):
    r = requests.get(site)
    return r.text

def get_page_data(html):                         #sources
    soup = BeautifulSoup(html, 'lxml')           #(format_in, parser)

    print(soup)

    # for article in articles:
    #     a = article.find('div', class_='course-details-bottom').find_all('a')
    #     for href in a:
    #         dict_href = href['href']
    #         urls.append({'href':dict_href})


def main():
    with open("1.html", "r") as read_file:
        ss = []
        data = read_file.read()
        clear_data=data.replace('\'', '')
        clear_data1 = clear_data.strip('[ ]')
        clear_data2 = clear_data1.split(',')
        # print(os.path.basename('geckodriver'))
        driver = webdriver.Firefox(executable_path='/home/frank/Desktop/scrap_coursehunter/geckodriver')
        print(driver.get(clear_data2[0]))
        # r = requests.get(clear_data2[0])
        # print(r.text) #loop all

        # for elem in clear_data2:
        #     r = requests.get(elem)
        #     print(r.text) #loop all


if __name__ == '__main__':
    main()