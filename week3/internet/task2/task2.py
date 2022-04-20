import re
import requests

debug = True # для теста

if debug:
    with open('test.html') as test_file:
        file_html = test_file.read()
else:
    url_html = input().rstrip()
    file_html = requests.get(url_html).text

pattern = r'(<a .*?href=[\'\"])(?!../)(\w+://)?([^:/\'\"]+)'
urls_set = set()

urls = re.findall(pattern, file_html)

for url in urls:
    urls_set.add(url[2])

urls = sorted(list(urls_set))

for url in urls:
    print(url)
