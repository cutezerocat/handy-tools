#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from functools import cmp_to_key
import datetime
import subprocess

import os

KERNEL_FETCH_URL = 'http://kernel.ubuntu.com/~kernel-ppa/mainline/'

def write_log(version_number=None, warning=None):
    with open('/root/kernel_update.log', 'a') as f:
        if version_number:
            f.write(str(datetime.datetime.now()) + ' updates kernel: ' + version_number + '\n')
        if warning:
            f.write('----------\n' + str(datetime.datetime.now()) + ' has a WARNING!!!\n----------\n' + warning + '\n----------\n')

# get kernel version
def get_kernel_version():
    # use `uname -r`
    return subprocess.getoutput('uname -r').split('-')[0]

# companion
def cmp(s1, s2):
    s1 = s1.split('.')
    s2 = s2.split('.')
    for i in range(max(len(s1), len(s2))):
        if i >= len(s1): return -1
        if i >= len(s2): return 1
        if int(s1[i]) != int(s2[i]):
            return int(s1[i]) - int(s2[i])

    return 0

def init():
    soup = BeautifulSoup(requests.get(KERNEL_FETCH_URL).text, "lxml")

    a_list_from_html = soup.find_all('a')[19: ]
    version_list = [ i.text[1:-1] for i in a_list_from_html if i.text.find('-') == -1 ]
    max_version = max(version_list, key = cmp_to_key(cmp))

    if cmp(max_version, get_kernel_version()) == 1:
        base_url = 'http://kernel.ubuntu.com/~kernel-ppa/mainline/v'+max_version+'/'
        new_soup = BeautifulSoup(requests.get(base_url).text, 'lxml')
        download_available_url = new_soup.find_all('a')
        download_available_url = [ base_url+url['href'] for url in download_available_url if url.text.find('amd64') != -1 and url.text.find('generic') != -1 ][:2]

        os.system('rm linux-*')
        os.system('wget ' + ' '.join(download_available_url))
        os.system('dpkg -i linux-*')

        write_log(version_number=max_version)

if __name__ == '__main__':
    try:
        init()
    except Exception as e:
        write_log(warning=str(e))

