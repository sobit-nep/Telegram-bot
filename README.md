# Telegram-bot-using-python
This Python script is a Telegram bot that tracks and stores the number of unique senders in specified Telegram groups over a certain timeframe. It uses the Telebot library to interact with the Telegram Bot API and utilizes the Pandas library to store the data in an Excel file.

# Telegram Group Unique Senders Tracker

This Python script is a Telegram bot that tracks and stores the number of unique senders in specified Telegram groups over a 10-minute timeframe.

## Prerequisites
- Python 3.6 or above
- Required Python packages: `telebot`, `pandas`

## Installation

1. Clone the repository:
   ```shell
   git clone https://github.com/sobit-nep/Telegram-bot.git
   
2. Install the required packages:
   ```shell
   pip install -r requirements.txt
   
3. Obtain a Telegram Bot API token:

    Create a new bot on Telegram and obtain the API token. You can follow the instructions here: https://core.telegram.org/bots#6-botfather

4. Update the API token in the script:

    Open main.py file and replace 'YOUR_TELEGRAM_BOT_API_TOKEN' with your actual Telegram Bot API token.

5. Define the group IDs to track:

    Modify the group_ids variable in main.py to include the desired group IDs you want to track.

## Usage
Run the script using the following command:
 ```shell
 python main.py
