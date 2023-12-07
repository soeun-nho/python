import re 
import requests
url="http://finance.naver.com/item/main.nhn?"

response = requests.get(url,{"code":"005930"})
#response = requests.get("url")
html_contents = response.text

results = re.findall("(\<dl class=\"blind\"\>)([\s\S]+?)(\<\/dl\>)", html_contents)
print(results)

#음.
samsung_stock = results[0]
samsung_index = results[1]

index_list = re.findall("(\<dd\>)([\s\S]+?)(\<\/dd\>)", samsung_index)
for index in index_list:
    print(index[1])
