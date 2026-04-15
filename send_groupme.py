import os
import json
from datetime import datetime
import requests

BOT_ID = os.environ["GROUPME_BOT_ID"]

with open("birthdays.json", "r") as f:
    birthdays = json.load(f)

today = datetime.now()
today_month = today.month
today_day = today.day

birthday_people = [
    person["name"]
    for person in birthdays
    if person["month"] == today_month and person["day"] == today_day
]

if birthday_people:
    if len(birthday_people) == 1:
        message = f"🎉 Happy Birthday {birthday_people[0]}!"
    else:
        names = ", ".join(birthday_people[:-1]) + f" and {birthday_people[-1]}"
        message = f"🎉 Happy Birthday {names}!"

    response = requests.post(
        "https://api.groupme.com/v3/bots/post",
        json={
            "bot_id": BOT_ID,
            "text": message
        },
        timeout=20
    )

    print("Status:", response.status_code)
    print("Body:", response.text)
    response.raise_for_status()
else:
    print("No birthdays today.")
