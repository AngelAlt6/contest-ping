import os
import requests
import time
from datetime import datetime

# Get the Discord Webhook URL from environment variable
WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')

# Function to send a message to Discord
def send_message(content):
    if WEBHOOK_URL is None:
        print("Discord Webhook URL is not set")
        return
    data = {"content": content}
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code != 204:
        print(f"Failed to send message: {response.status_code}")

# Main loop
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    
    # Send message at xx:00, xx:15, xx:45
    if current_time.endswith(':59') or current_time.endswith(':14') or current_time.endswith(':44'):
        send_message("Ping: <@&1289531502350041190> team contest is happening soon!")
        break
    # Send message at xx:30
    if current_time.endswith(':29'):
        send_message("Ping: <@&1289531604666155051> battle royale contest is happening soon!")
        break
    # Wait for the next minute
    time.sleep(20)
