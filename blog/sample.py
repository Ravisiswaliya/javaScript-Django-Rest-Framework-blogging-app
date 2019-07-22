import json


config =open('sample.json').read()
a = json.loads(config)
print(a)

