#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import os
import platform
import subprocess

FIREFOX_HEADERS = json.load(open('firefox_headers.json'))['headers']
BING_IMAGE_API = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US'

def set_save_path():
    if platform.system() == 'Windows':
        os.chdir('D:\\temp\\bing')
    elif platform.system() == 'Linux':
        if subprocess.getoutput('uname -a').find('Microsoft') != -1:
            os.chdir('/mnt/d/temp/bing')
        else:
            os.chdir('/tmp')
    else:
        raise Exception('Not Implemented')

def init():
    bing_image_url = requests.get(BING_IMAGE_API, headers=FIREFOX_HEADERS).json()['images'][0]['url']
    set_save_path()
    with open(os.path.basename(bing_image_url), 'wb') as f:
        f.write(requests.get('https://www.bing.com/' + bing_image_url, headers=FIREFOX_HEADERS).content)

if __name__ == '__main__':
    init()
