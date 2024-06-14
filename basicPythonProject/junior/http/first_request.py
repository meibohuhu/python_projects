## requests module
## python3 -m pip install requests

import requests
## get data JSON, turn into Python, we can manipulate
## Params: Query string
## Add as many as query as we want

url = "https://icanhazdadjoke.com/search"
response = requests.get(url,
                        headers= {"Accept": "application/json"},
                        params = {"term": "cat", "limit": 1}
)
data = response.json()
print(data)
print(data["results"])


