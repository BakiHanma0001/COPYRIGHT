import asyncio
import importlib
from pyrogram import idle
from SHIELD3 import SHIELD3
from SHIELD3.modules import ALL_MODULES

LOGGER_ID = -1002237562181

loop = asyncio.get_event_loop()

async def roy_bot():
    for all_module in ALL_MODULES:
        importlib.import_module("SHIELD3.modules." + all_module)
    print("♥︎ B𝗈𝗍 Started Successfully.")
    await idle()
    print("♥︎ Dᴏɴ'ᴛ ᴇᴅɪᴛ ʙᴀʙʏ, ᴏᴛʜᴇʀᴡɪsᴇ ʏᴏᴜ ɢᴇᴛ ᴀɴ ᴇʀʀᴏʀ. @Satan_Network")
    await SHIELD3.send_message(LOGGER_ID, "**✦ ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ.\n\n✦ ᴊᴏɪɴ - @Satan_Fucker**")

if __name__ == "__main__":
    loop.run_until_complete(roy_bot())




