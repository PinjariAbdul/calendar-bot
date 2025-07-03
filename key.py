import requests

proxies = requests.utils.get_environ_proxies("https://www.google.com")
print("Detected Proxies:", proxies)
