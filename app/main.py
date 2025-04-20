import os
import requests


def get_weather() -> None:
    API_KEY = os.getenv("API_KEY")
    if not API_KEY:
        print("API_KEY not set")
        return

    city = "Paris"
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
    response = requests.get(url)
    if response.status_code == 200:
        weather = response.json()

        temperature = weather["current"]["temp_c"]
        condition = weather["current"]["condition"]["text"]

        print(f"Weather in {city}: {temperature}*C, {condition}")
    else:
        print(f"{response.status_code}: {response.text}")


if __name__ == "__main__":
    get_weather()
