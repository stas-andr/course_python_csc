import json

input_from = """[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]"""
js = json.loads(input_from)

for item in js:
    print(item['name'])