#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests
from bs4 import BeautifulSoup
import argparse

HEADERS = json.load(open('firefox_headers.json'))['headers']
try:
    URL = open('.user-config/ziroom_url.txt').read().strip()
except FileNotFoundError:
    print('请在 .user-config/ziroom_url.txt 内保存你的自如搜索结果页网址，例如 http://www.ziroom.com/z/nl/.html?qwd=%E5%BD%A9%E8%99%B9%E6%96%B0%E5%9F%8E')
    exit(1)

def house_status(webpsrc):
    if webpsrc.find('defaultPZZ') != -1:
        if webpsrc.find('canbook') != -1:
            return '可预定'
        else:
            return '配置中'
    else:
        return '可入住'

def get_house_detail(house_li):
    detail = {}

    house_name = house_li.find(class_='t1')
    detail['name'] = house_name.string.strip()
    detail['url'] = 'http://' + house_name['href']
    house_price = house_li.find(class_='price').contents
    detail['price'] = house_price[0].strip() + house_price[1].string
    house_properties = house_li.find(class_='detail').find_all('span')
    detail['detail'] = '、'.join([i.string.strip() for i in house_properties])
    detail['status'] = house_status(house_li.find('img')['_webpsrc'])

    return detail

def print_house_details(house_list, args):
    for i in house_list.find_all('li'):
        house = get_house_detail(i)

        if args.display_available_house and house['status'] == '配置中':
            continue
        print('{:<20}{:^15} {:^5}\t{}'.format(house['name'], house['price'], house['status'], house['detail']))
        if args.show_url:
            print('{}'.format(house['url']))


def argu_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--display-available-house", help='只显示可用的房子', action='store_true')
    parser.add_argument('-u', '--display-url', help='显示住房链接', action='store_true')

    return parser.parse_args()

def init():
    args = argu_parser()
    s = requests.Session()

    soup = BeautifulSoup(s.get(URL, headers=HEADERS).text, 'lxml')
    house_list = soup.find_all(id='houseList')[0]

    print_house_details(house_list, args)

if __name__ == '__main__':
    init()
