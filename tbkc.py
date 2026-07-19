import os
import requests
os.system("clear")
key = input("What is your Text Belt key?: ")
response = requests.post('https://textbelt.com/text', {
      'phone': '',
      'message': 'test',
      'key': key,
    })
print(response.json())