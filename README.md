# XRPL-TG-Buy-Bot

This repository contains three versions of a Telegram bot that monitors the XRP Ledger (XRPL) and posts details of token purchases to a specified Telegram channel. The bots are designed to track and notify based on different criteria, such as token quantity or XRP value spent.

## Table of Contents

- [Bot Versions](#bot-versions)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)

## Bot Versions
1. **Bot.py**: This version posts all purchases of a specified XRPL token to the Telegram channel without any filters.
2. **Minimum-Token-Amount-Bot.py**: This version filters and posts purchases based on the quantity of tokens purchased.  
   *Only purchases greater than or equal to the specified token quantity are posted.*
4. **Minimum-XRP-Value-Bot.py**: This version filters and posts purchases based on the amount of XRP spent.  
   *Only purchases where the buyer spends more than or equal to the specified XRP value are posted.*

## Installation

To run these bots, you’ll need to have Python installed on your machine and install the necessary dependencies.

### Clone the Repository
```bash
git clone https://github.com/joshuahamsa/xrpl-tg-buy-bot.git
cd xrpl-token-purchase-bot
```
### Install Dependencies

Install the required Python packages by running:
```bash
pip install -r requirements.txt
```
The requirements.txt file should include the following packages:
`xrpl-py`  
`python-telegram-bot`  
### Set Up Your Telegram Bot

1. Message [BotFather](https://t.me/botfather) on Telegram and create a new bot.
2. Save the API Token provided by BotFather after the bot creation.

## Configuration

Before running any of the bot versions, make sure to update the following variables in the Python scripts:  
`bot_token:`  
This is your Telegram Bot API token. You can get one by messaging the [BotFather](https://t.me/botfather) app on Telegram, which will provide tons of resources for Telegram bots if you're interested in learning more.  
  
`chat_id:`  
The Telegram chat or channel ID where the bot will post updates.  
  
`ISSUER_ADDRESS:`  
The XRPL address that issued the token.  
  
`TOKEN_CURRENCY:`  
This is the token’s currency code. If the name of the token is longer than 3 characters, you must [convert](https://www.rapidtables.com/convert/number/ascii-to-hex.html) the ASCII letters into HEX code.  
*Note: If using a converter that has an Output Delimiter option, be sure to set this to **None**.*


## Usage

### Running Bot.py

This version posts all purchases of the specified token to the Telegram channel without any filters.
```bash
python Bot.py
```
### Running Minimum-Token-Amount-Bot.py

This version filters purchases based on token quantity. Upon starting, it will prompt you to enter the minimum token amount. Only purchases greater than or equal to this amount will be posted to Telegram.
```bash
python Minimum-Token-Amount-Bot.py
```
### Running Minimum-XRP-Value-Bot.py

This version filters purchases based on the amount of XRP spent on the purchase. Upon starting, it will prompt you to enter the minimum XRP value. Only purchases where the buyer spends this amount or more will be posted to Telegram.
```bash
python Minimum-XRP-Value-Bot.py
```
