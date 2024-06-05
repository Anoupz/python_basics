weather: dict = {
    "city": "New York",
    "temperature": 32,
    "humidity": 90,
    "metadata": {"type": "cloudy", "wind": 10, "precipitation": 0},
}


print(weather["metadata"]["type"])

# to get the value of a key
print(weather.get("temperature"))  # 32

# to delete a value
weather.pop("humidity")  # removes the key and value

for key, value in weather["metadata"].items():
    print(f"{key}: {value}")
