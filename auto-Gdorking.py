import requests
import os
import json


def file_type(url_get, domain_get, count_get):
    with open('output.txt', 'a') as writer:
        with open('payload.txt', 'r') as file:
            for payload in file:
                requesting = requests.get(f"{url_get}site:{domain_get} {payload.strip()}&num={count_get}")
                response = requesting.text
                data = json.loads(response)
                if "items" in data:
                    for item in data["items"]:
                        try:
                            print(item['link'])
                            writer.write(item['link'] + '\n')
                        except KeyError as e:
                            pass
                else:
                    pass



def changing_Key_or_ID():
    while True:
        getting_input = str(
            input("If you want to change SearchID type 'Id' and for API key type 'API' ")).lower().strip()
        if getting_input == 'api':
            ask3 = str(input("Enter the API key here : "))
            with open('config/api_key.txt', 'w') as writing:
                writing.truncate(0)
                writing.write(ask3)
        elif getting_input == 'id':
            ask4 = str(input("Enter the search id here : "))
            with open('config/api_key.txt', 'w') as writing:
                writing.truncate(0)
                writing.write(ask4)


if not os.path.exists('config/api_key.txt'):
    with open('config/api_key.txt', 'a') as api:
        print("created the api_key.txt created : ")
if os.path.getsize('config/api_key.txt') == 0:
    with open('config/api_key.txt', 'a') as api:
        ask = str(input("Enter your API Key: : "))
        api.write(ask)
if not os.path.exists('config/search_id.txt'):
    with open('config/search_id.txt', 'a') as searchID:
        print("created the api_key.txt created : ")
if os.path.getsize('config/search_id.txt') == 0:
    with open('config/search_id.txt', 'a') as SearchID:
        ask2 = str(input("Enter your Search ID : "))
        SearchID.write(ask2)

while True:
    answer = str(input("Do you want to change API or SearchID (Y/N)"))
    if answer == 'Y':
        changing_Key_or_ID()
        break

    elif answer == 'N':
        break

apikey = open('config/api_key.txt', 'r').read()
search_id = open('config/search_id.txt', 'r').read()

domain = str(input("Enter the Domain name : "))
count = int(input("Enter the Number of search result : "))
url = f"https://www.googleapis.com/customsearch/v1?key={apikey}&cx={search_id}&q="

file_type(url, domain, count)
