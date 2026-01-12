import requests
import json
from pyrogram import *
from pyrogram import Client, filters
from fansx import PY

__MODULE__ = "𝙲𝚁𝙴𝙰𝚃𝙴 𝙳𝙾𝙼𝙰𝙸𝙽"
__HELP__ = """
<blockquote><b>Bantuan Untuk Subdomain Creator</b>

Perintah:
<code>{0}subdocreate [domain] [subdomain] [IP]</code> → Menambahkan subdomain ke domain yang tersedia di Cloudflare.
<code>{0}listdomain </code> → Untuk melihat list domain.

🔍 Contoh:
<code>{0}subdocreate example.com test 192.168.1.1</code>

💡 Gunakan <code>{0}domainlist</code> untuk melihat daftar domain yang tersedia.</blockquote></b>
"""

# Konfigurasi Cloudflare dengan Token masing-masing domain
DOMAIN_LIST = {
    "digitalatelier.tech": {"zone": "1932711fb1d4d86b1f53b00d1b275f8a", "token": "auQMrkPsYbpFO29HwHMEVzNvkY_nLNlR3vPW6Y7Y"},
    "mydigital-store.me": {"zone": "11c1abb8f727bf4d7342f1cade2b3cd7", "token": "auQMrkPsYbpFO29HwHMEVzNvkY_nLNlR3vPW6Y7Y"},
    "pterodactyl-panel.web.id": {"zone": "d69feb7345d9e4dd5cfd7cce29e7d5b0", "token": "32zZwadzwc7qB4mzuDBJkk1xFyoQ2Grr27mAfJcB"},
    "storedigital.web.id": {"zone": "2ce8a2f880534806e2f463e3eec68d31", "token": "v5_unJTqruXV_x-5uj0dT5_Q4QAPThJbXzC2MmOQ"},
    "storeid.my.id": {"zone": "c651c828a01962eb3c530513c7ad7dcf", "token": "N-D6fN6la7jY0AnvbWn9FcU6ZHuDitmFXd-JF04g"},
    "store-panell.my.id": {"zone": "0189ecfadb9cf2c4a311c0a3ec8f0d5c", "token": "eVI-BXIXNEQtBqLpdvuitAR5nXC2bLj6jw365JPZ"},
    "xyro.web.id": {"zone": "46d0cd33a7966f0be5afdab04b63e695", "token": "CygwSHXRSfZnsi1qZmyB8s4qHC12jX_RR4mTpm62"},
    "xyroku.my.id": {"zone": "f6d1a73a272e6e770a232c39979d5139", "token": "0Mae_Rtx1ixGYenzFcNG9bbPd-rWjoRwqN2tvNzo"},
    "mafiapnel.my.id": {"zone": "34e28e0546feabb87c023f456ef033bf", "token": "bHNaEBwaVSdNklVFzPSkSegxOd9OtKzWtY7P9Zwt"},
    "gacorr.biz.id": {"zone": "cff22ce1965394f1992c8dba4c3db539", "token": "v9kYfj5g2lcacvBaJHA_HRgNqBi9UlsVy0cm_EhT"},
    "cafee.my.id": {"zone": "0d7044fc3e0d66189724952fa3b850ce", "token": "wAOEzAfvb-L3vKYE2Xg8svJpHfNS_u2noWSReSzJ"},
    "pterodaytl.my.id": {"zone": "828ef14600aaaa0b1ea881dd0e7972b2", "token": "75HrVBzSVObD611RkuNS1ZKsL5A_b8kuiCs26-f9"},
    "jhonaley.net": {"zone": "e67db64db8ec671f105c77ee521daa37", "token": "-eNyMkEo9Wy1_n92YhDZ3QBDlVihX-1VGCUzfrj8"},
    "jhonaley.web.id": {"zone": "dd00b76d94af1e8d5f37f4253f77861f", "token": "MHXAKlSaWbFcCLDqo7t-A-KFx1N89vUOwjvSgVTt"},
    "jhonaleyhost.web.id": {"zone": "d2d72f4164b3e18c455dd2b0660d85a1", "token": "J_Nb9wERFSu-Bqfvu6zOY8js9V4rKKcszZtsZJxm"},
    "naell.cloud": {"zone": "1b662cae2a8214a8468c97fb552070d0", "token": "EX4ezkgaSvD3JeXeKoDQzfmqI_Mh0yUek7WmDO0u"},
    "naell.my.id": {"zone": "090a81422da7b258cdf3ef02de1e4ca3", "token": "HTLdfWAdDalNoz5x3-Pe4MLWGVgxKRq6ZMVz4vl0"},
    "privateeserverr.my.id": {"zone": "2b47743c5a3afecde36ffa0f52073270", "token": "2ltJMUmL2QZ-H3IQ0NGM8n84zxoJlU1D8Wwj26AB"},
    "publicserverr.my.id": {"zone": "b23d82b98aa932317c93571a3846240a", "token": "2ltJMUmL2QZ-H3IQ0NGM8n84zxoJlU1D8Wwj26AB"},
    "panelku-ptero.my.id": {"zone": "ea719beeec3cfe39b58f0195f848498f", "token": "Gb8j0xFasrWB1k80b4BFrIL_f2IgAQ5n66CamFbP"},
    "sainsproject.biz.id": {"zone": "8211830a7911e9028f38018243ea360d", "token": "XLllrPcIOIC-S4yQP2iaJ9GELQVrL5agcAtEyGXN"},
    "barmodsdomain.my.id": {"zone": "05478e906fa1556f81ae0eaf86816060", "token": "nkIplLsfGW-FSUYEpbSt3_I2-a9JIWZIvGO5W6xN"},
    "rikionline.shop": {"zone": "082ec80d7367d6d4f7c52600034ac635", "token": "r3XUyNYtxNQYwZtGUIAChRqe0uTzwV4eVO7JpJ_l"},
    "lightsecret.my.id": {"zone": "e34c31e55b96bcc90c925f21dbe3f5ac", "token": "yDtnVxibxU8L0nVOM1SzOzkT3zhbjsLHgQ"},
    "lightsecretaja.web.id": {"zone": "68ca80984086afc9bf4909c81ebd1f85", "token": "Cn5WHHw81TGRwuFahaYsDllba7xAaz1RpMdxykE5"},
    "lightsecret.xyz": {"zone": "169d4991c822f469f38d8eb485250840", "token": "nHmGvbgVzLdCrY1kUe9HGrJpkUsdMmsSpMkmwQTv"},
    "bot-wa-lightsecret.my.id": {"zone": "52233f7bec570d42092bc887ff2e9ea1", "token": "CG984ovHlLM6uG5arMaGR65xNBQL9k4yDwvNxdGB"}
}

