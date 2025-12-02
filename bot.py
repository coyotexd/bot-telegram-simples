## importar bibliotecas
from telethon import TelegramClient, events

## valores api
api_id = "api id"
api_hash = "api hash"
bot_token = "token bot"

client = TelegramClient('bot',api_id,api_hash)

@client.on(events.NewMessage(pattern='/start'))
async def handler(event):
	await event.respond('olá eu sou um bot de teste!')
	
async def main():
	await client.start(bot_token=bot_token)
	print("bot está sendo executado!!")
	await client.run_until_disconnected()
	
	
client.loop.run_until_complete(main())

##by coyote##