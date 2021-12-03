from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hallo {}

Selamat datang di {}

Jika Anda tidak mempercayai bot ini,
1) berhenti membaca pesan ini
2) hapus obrolan ini

Masih membaca?
Anda dapat menggunakan saya untuk menghasilkan sesi string pyrogram dan telethon. Gunakan tombol di bawah ini untuk mempelajari lebih lanjut!

By @Rhitosakai
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")],
        [InlineKeyboardButton(text="🏠 Kembali keawal 🏠", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")],
        [
            InlineKeyboardButton("Cara Menggunakan Saya ❔", callback_data="help"),
            InlineKeyboardButton("🎪 Tentang Saya 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("🎶 Bot Music 🎶", url="t.me/inimusicxbot")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - Tentang Saya
/help - Cara Menggunakan
/start - Memulai Bot
/generate - Memulai Generator Session
/cancel - Membatalkan Proses
/restart - Membatalkan
"""

    # About Message
    ABOUT = """
**Tentang Saya** 

Bot telegram untuk menghasilkan string session pyrogram dan telethon By @RhitoSakai

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @RhitoSakai
    """
