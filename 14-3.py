import requests
import re

url="http://goo.gl/U7mSQl" 
response = requests.get(url) #GET방식
html_contents =response.text
id_results = re.findall(r"([A-Za-z0-9]+\*\*\*)", html_contents)

for result in id_results:
    print(result)

print(id_results)

