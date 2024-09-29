import requests


def get_ip_location(ip: str) -> dict:
    res = requests.get(f"http://ip-api.com/json/{ip}")
    data = res.json()

    return {
        'country': data.get('country') or "Неизвестно",
        'regionName': data.get('regionName') or "Неизвестно",
        'region': data.get('region') or "Неизвестно",
        'city': data.get('city') or "Неизвестно",
        'timezone': data.get('timezone') or "Неизвестно",
        'org': data.get('org') or "Неизвестно",
    }
