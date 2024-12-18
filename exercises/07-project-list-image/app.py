import requests

# Your code here

url = 'https://assets.breatheco.de/apis/fake/sample/project_list.php'

# Realizar una petición GET al sitio web
response = requests.get(url)

# comprobar si hemos tenida éxito en la petición
if response.status_code==200:
   project_data = response.json()
   project_ult_imagen = project_data[-1]["images"]
   print(project_ult_imagen)
else:
    print("Fail")