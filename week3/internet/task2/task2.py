import re
import requests

url_html = "http://pastebin.com/raw/7543p0ns"
# file_html = requests.get(url_html).text

file_html = """<a href="http://stepic.org/courses">
<a href="ftp://www.mya.ru">
<a href='https://stepic.org'>
<a link href='http://neerc.ifmo.ru:1345'>
<a target="blank" href='http://sasd.ifmo.ru:1345'>
<a href='http://neerc.ifmo.ru:1345'>
<a href="../some_path/index.html">
<a href="https://www.ya.ru">
<a href="ftp://mail.ru/distib" >
<a href="bya.ru">
<a href="http://www.ya.ru">
<a href="www.kya.ru">
<a href="../skip_relative_links">
<a href="http://stepic.org/courses">
<a class = "hello" href= "http://ftepic.org/courses" id="dfdf">
<p class = "hello" href= "http://dtepic.org/courses">
<a class = "hello" href = "http://a.b.vc.ttepic.org/courses">
<a href='https://stepic.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href = "ftp://mail.ru/distib" >
<a href= "ya.ru">
<a href ="www.ya.ru">
<a href="../skip_relative_links">
<link rel="image_src" href="https://examaple.org/files/6a2/72d/e09/6a272de0944f447fb5972c44cc02f795.png" />
<a href="http://www.gtu.edu.ge/index_e.htm" target="_top">Georgian Technical University</a>﻿"""
print(file_html)
pattern = r'(<a href ?= ?[\'\"])(?!../)(\w+://)?([\w.]+)'
urls_set = set()

urls = re.findall(pattern, file_html)
print(urls)
for url in urls:
    urls_set.add(url[2])

urls = sorted(list(urls_set))

for url in urls:
    print(url)
