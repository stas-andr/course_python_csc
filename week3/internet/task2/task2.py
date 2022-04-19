import re

from bs4 import BeautifulSoup

file_html = """ <a href="http://stepic.org/courses">
                <a href='https://stepic.org'>
                <a href='http://neerc.ifmo.ru:1345'>
                <a href="ftp://mail.ru/distib" >
                <a href="ya.ru">
                <a href="www.ya.ru">
                <a href="../skip_relative_links">"""

soup = BeautifulSoup(file_html, 'lxml')
urls = soup.find_all('a', href=True)
urls = [url['href'] for url in urls]

pattern = r'(^../)?(\w+://)?([\w.]+)'
urls_set = set()

for url in urls:
    match = re.search(pattern, url)
    if not match.group(1):
        urls_set.add(match.group(3))

print(urls_set)
urls = sorted(list(urls_set))
print(urls)


