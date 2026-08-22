# ISS Tracker

A Python script that fetches the real-time location of the International Space Station (ISS) and posts it to Discord every 2 hours — now with reverse geocoding and human-readable timestamps.

## What It Does

- Fetches live ISS coordinates from the [Open Notify API](http://api.open-notify.org/)
- **Reverse geocodes** the coordinates to show what city/country the ISS is over (via [Nominatim](https://nominatim.openstreetmap.org/))
- Converts Unix timestamps to **human-readable local time**
- Posts a formatted message to a Discord webhook
- Runs in a loop, auto-posting every 2 hours
- Handles errors gracefully so it keeps running even if APIs hiccup

## Example Discord Output

```
 ISS Current Location
 Paris
 Lat: 48.8566, Lon: 2.3522
 Aug 22, 2024 at 04:19 PM
```

## What I Learned

| Skill | How I Used It |
|-------|---------------|
| Nested JSON | `data["iss_position"]["latitude"]` — coordinates aren't top-level |
| Chaining APIs | Output from ISS API → input to geocode API |
| Query parameters | `requests.get(url, params={"lat": ..., "lon": ...})` |
| Required headers | `User-Agent` header for Nominatim (blocked without it) |
| Fallback chains | `city or town or village or "Unknown Location"` |
| DateTime formatting | `datetime.fromtimestamp()` + `strftime()` for readable timestamps |
| Discord webhooks | POSTing formatted messages with emojis and newlines |
| Loops & sleep | `while True` + `time.sleep(7200)` for automation |
| Error handling | `try/except` so the loop doesn't die on API failures |
| Entry points | `if __name__ == "__main__"` — learned why it matters for imports |

## Setup

1. Clone the repo
2. Install dependencies:
   ```bash
   pip install requests
   ```
3. Create a Discord webhook in your server (Server Settings → Integrations → Webhooks)
4. Replace `WEBHOOK_URL` in `ISS-Tracker.py` with your actual webhook URL
5. Run it:
   ```bash
   python ISS-Tracker.py
   ```
6. Stop it with `Ctrl + C`

## APIs Used

- [Open Notify ISS Location API](http://api.open-notify.org/iss-now.json) — live ISS coordinates
- [Nominatim Reverse Geocoding](https://nominatim.openstreetmap.org/reverse) — coordinates to place names
