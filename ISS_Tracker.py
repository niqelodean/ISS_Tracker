import requests
import time
import os

WEBHOOK_URL = os.getenv('WEBHOOK_URL')
INTERVAL = 7200

def get_iss_location():
    response = requests.get('http://api.open-notify.org/iss-now.json')
    data = response.json()

    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]
    timestamp = data["timestamp"]

    return latitude, longitude, timestamp

def send_iss_location_to_discord(latitude, longitude, timestamp):
    message = {
        "content": f"Current ISS Location:\nLatitude: {latitude}\nLongitude: {longitude}\nTimestamp: {timestamp}"
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
