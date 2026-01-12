import requests
import os
import urllib.parse
import random
from bs4 import BeautifulSoup
from fansx import *

__MODULE__ = "xɴxx"
__HELP__ = """
<b>♛ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ xɴxx ♛</b>
<blockquote><b>
Perintah :
<code>{0}xnxx</code> kata pencarian
Mendownload Video Yang Di Inginkan.</b></blockquote>
"""

@PY.UBOT("xnxx")
async def random_bokep(client, message):
    try:
        query = message.text.split()[1:]
        if not query:
            await message.reply(
                "<emoji id=5215204871422093648>❌</emoji> Gunakan format: `.xnxx [kata kunci]`\n\nContoh: `.xnxx japanese teacher` atau `.xnxx bokep`"
            )
            return

        search_query = " ".join(query)
        status_msg = await message.reply(f"<emoji id=4967797089971995307>🔍</emoji> Mencari bokep untuk: **{search_query}**...")

        # 🔍 Cari di situs XNXX
        encoded_query = urllib.parse.quote_plus(search_query)
        search_url = f"https://www.xnxx.com/search/{encoded_query}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; Mobile; rv:110.0) Gecko/110.0 Firefox/110.0"
        }

        res = requests.get(search_url, headers=headers, timeout=20)
        res.raise_for_status()

        soup = BeautifulSoup(res.text, "html.parser")
        results = soup.select(".thumb-block .thumb-under a")

        if not results:
            await status_msg.edit(
                f"<emoji id=5215204871422093648>❌</emoji> Tidak ditemukan hasil untuk: **{search_query}**"
            )
            return

        # 🎲 Ambil video random dari hasil pencarian
        chosen = random.choice(results)
        first_link = "https://www.xnxx.com" + chosen.get("href")

        # 🔎 Ambil halaman video
        video_page = requests.get(first_link, headers=headers, timeout=20)
        video_soup = BeautifulSoup(video_page.text, "html.parser")

        title = video_soup.find("title").text.strip()

        # 🎥 Cari URL video asli (high/low)
        video_url = None
        meta_tag = video_soup.find("meta", {"property": "og:video"})
        if meta_tag and meta_tag.get("content"):
            video_url = meta_tag.get("content")
        else:
            for script in video_soup.find_all("script"):
                if script.string and "html5player.setVideoUrlHigh" in script.string:
                    start = script.string.find("setVideoUrlHigh('") + len("setVideoUrlHigh('")
                    end = script.string.find("')", start)
                    video_url = script.string[start:end]
                    break

        if not video_url:
            await status_msg.edit("<emoji id=5215204871422093648>❌</emoji> Gagal mendapatkan URL video dari halaman.")
            return

        # 🕒 Ambil durasi kalau ada
        duration = "N/A"
        meta_duration = video_soup.find("meta", {"property": "video:duration"})
        if meta_duration and meta_duration.get("content"):
            duration = meta_duration.get("content") + " detik"

        capt = (
            f"卍 **Hasil Pencarian: {search_query}**\n\n"
            f"  ◦ **Title** : {title}\n"
            f"  ◦ **Duration** : {duration}\n"
            f"  ◦ **[🔗 Link Asli]({first_link})**\n"
        )

        await status_msg.edit(f"📥 Mengunduh video dari: **{title}**...")

        video_path = "video.mp4"
        with requests.get(video_url, stream=True, timeout=60) as vid_res:
            vid_res.raise_for_status()
            with open(video_path, "wb") as f:
                for chunk in vid_res.iter_content(chunk_size=8192):
                    f.write(chunk)

        await status_msg.edit("📤 Mengunggah video ke Telegram...")
        await client.send_video(message.chat.id, video_path, caption=capt)
        os.remove(video_path)
        await status_msg.delete()

    except requests.exceptions.RequestException as e:
        await message.reply(
            f"<emoji id=5215204871422093648>❌</emoji> Kesalahan koneksi / situs: {str(e)}"
        )
    except Exception as e:
        await message.reply(
            f"<emoji id=5215204871422093648>❌</emoji> Terjadi Kesalahan: {str(e)}"
        )
