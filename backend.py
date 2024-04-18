import requests

API_KEY = "64b4149dda3c02532c294e8c4b19663e"

def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

if __name__=="__main__":
    print(get_data(place ="Tokyo"))