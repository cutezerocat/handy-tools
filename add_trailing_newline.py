#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import io
import platform

def check_platform():
    if platform.system() != 'Linux':
        raise Exception("Your OS is not supported currently")


def get_valid_text_file_list(files):
    valid_file = []
    valid_file_exts = ['.py', '.txt', '.md', '.php', '.sh', '.c', '.h', '.cpp', '.cc', '.html', '.css', '.js', '.hpp']

    for file in files:
        if os.path.isfile(file) and os.path.splitext(file)[1] in valid_file_exts:
            valid_file.append(file)

    return valid_file

def has_trailing_newline(file):
    with open(file, 'rb') as f:
        if f.seekable():
            f.seek(-1, io.SEEK_END)
            return f.read(1) == b'\n'
        else:
            return True

def init():
    check_platform()

    files = get_valid_text_file_list(sys.argv[1:])

    for file in files:
        with open(file, 'a') as f:
            if not has_trailing_newline(file):
                print('append newline into file ' + file)
                f.write('\n')

if __name__ == '__main__':
    init()
