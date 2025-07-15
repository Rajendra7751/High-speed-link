from pyrogram.errors import UserNotParticipant
import os

FORCE_JOIN = os.getenv("FORCE_JOIN")

async def force_join_handler(c, m):
    if not FORCE_JOIN:
        return False
    try:
        user = await c.get_chat_member(FORCE_JOIN, m.from_user.id)
        if user.status in ("kicked", "left"):
            raise UserNotParticipant
    except UserNotParticipant:
        await m.reply_text(
            f"🔒 To use this bot, please join @{FORCE_JOIN.strip('@')} first."
        )
        return True
    return False
