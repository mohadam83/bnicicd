import requests
print("hello world")
print("Push ulang")

response = requests.get("https://www.google.com")

print(response.text)