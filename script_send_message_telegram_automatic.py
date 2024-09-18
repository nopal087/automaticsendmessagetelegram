from telethon import TelegramClient
import nest_asyncio
import asyncio

# Apply nest_asyncio to avoid asyncio loop issues
nest_asyncio.apply()

# Replace with your API IDs, API Hashes, and Phone Numbers
accounts = [
    {'api_id': '24079184', 'api_hash': '142e695f7431af05c582f8610329f1ca', 'session_name1': 'session4', 'phone_number': '+6285712666154'},
    {'api_id': '20122958', 'api_hash': '73685cb668c0b3485dab2939016d83a6', 'session_name1': 'session2', 'phone_number': '+6285921840555'},
    {'api_id': '20793497', 'api_hash': 'fa5dd599d1627c1a3ecd616ffe1e03ae', 'session_name1': 'session3', 'phone_number': '+6281225524603'},
    {'api_id': '24818691', 'api_hash': '9cfe2ef93ea7ab042a8a553ed954c145', 'session_name1': 'session5', 'phone_number': '+6281238134524'}
]

# List of messages to send
messages = [
    '/report_atm_kc 0245',
    '/report_crm_kc 0245'
]

# Target chat/channel
chat = '@jaguargesit_bot'  # Replace with your target channel ID or username

# Function to send messages using each Telegram account
async def send_message(client):
    await client.start()

    # Infinite loop to continuously send messages
    while True:
        for message in messages:
            await client.send_message(chat, message)

        # Wait for 1 minute before sending the messages again
        await asyncio.sleep(1200)

# Function to handle OTP login for each account
async def login_with_otp(account):
    phone_number = account['phone_number']

    # Create client instance
    client = TelegramClient(account['session_name1'], account['api_id'], account['api_hash'])

    # Send the OTP code
    await client.connect()
    await client.send_code_request(phone_number)

    # Ask the user for the OTP code
    otp_code = input(f"Masukkan kode OTP yang dikirim ke {phone_number}: ")

    # Sign in with the OTP code
    await client.sign_in(phone_number, otp_code)

    return client

# Main function to run multiple clients
async def main():
    # Login and create clients for all accounts
    clients = [await login_with_otp(account) for account in accounts]

    # Start sending messages for each client
    await asyncio.gather(*(send_message(client) for client in clients))

if __name__ == "__main__":
    asyncio.run(main())
