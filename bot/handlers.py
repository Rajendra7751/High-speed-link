import logging
from pyrogram import Client, __version__
from info import API_ID, API_HASH, BOT_TOKEN, PORT, temp
from aiohttp import web
from plugins import web_server

class Bot(Client):

    def __init__(self):
        super().__init__(
            name="FileToLinkBot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=30,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
        await super().start()
        temp.BOT = self
        print("✅ Bot started. Now launching web server...")

        # ✅ Start aiohttp web server on Render-required port
        runner = web.AppRunner(await web_server())
        await runner.setup()
        site = web.TCPSite(runner, "0.0.0.0", PORT)
        await site.start()
        print(f"✅ Web server is running on http://0.0.0.0:{PORT}")

    async def stop(self, *args):
        await super().stop()
        print("🛑 Bot stopped.")

app = Bot()
