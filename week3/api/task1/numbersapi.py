import requests

with open("dataset_24476_3.txt") as fi:
    numbers = fi.readlines()
    for number in numbers:
        number = int(number)
        url_api = f"http://numbersapi.com/{number}/math?json=true"

        res = requests.get(url_api)
        json_res = res.json()

        if json_res['found']:
            print("Interesting")
        else:
            print("Boring")
