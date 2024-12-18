import requests

# Your code here

url = 'https://assets.breatheco.de/apis/fake/sample/project1.php'

# Realizar una petición GET al sitio web
response = requests.get(url)

# comprobar si hemos tenida éxito en la petición
if response.status_code==200:
  project_data = response.json()
  project_name = project_data["name"]
  print(project_name)
else:
    print("Fail")