import config
import time
import logging
from flask import Flask
from pyrogram import Client, idle
from pyromod import listen  # type: ignore
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from threading import Thread

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Flask app initialization
flask_app = Flask(__name__)

# Pyrogram bot initialization
StartTime = time.time()
bot = Client(
    "Anonymous",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="StringGenBot"),
)


# Define a simple route for the Flask app
@flask_app.route('/')
def home():
    return "Flask app is running with Pyrogram bot in the background!"


# Function to run the pyrogram bot in a separate thread
def run_bot():
    try:
        print("𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐒𝐭𝐫𝐢𝐧𝐠 𝐁𝐨𝐭...")
        bot.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    uname = bot.get_me().username
    print(f"@{uname} 𝐒𝐓𝐀𝐑𝐓𝐄𝐃 𝐒𝐔𝐂𝐄𝐒𝐒𝐅𝐔𝐋𝐋𝐘. 𝐌𝐀𝐃𝐄 𝐁𝐘 @𝗧𝗛𝗘_𝗩𝗜𝗣_𝗕𝗢𝗬 🤗")
    idle()
    bot.stop()
    print("𝗕𝗢𝗧 𝗦𝗧𝗢𝗣𝗣𝗘𝗗 𝗕𝗬 𝗕𝗬 !")


# Run the pyrogram bot in a separate thread
bot_thread = Thread(target=run_bot)
bot_thread.daemon = True  # Allow the bot thread to exit when the main thread ends
bot_thread.start()


# Flask app main entry
if __name__ == "__main__":
    flask_app.run(debug=True, host="0.0.0.0", port=8000)
