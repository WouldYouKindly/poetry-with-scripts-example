import requests


def main():
    print(requests.get('https://httpbin.org/status/200'))
