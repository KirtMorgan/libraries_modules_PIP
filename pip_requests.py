import requests
requests_website = requests.get('https://docs.python.org/3/library/')
print(requests_website.headers)
