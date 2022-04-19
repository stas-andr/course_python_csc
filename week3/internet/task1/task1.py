import requests
from bs4 import BeautifulSoup

url1 = input()
url2 = input()
# url1 = 'https://stepic.org/media/attachments/lesson/24472/sample1.html'
# url2 = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'

def find_cicle_url(url1, url2):
    request = requests.get(url1)
    if request.status_code != 200:
        print('No')
    else:
        file1 = request.text
        soup = BeautifulSoup(file1, 'lxml')
        urls = soup.find_all('a', href=True)
        for url in urls:
            req = requests.get(url['href'])
            if req.status_code == 200:
                file2 = req.text
                soup_file2 = BeautifulSoup(file2, 'lxml')
                urls_file2 = soup_file2.find_all('a', href=True)
                urls_file2 = [elem['href'] for elem in urls_file2]
                if url2 in urls_file2:
                    print('Yes')
                    return
        print('No')

find_cicle_url(url1, url2)