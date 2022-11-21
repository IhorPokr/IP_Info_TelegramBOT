import requests


def response_ip(ip):
    response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
    return response
