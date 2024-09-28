import requests
import time
from datetime import datetime

# Discord Webhook URL
WEBHOOK_URL = 'YOUR_DISCORD_WEBHOOK_URL'

# Function to send message to Discord
def send_message(content):
    data = {"content": content}
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code != 204:
        print(f"Failed to send message: {response.status_code}")

# Main loop
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    
    # Send message at xx:00, xx:15, xx:45
    if current_time.endswith(':00') or current_time.endswith(':15') or current_time.endswith(':45'):
        send_message("Ping: Team Contest is happening!")
    
    # Send message at xx:30
    if current_time.endswith(':30'):
        send_message("Ping: Battle Royale Contest is happening!")
    
    # Wait for the next minute
    time.sleep(60)
