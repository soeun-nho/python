import requests
response = requests.get("http://theteamlab.io") #get():전부 읽어옴
print(response.text)