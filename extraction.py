import requests

url = "https://www.fbi.gov/"
page = requests.get(url)

# Voir le code html source
print(page.content)
reponse= requests.get(url)
