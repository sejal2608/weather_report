import requests

api_key = "27293c31d473e9d4ea83c9e1af70f543"

city = input("Enter city name: ").strip()

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city + ",IN",
    "appid": api_key,
    "units": "metric"
}

response = requests.get(url, params=params)

print("STATUS CODE:", response.status_code)
print("RAW RESPONSE:", response.text)

if response.status_code != 200:
    print("City not found or API error")
    exit()

data = response.json()

print("\n🌤 Weather Report")

print("City:", data["name"])
print("Humidity:", data["main"]["humidity"], "%")
print("Wind Speed:", data["wind"]["speed"], "m/s")
print("Wind Direction:", data["wind"].get("deg", "N/A"), "degrees")
print("Condition:", data["weather"][0]["description"])
