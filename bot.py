# https://huzunluartemis.github.io/ChatSizeBot/

import logging
import time
from config import Config
from pyrogram import idle
import pyrogram
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)
botStartTime = time.time()

if __name__ == '__main__':
    # init pyrogram client
    plugins = dict(root = 'plugins')
    app = pyrogram.Client("ChatSizeBot", bot_token = Config.BOT_TOKEN,
        api_id = Config.APP_ID, api_hash = Config.API_HASH, plugins = plugins)
    app.start()
    LOGGER.info(app.get_me())
    LOGGER.info(msg="Bot Started.")
    try: app.send_message(Config.OWNER_ID, "Bot Started.")
    except: pass
    idle()
    LOGGER.info(msg="Bot Stopped.")
    try: app.send_message(Config.OWNER_ID, "Bot Stopped.")
    except: pass
