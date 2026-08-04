from pyrogram import Client, filters
from flask import Flask
import threading
import os

# ===== TELEGRAM CREDENTIALS =====
api_id = 36786764
api_hash = "8b4eac106e76e0e94b92a7da8eb9a491"
bot_token = "8967301761:AAFFdQaKsbSb_V_Z3NSHO2gLYPI4bhFuGBJA"

TARGET_CHATS = [
    -1003959234986,
    -1004479099838,
    -1003823745210,
    -1003681289888,
    -1003975750767,
    -1002306956966,
    -1004307504599,
    -1003157773225,
    -1003523693073,
    -1004470037524,
    -1003975928544,
    -1002458549043,
    -1002457215123,
    -1004345853199,
    -1004379369225,
    -1004307278991,
    -1004490657670
]

last_message = {}

bot = Client(
    "auto_delete_bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

@bot.on_message(filters.chat(TARGET_CHATS))
async def auto_delete(client, message):
    chat_id = message.chat.id

    if chat_id in last_message:
        try:
            await client.delete_messages(chat_id, last_message[chat_id])
        except:
            pass

    last_message[chat_id] = message.id


# ===== FLASK SERVER (FOR RENDER) =====
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running ✅"

def run_web():
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )

def run_bot():
    bot.run()


if __name__ == "__main__":
    threading.Thread(target=run_web).start()
    run_bot()
