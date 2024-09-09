from telethon import TelegramClient
import nest_asyncio
import asyncio

api_id = '24079184'
api_hash = '142e695f7431af05c582f8610329f1ca'

# Initialize the Telegram Client
client = TelegramClient('new_session2_name', api_id, api_hash)

messages = [
    '/report_atm_kc 0245',
    '/report_crm_kc 0245'
]

async def send_message():
    await client.start()
    chat = '@jaguargesit_bot'

    while True:
        for message in messages:
            await client.send_message(chat, message)
        await asyncio.sleep(600)

if __name__ == "__main__":
    nest_asyncio.apply()
    asyncio.run(send_message())
