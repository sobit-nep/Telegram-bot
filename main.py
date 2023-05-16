import csv
from datetime import datetime, timedelta
from collections import defaultdict
import telebot
import pandas as pd

# Define a dictionary to store the unique sender counts for each group
group_counts = defaultdict(lambda: defaultdict(set))

# Define the group IDs you want to track
group_ids= {'-1001922973675','-1001900748432'}
group_ids_dict = {'-1001922973675':'Group AA',
                  '-1001900748432':'Group Bb'}

# Handle incoming messages to count unique senders
def handle_messages(message):
    group_id = message.chat.id
    if str(group_id) in group_ids:
        sender_id = message.from_user.id
        current_time = datetime.now()

        # Update the unique sender set for the group within the 10-minute timeframe
        previous_time = current_time - timedelta(minutes=10)
        group_counts[str(group_id)]['10m'].discard(sender_id)
        if current_time > previous_time:
            group_counts[str(group_id)]['10m'].add(sender_id)

        # Store the data in the CSV file
        store_data()

        # You can optionally print the user count for each group
        for group_id, timeframe_counts in group_counts.items():
            unique_senders = timeframe_counts['10m']
            group_name = group_ids_dict.get(group_id)
            print(f"Group Name: {group_name}, Unique Senders: {len(unique_senders)}")

# Define a function to store the data in the CSV file
def store_data():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    rows = []
    for group_id, timeframe_counts in group_counts.items():
        unique_senders = timeframe_counts['10m']
        group_name = group_ids_dict.get(group_id)
        row = [group_name, timestamp, len(unique_senders)]
        rows.append(row)

    # Create a pandas DataFrame
    df = pd.DataFrame(rows, columns=['Group name', 'Timestamp', 'Unique senders'])

    # Save DataFrame to Excel file
    df.to_excel('user_records.xlsx', index=False)

# Create an instance of the Telebot with your API token which looks like this: 01234567889:AASaRZpv9xtBVACLj-4vFK51Gs70AmQVyKo
bot = telebot.TeleBot('YOUR_API_TOKEN')

# Register the message handler function
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    handle_messages(message)

# Start the bot
bot.polling()
