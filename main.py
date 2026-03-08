from pyrogram import Client, filters
from flask import Flask
import threading
import os

# ---------------- Flask server (keeps Render awake) ----------------
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Auto Delete Bot is running ✅"

def run_flask():
    flask_app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )

# ---------------- Telegram Bot Credentials ----------------
api_id = 29842444
api_hash = "0c2c4ac4fa5ddf626edaaf302abce6df"
bot_token = "8273089291:AAFEVx58Ivcu5usr7Wozgw3VvDXt8ILp4QA"

# ---------------- Your 8 Channels ----------------
TARGET_CHATS = [
    -1003157773225,
    -1003813087595,
    -1003681289888,
    -1002457215123,
    -1003477857630,
    -1002583103466,
    -1002738151866,
    -1002892550508,
    -1002458549043,
    -1002306956966,
    -1003574367351
]

# ---------------- Store last message per chat ----------------
last_message = {}

bot = Client(
    "auto_delete_bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

@bot.on_message(filters.chat(TARGET_CHATS))
async def auto_delete_previous(client, message):
    chat_id = message.chat.id

    if chat_id in last_message:
        try:
            await client.delete_messages(chat_id, last_message[chat_id])
        except:
            pass

    last_message[chat_id] = message.id

# ---------------- Run Flask + Bot together ----------------
if __name__ == "__main__":
    # Run Flask in a separate thread
    threading.Thread(target=run_flask).start()
    # Run the Telegram bot
    bot.run()
