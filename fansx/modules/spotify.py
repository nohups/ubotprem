from pyrogram import Client, filters
import requests, os
from fansx import *

__MODULE__ = "sᴘᴏᴛɪғʏ"
__HELP__ = """
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴘᴏᴛɪғʏ ⦫</b>
<blockquote><b>
⎆ Perintah :
ᚗ <code>{0}spotify</code> judul lagu
⊶ Mendownload dan mengirimkan lagu otomatis.</b></blockquote>
"""

API_SEARCH = "https://saavn.dev/api/search/songs?query={}"
API_SONG = "https://saavn.dev/api/songs?id={}"

@PY.UBOT("spotify")
async def spotify_search(client, message):
    query = " ".join(message.command[1:])
    if not query:
        await message.reply_text("Gunakan format: <code>/spotify judul lagu</code>")
        return

    proses = await message.reply_text("🔎 Sedang mencari lagu...")

    try:
        res = requests.get(API_SEARCH.format(query)).json()
        songs = res.get("data", [])
        if not songs:
            await proses.edit_text("❌ Tidak ditemukan hasil untuk pencarian tersebut.")
            return

        # ambil lagu pertama langsung
        song_id = songs[0]["id"]
        song_res = requests.get(API_SONG.format(song_id)).json()
        song = song_res["data"][0]

        title = song["name"]
        artist = song["primaryArtists"]
        album = song["album"]["name"]
        duration = song["duration"]
        dl_link = song["downloadUrl"][-1]["link"]

        await proses.edit_text(f"🎶 Mengunduh: <b>{title}</b> - {artist}")

        filename = f"{title}.mp3"
        r = requests.get(dl_link)
        with open(filename, "wb") as f:
            f.write(r.content)

        caption = (f"🎵 <b>{title}</b>\n"
                   f"👤 {artist}\n"
                   f"💿 {album}\n"
                   f"⏳ {duration} detik")

        await client.send_audio(
            chat_id=message.chat.id,
            audio=filename,
            title=title,
            performer=artist,
            caption=caption
        )

        os.remove(filename)
        await proses.delete()

    except Exception as e:
        await proses.edit_text(f"❌ Error saat mencari/mengunduh lagu:\n<code>{e}</code>")
