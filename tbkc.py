import os
import requests
os.system("clear")
key = input("What is your Text Belt key?: ")
os.system("clear")
phonenumber = input("What is your phone number?: ")
response = requests.post('https://textbelt.com/text', {
      'phone': phonenumber,
      'message': 'test',
      'key': key,
    })
print(response.json())