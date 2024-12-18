import requests

# Your code here
url = "https://assets.breatheco.de/apis/fake/sample/post.php"
myobj = {'id': '2323','title': '"Very big project'}

response = requests.post(url, json = myobj)

print(response.text)


