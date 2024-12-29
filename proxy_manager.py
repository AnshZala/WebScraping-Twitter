import requests
import random

class ProxyManager:
    def __init__(self, proxy_list_url):
        self.proxy_list_url = proxy_list_url
        self.proxies = self.fetch_proxies()

    def fetch_proxies(self):
        response = requests.get(self.proxy_list_url)
        return response.text.strip().split('\n')

    def get_random_proxy(self):
        return random.choice(self.proxies)

# Usage:
# proxy_manager = ProxyManager('http://your-proxymesh-url.com/proxy-list')
# proxy = proxy_manager.get_random_proxy()