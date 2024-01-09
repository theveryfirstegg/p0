# GROUP ME BOT

## Angie P0 Bot

## Overview

- I created a GroupMe bot that reads and responds to messages and can send astronomy pictures (or videos) of the day (from the NASA APOD API)

## Functionality
The bot has the following functionality:
- answers messages
    - My bot will respond to the message "hello bot" with "sup" only if it is sent by me, (the bot checks the sender id to make sure it is mine). 
    - If anyone in the group chat (excluding other bots) sends "good morning" or "good night", my bot responds with the message "Good morning," or "Good night," followed by the name of the sender
- sends astronomy pictures of the day
    - The bot can send the astronomy picture of the day for a given day.
    - Anyone in the groupchat can get a link by sending a message that has the following format: "APOD for YYYY-MM-DD"
    - For instance, if I send the message "APOD for 2024-01-09" while the bot is active, the bot will send the url to the astronomy picture of the day for January 9th 2024 into the groupchat.
    - Note that the APOD was launched in June 16th of 1995, so there are no available pictures on/before that date. Naturally, there are no pictures after the current date.
    