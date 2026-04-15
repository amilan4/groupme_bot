import os
import json
from datetime import datetime
import requests

# Get bot ID from GitHub secret
BOT_ID = os.environ.get("GROUPME_BOT_ID")

if not BOT_ID:
    raise ValueError("Missing GROUPME_BOT_ID environment variable")

# Load birthday data
with open("birthdays.json", "r") as f:
    birthdays = json.load(f)

# Get today's date (MM-DD format)
today = datetime.now().strftime("%m-%d")

print("Today is:", today)

# Find matching birthdays
birthday_people = [
    person["name"]
    for person in birthdays
    if person["date"] == today
]

print("Birthdays found:", birthday_people)

# If there are birthdays, send message
if birthday_people:
    if len(birthday_people) == 1:
        message = f"🎉 Happy Birthday {birthday_people[0]}!"
    else:
        names = ", ".join(birthday_people[:-1]) + f" and {birthday_people[-1]}"
        message = f"🎉 Happy Birthday {names}!"

    print("Sending message:", message)

    response = requests.post(
        "https://api.groupme.com/v3/bots/post",
        json={
            "bot_id": BOT_ID,
            "text": message
        },
        timeout=20
    )

    print("Status:", response.status_code)
    print("Response:", response.text)

    # Fail if GroupMe rejects request
    response.raise_for_status()

else:
    print("No birthdays today. No message sent.")
