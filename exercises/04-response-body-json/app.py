import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")

if response.status_code ==200:
    time_data = response.json()

    hours = time_data["hours"]
    minutes = time_data["minutes"]
    seconds = time_data["seconds"]
    
    print(f"Current time: {hours} hrs {minutes} min and {seconds} sec")
else: 
    none