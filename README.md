# ISS Tracker

A simple Python script that fetches the real-time location of the International Space Station (ISS) and posts it to Discord every 2 hours.

## What It Does

- Fetches live ISS coordinates from the [Open Notify API](http://api.open-notify.org/)
- Posts latitude, longitude, and timestamp to a Discord webhook
- Runs in a loop, auto-posting every 2 hours
- Handles errors gracefully so it keeps running even if APIs hiccup

## What I Learned

This project levelled me up from my basic weather script:

| Skill | How I Used It |
|-------|---------------|
| Nested JSON | `data["iss_position"]["latitude"]` — the coordinates aren't top-level |
| Discord webhooks | POSTing formatted messages to a webhook URL |
| Loops & sleep | `while True` + `time.sleep(7200)` for automation |
| Error handling | `try/except` so the loop doesn't die on API failures |
| Entry points | `if __name__ == "__main__"` — learned why it matters for imports |

## Setup

1. Clone the repo
2. Install dependencies (just `requests`):
   ```bash
   pip install requests
   ```
3. Create a Discord webhook in your server (Server Settings → Integrations → Webhooks)
4. Replace `WEBHOOK_URL` in the script with your actual webhook URL
5. Run it:
   ```bash
   python ISS-Tracker.py
   ```
6. Stop it with `Ctrl + C`

## API Used

- [Open Notify ISS Location API](http://api.open-notify.org/iss-now.json)
