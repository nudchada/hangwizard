import requests
import json


# List of Harry Potter Characters and Description
# https://dedolist.com/lists/entertainment/harry-potter-characters/
database=requests.get("https://api.dedolist.com/api/v1/entertainment/harry-potter-characters/").json()

names=[]
for item in database:
    names.append(item['name'])

'''
with open("HP_characters.txt", "w") as file:
    for name in names:
        file.write(f"{name}\n")'''

characters=[]
with open("HP_characters.txt","r") as file:
    for line in file:
        characters.append(line.rstrip())