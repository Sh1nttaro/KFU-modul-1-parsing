import requests


def get_country_by_ip(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()
    if data["status"] == "success":
        return data["country"]
    elif data["message"] == "invalid query":
        raise Exception("Такого IP не существует")


def main():
    ip = input("Введите IP адрес: ")
    try:
        country = get_country_by_ip(ip)
        print(f"IP Страны: {ip}: {country}")
    except Exception as e:
        print(e)


main()
