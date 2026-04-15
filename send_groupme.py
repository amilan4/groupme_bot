import os
import requests

BOT_ID = os.environ["GROUPME_BOT_ID"]

message = "Good morning! Daily check-in reminder."

requests.post(
  "https://api.groupme.com/v3/bots/post",
  json={
    "bot_id": BOT_ID,
    "text": message
  }
)
