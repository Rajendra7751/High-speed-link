from aiohttp import web
from utils.db import get_file
from pyrogram import Client
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("WebServer", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def handle_download(request):
    msg_id = request.match_info.get("msg_id")
    file_data = get_file(msg_id)
    if not file_data:
        return web.Response(text="404: File Not Found", status=404)
    message = await app.get_messages(file_data["chat_id"], file_data["msg_id"])
    file_path = await app.download_media(message)
    return web.FileResponse(path=file_path)

web_app = web.Application()
web_app.router.add_get("/download/{msg_id}", handle_download)
