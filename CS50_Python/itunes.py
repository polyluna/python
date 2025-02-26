import json
import requests
import sys

if len (sys.argv) != 2:
        sys.exit()

requests.get("https://itunes.apple.com/search?entity=song&limit=1term=" + sys.argv[1])
print(response.json())