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

def timestamp_to_local_datetime(timestamp):
    from datetime import datetime, timezone
    local_dt = datetime.fromtimestamp(timestamp, tz=timezone.utc).astimezone() 
    return local_dt.strftime('%b %d, %Y at %I:%M %p')

def send_iss_location_to_discord(latitude, longitude, timestamp):
    message = {
        "content": f"Current ISS Location:\nLatitude: {latitude}\nLongitude: {longitude}\nTimestamp: {timestamp_to_local_datetime(timestamp)}"
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
