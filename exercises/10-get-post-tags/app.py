import requests

def get_post_tags(post_id):
    # Your code here
    url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
    
    response = requests.get(url)

    if response.status_code == 200:
        body = response.json()

        for post in body["posts"]:
            if post["id"] == post_id:
                return post["tags"]
        print("No post found") 
    else:
        print("Fail")
    
    return None


print(get_post_tags(11))