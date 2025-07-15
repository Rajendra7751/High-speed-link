import logging
from pyrogram import Client, filters
from dotenv import load_dotenv
import os
from utils.force_join import force_join_handler
from aiohttp import web
from web.server import web_app

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT", 8080))

app = Client("FileToLink", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start") & filters.private)
async def start_cmd(c, m):
    if await force_join_handler(c, m):
        return
    name = m.from_user.first_name
    await m.reply_text(
        f"Hey {name}, 👋\n\n"
        f"Welcome to the Best File-to-Link Bot!\n"
        f"This bot is proudly managed by @bolly_king.\n\n"
        f"📤 Send me any file and I'll give you a permanent link to download or stream."
    )

@app.on_message(filters.command("start") & filters.private)
async def launch_web_server(c, m):
    runner = web.AppRunner(web_app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()
