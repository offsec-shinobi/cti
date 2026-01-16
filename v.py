import mmh3
import requests
import codecs
response = requests.get("https://www.google.com/favicon.ico")
favicon = codecs.encode(response.content, "base64")
print(mmh3.hash(favicon))
