from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from fansx import OWNER_ID, bot, ubot, get_expired_date


class MSG:     
    def EXP_MSG_UBOT(X):
        return f"""
<blockquote><b>❏ Pemberitahuan</b>
<b>├ Akun : </b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>├ ID : </b> <code>{X.me.id}</code>
<b>╰ Masa aktif telah habis</b></blockquote>
"""

    def START(message):
        return f"""
<blockquote><b>👋 Olaaa <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>!

> 𝗙𝗜𝗧𝗨𝗥 𝗙𝗥𝗘𝗘
/freealdi

ALDI USERBOT
<b> 📚💎@{bot.me.username} Adalah bot yang dapat membuat userbot dengan efisien dan cepat. Bot ini dikembangkan oleh <a href=tg://openmessage?user_id={OWNER_ID}>@ajigz</a> jika ada kendala atau kesalahan pada bot bisa dm owner bot nya</b></blockquote>
"""

    def TEXT_PAYMENT(harga, total, bulan):
        return f"""
<blockquote><b>💬 sɪʟᴀʜᴋᴀɴ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ</b>

<b>🎟️ ʜᴀʀɢᴀ ᴘᴇʀʙᴜʟᴀɴ: {harga}.000</b>

<b>💳 ᴍᴏᴛᴏᴅᴇ ᴘᴇᴍʙᴀʏᴀʀᴀɴ:</b>
 <b>├ Qʀɪꜱ ᴀʟʟ ᴘᴀʏᴍᴇɴᴛ </b>
<b>🔖 ᴛᴏᴛᴀʟ ʜᴀʀɢᴀ: ʀᴘ {total}.000</b>
<b>🗓️ ᴛᴏᴛᴀʟ ʙᴜʟᴀɴ: {bulan}</b> 

OWNER BOT : <a href=tg://openmessage?user_id={OWNER_ID}>@ajigz</a> 

<b>🛍 ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴋᴏɴꜰɪʀᴍᴀsɪ ᴜɴᴛᴜᴋ ᴋɪʀɪᴍ ʙᴜᴋᴛɪ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴀɴᴅᴀ</b></blockquote>
"""

    async def UBOT(count):
        return f"""
<blockquote><b>╭〢Aldi-Userbot</b> <code>{int(count) + 1}/{len(ubot._ubot)}</code>
<b>├〢 ᴀᴄᴄᴏᴜɴᴛ </b> <a href=tg://user?id={ubot._ubot[int(count)].me.id}>{ubot._ubot[int(count)].me.first_name} {ubot._ubot[int(count)].me.last_name or ''}</a> 
<b>╰〢ᴜsᴇʀ ɪᴅ </b> <code>{ubot._ubot[int(count)].me.id}</code></blockquote>
"""

    def POLICY():
        return """ <blockquote><b>ᴊɪᴋᴀ ᴀᴅᴀ ᴋᴇɴᴅᴀʟᴀ sɪʟᴀʜᴋᴀɴ ʜᴜʙᴜɴɢɪ  <a href=tg://openmessage?user_id={OWNER_ID}>@ajigz</a></b></blockquote>
"""
