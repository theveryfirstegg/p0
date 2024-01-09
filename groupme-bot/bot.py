import requests
import time
import json
import os
from dotenv import load_dotenv
import re

load_dotenv()

BOT_ID = os.getenv("BOT_ID")
GROUP_ID = os.getenv("GROUP_ID")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
LAST_MESSAGE_ID = None

def get_images(date=None):
    get_url = "https://api.nasa.gov/planetary/apod?api_key=clRxngihFcTxdYRki2inm2cyHcdnEdvDtcjpy5Gf"
    api_key = "clRxngihFcTxdYRki2inm2cyHcdnEdvDtcjpy5Gf"
    params = {
      'api_key':api_key,
      'date': date,
    }
    response = requests.get(get_url, params=params).json()

    print(response["url"])
    return response["url"]





def send_message(text, attachments=None):
    """Send a message to the group using the bot."""
    post_url = "https://api.groupme.com/v3/bots/post"
    data = {"bot_id": BOT_ID, "text": text, "attachments": attachments or []}
    response = requests.post(post_url, json=data)
    return response.status_code == 202


def get_group_messages(since_id=None):
    """Retrieve recent messages from the group."""
    params = {"token": ACCESS_TOKEN}
    if since_id:
        params["since_id"] = since_id

    get_url = f"https://api.groupme.com/v3/groups/{GROUP_ID}/messages"
    response = requests.get(get_url, params=params)
    if response.status_code == 200:
        # this shows how to use the .get() method to get specifically the messages but there is more you can do (hint: sample.json)
        return response.json().get("response", {}).get("messages", [])
    return []


def process_message(message):
    """Process and respond to a message."""
    global LAST_MESSAGE_ID
    text = message["text"].lower()
    message_id = message["id"]
    pattern = re.compile(r'^apod for \d{4}-\d{2}-\d{2}$')

   

    if message["sender_id"] == "85662324":

        if "hello bot" in text:
            send_message("sup")

    if message["sender_type"] != "bot":

        if "good morning" in text:
            output = "Good morning, "
            sender = message["name"]
            output += sender
            send_message(output)
        
        if "good night" in text:
            output = "Good night, "
            sender = message["name"]
            output += sender
            send_message(output)
        
        if pattern.match(text):
            date = text[-10:]
            image_url = get_images(date)
            send_message(f"The astronomy picture of the day: {image_url}")
            


    LAST_MESSAGE_ID = message["id"]

    

    # i.e. responding to a specific message (note that this checks if "hello bot" is anywhere in the message, not just the beginning)
  


def main():
    global LAST_MESSAGE_ID
    # this is an infinite loop that will try to read (potentially) new messages every 10 seconds, but you can change this to run only once or whatever you want
    while True:
        messages = get_group_messages(LAST_MESSAGE_ID)

        if messages:
            print(messages[0])
            process_message(messages[0])
        # for message in reversed(messages):
            
            
        time.sleep(10)


if __name__ == "__main__":
    main()
