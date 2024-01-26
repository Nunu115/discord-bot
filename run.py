from discord_code.discord_api import client, discord_token
from chatgpt_code.openai import chatgpt_response

if __name__ == '__main__':
    bot_response = chatgpt_response(prompt="keep responses to under 2000 characters.")
    print(bot_response)
    client.run(discord_token)
