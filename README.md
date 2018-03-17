# Handy Tools

These tools is used to automatically handle some tedious tasks, just for fun and to relax!

## Description

* [update_kernel.py](#update_kernelpy)
* [check_online_file_sha256.sh](#check_online_file_sha256sh)
* [download_bing_wallpaper](#download_bing_wallpaperpy)
* [add_trailing_newline.py](#add_trailing_newlinepy)

## Usage and Function

### update_kernel.py

Install the **up-to-date mainline generic and amd64** kernel for Ubuntu, recommended to run only on the **non-production environment server** because these kernels are not supported and are not appropriate for production use.

### check_online_file_sha256.sh

Usage: check_online_file_sha256.sh *ONLINE_FILE_URL*

Calculate the SHA256 of the file located at ONLINE_FILE_URL .

### download_bing_wallpaper.py

Download Bing daily wallpaper, on Windows, it will save to D:\temp\bing, on Linux, save to /tmp .

### add_trailing_newline.py

Usage: add_trailing_newline.py FILE...

Append newline character into FILES... if the FILE end without a newline.

Currently Support OS: **Linux**

Currently Support File Type: **.py, .txt, .md, .php, .sh, .c, .h, .cpp, .cc, .html, .css, .js, .hpp**
