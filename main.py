import requests
from send_email import send_email

api_key = "951b25f5eb4c4761befc3cc2fb0b01e1"
url = (
    "https://newsapi.org/v2/everything?q=tesla&"
    "sortBy=publishedAt&"
    "apiKey=951b25f5eb4c4761befc3cc2fb0b01e1"
)

# make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)
