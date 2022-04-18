import requests
import re

from bs4 import BeautifulSoup

# url1 = input()
# url2 = input()
url1 = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
url2 = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'

file1 = requests.get(url1).text


soup = BeautifulSoup(file1, 'lxml')
links = soup.find_all('a', href=True)

for link in links:
    print(link['href'])
