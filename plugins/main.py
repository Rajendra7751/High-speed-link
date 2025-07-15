from pyrogram import Client, filters
from pyrogram.types import Message
from utils.db import insert_file
from utils.force_join import force_join_handler
import os

BIN_CHANNEL = int(os.getenv("BIN_CHANNEL"))
FQDN = os.getenv("FQDN")

@Client.on_message(filters.private & filters.document | filters.video | filters.audio)
async def handle_file(c: Client, m: Message):
    if await force_join_handler(c, m):
        return

    sent = await m.forward(BIN_CHANNEL)
    await insert_file(sent)

    link = f"{FQDN}/download/{sent.id}"
    await m.reply_text(
        f"✅ File Stored Successfully!\n\n🔗 **Link:** {link}",
        disable_web_page_preview=True
    )
