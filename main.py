import os
import time

from tools import search_papers,extract_info
from system_prompt import system_instruction


from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv() 

client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat1 = client.chats.create(
    model='gemini-2.0-flash-lite',
    config=types.GenerateContentConfig(
          system_instruction=system_instruction,
          tools=[search_papers,extract_info]
        )
    )

chat2 = client.chats.create(
    model='gemini-2.0-flash-lite',
    config=types.GenerateContentConfig(
          system_instruction=system_instruction,
          tools=[search_papers,extract_info]
        )
    )

message = "Lets discuss about something"
start_time = time.time()
timeout = 180  # 3 minutes in seconds

while True:
    # Check if 3 minutes have elapsed
    if time.time() - start_time >= timeout:
        with open('chat_log.txt', 'a') as f:
            f.write("Chat session ended after 3 minutes\n")
        break
    
    message = chat1.send_message(message=message).text
    with open('chat_log.txt', 'a') as f:
        f.write(f"===========================     model1 response     =========================== \n\n {message}\n")
    # Check if any goodbye message is in response1
    goodbye_messages = ['good bye', 'Good bye!', 'Good bye.']
    if any(msg in message for msg in goodbye_messages):
        break
    
    message = chat2.send_message(message=message).text
    with open('chat_log.txt', 'a') as f:
        f.write(f"===========================     model2 response     =========================== \n\n {message}\n")
    
    # Check if any goodbye message is in response2    
    if any(msg in message for msg in goodbye_messages):
        break