# Fungsi untuk menambahkan subdomain ke Cloudflare (Sekarang menerima token sebagai parameter)
def create_subdomain(zone_id, api_token, subdomain, target_ip):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }

    data = {
        "type": "A",
        "name": subdomain,
        "content": target_ip,
        "ttl": 1,
        "proxied": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

@PY.UBOT("subdocreate")
@PY.TOP_CMD
async def subdomain_create(client, message):
    args = message.text.split(maxsplit=3)
    if len(args) < 4:
        await message.reply_text("❌ Silakan masukkan format yang benar: `.subdocreate [domain] [subdomain] [IP]`")
        return

    domain = args[1].strip()
    subdomain = args[2].strip()
    target_ip = args[3].strip()

    if domain not in DOMAIN_LIST:
        await message.reply_text(f"❌ Domain `{domain}` tidak ditemukan dalam daftar. Gunakan `.domainlist` untuk melihat daftar domain yang tersedia.")
        return

    # Mengambil Zone ID dan Token dari DOMAIN_LIST
    zone_id = DOMAIN_LIST[domain]["zone"]
    api_token = DOMAIN_LIST[domain]["token"]
    full_subdomain = f"{subdomain}.{domain}"

    await message.reply_text(f"🔍 **Menambahkan subdomain:** `{full_subdomain}` ➝ `{target_ip}`")

    # Mengirim data ke fungsi create_subdomain
    result = create_subdomain(zone_id, api_token, full_subdomain, target_ip)

    if result.get("success"):
        await message.reply_text(f"✅ **Subdomain Berhasil Ditambahkan!**\n🌐 `{full_subdomain} → {target_ip}`")
    else:
        error_msg = result.get("errors", [{"message": "Unknown Error"}])[0]["message"]
        await message.reply_text(f"❌ **Gagal Menambahkan Subdomain**\n⚠️ Error: `{error_msg}`")

@PY.UBOT("domainlist")
@PY.TOP_CMD
async def list_domains(client, message):
    domain_list_text = "📜 **Daftar Domain yang Tersedia:**\n"
    for domain in DOMAIN_LIST.keys():
        domain_list_text += f"✅ `{domain}`\n"
    
    await message.reply_text(domain_list_text)
