import discord
from chatgpt_code.openai import chatgpt_response

discord_token = 'MTEyNjkwMjI3NzkwNzY5MzU3OA.GC1hv-.sHhiscR3II4YP_0t8eWUYVFBuUS3Anzjdcg9MU'

class MyClient(discord.Client):

    #chathistory = []

    async def on_ready(self):
        print("logged in as ", self.user)
    
    async def on_message(self, message):
        print(message.content)
        if message.author == self.user:
            return
        command, user_message=None,None
        
        for text in ['/yip']:  
            if message.content.startswith(text):
                command = message.content.split(' ')[0]
                user_message = message.content.replace(text, '')
                print(command, user_message)
        
        if command == '/yip': 
            bot_response = chatgpt_response(prompt = user_message)
            await message.channel.send(f"Answer: {bot_response}")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents = intents)
