import requests

# Your code here

url = 'https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php'

# Realizar una petición GET al sitio web
response = requests.get(url)

# comprobar si hemos tenida éxito en la petición
if response.status_code==200:
   body = response.json()    
   
   first_post = body["posts"][0]
   author_dict = first_post["author"]
   author_name = author_dict["name"]
   print(author_name)
else: print('fail')
