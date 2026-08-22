import requests
import time
from datetime import datetime, timezone


WEBHOOK_URL = ('Your_Discord_Webhook_URL')
INTERVAL = 7200

def get_iss_location():
    response = requests.get('http://api.open-notify.org/iss-now.json')
    data = response.json()

    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]
    timestamp = data["timestamp"]

    return latitude, longitude, timestamp

def  get_location_name (latitude, longitude):
    url = "https://nominatim.openstreetmap.org/reverse"
    parameters = {
        'lat' : latitude,
        'lon' : longitude,
        'format' : 'json'
    }
    headers = {
        'User-Agent' : 'ISS-Tracker/1.0'
    }
    
    response = requests.get(url, params=parameters, headers=headers)
    data = response.json()
    
    address = data.get("address", {})
    
    location = (
        address.get("city") or
        address.get("town") or
        address.get("village") or
        address.get("county") or
        address.get("state") or
        address.get("country") or
        "Unknown Location"
    )
    
    return location

def timestamp_to_local_datetime(timestamp):
    local_dt = datetime.fromtimestamp(timestamp, tz=timezone.utc).astimezone() 
    return local_dt.strftime('%b %d, %Y at %I:%M %p')
    
def send_iss_location_to_discord(latitude, longitude, timestamp):
    location_name = get_location_name(latitude, longitude)
    message = {
        "content":  f"Current ISS Location: {location_name}\n"
                    f'Latitude: {latitude}\n'
                    f'Longitude: {longitude}\n'
                    f'Timestamp: {unic_timestamp_to_am_pm_format(timestamp)}'
    }
    requests.post(WEBHOOK_URL, json=message)

def main():
    while True:
        try:
            latitude, longitude, timestamp = get_iss_location()
            send_iss_location_to_discord(latitude, longitude, timestamp)
            print("Sent to Discord successfully.")
            time.sleep(INTERVAL)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
