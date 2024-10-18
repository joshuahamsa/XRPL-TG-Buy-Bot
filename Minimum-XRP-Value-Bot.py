import xrpl
import asyncio
from telegram import Bot

# Telegram Bot API setup
bot_token = 'YOUR_TELEGRAM_BOT_API_TOKEN'
chat_id = 'YOUR_TELEGRAM_CHAT_ID'  # Group or channel chat ID
bot = Bot(token=bot_token)

# XRPL setup
client = xrpl.clients.JsonRpcClient('https://s1.ripple.com:51234/')
ISSUER_ADDRESS = "rExampleIssuer"  # The token issuer address
TOKEN_CURRENCY = "EXAMPLETOKEN"  # Token currency code (hex encoded if not ASCII)

# User-configurable option for filtering by XRP purchase amount
MIN_XRP_AMOUNT = float(input("Enter the minimum XRP amount to post (e.g., 50): "))

async def monitor_xrpl():
    async with client:
        while True:
            request = {
                "command": "subscribe",
                "streams": ["transactions"]
            }
            response = await client.request(xrpl.models.requests.Request(request))
            tx = response.result['transactions']
            
            for txn in tx:
                if txn['TransactionType'] == 'OfferCreate' and txn['TakerGets']['currency'] == TOKEN_CURRENCY:
                    # Extract relevant info about the purchase
                    buyer = txn['Account']
                    token_amount = txn['TakerGets']['value']
                    xrp_spent = float(txn['TakerPays']['value'])  # XRP paid for the tokens
                    
                    # Filter by minimum XRP amount
                    if xrp_spent >= MIN_XRP_AMOUNT:
                        # Prepare the message to send
                        message = (f"Purchase Detected!\nBuyer: {buyer}\n"
                                   f"Amount: {token_amount} {TOKEN_CURRENCY}\n"
                                   f"Price: {xrp_spent} XRP")
                        
                        # Send to Telegram
                        bot.send_message(chat_id=chat_id, text=message)
                    
            await asyncio.sleep(5)  # Poll every 5 seconds

if __name__ == "__main__":
    asyncio.run(monitor_xrpl())
