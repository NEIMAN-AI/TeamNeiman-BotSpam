from telethon import __version__, events, Button

from config import N1, N2, N3, N4, N5, N6, N7, N8, N9, N10


START_BUTTON = [
    [
        Button.inline("•🛠️ ᴄᴏᴍᴍᴀɴᴅs🛠️ •", data="help_back")
    ],
    [
        Button.url("• ⚡ᴄʜᴀɴɴᴇʟ⚡ •", "https://t.me/TeamNeiman"),
        Button.url("• 🥀sᴜᴘᴘᴏʀᴛ🥀 •", "https://t.me/Neiman_X_Support")
    ],
    [
        Button.url("•💸 ʀᴇᴘᴏ 💸•", "https://github.com/NEIMAN-AI/TeamNeiman-BotSpam")
    ],
    [
        Button.url("✨ᴍᴀsᴛᴇʀ✨", "https://t.me/Neiman_X_World")
    ]
]


@N1.on(events.NewMessage(pattern="/start"))
@N2.on(events.NewMessage(pattern="/start"))
@N3.on(events.NewMessage(pattern="/start"))
@N4.on(events.NewMessage(pattern="/start"))
@N5.on(events.NewMessage(pattern="/start"))
@N6.on(events.NewMessage(pattern="/start"))
@N7.on(events.NewMessage(pattern="/start"))
@N7.on(events.NewMessage(pattern="/start"))
@N8.on(events.NewMessage(pattern="/start"))
@N9.on(events.NewMessage(pattern="/start"))
@N10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        NeimanBot = await event.client.get_me()
        bot_name = NeimanBot.first_name
        bot_id = NeimanBot.id
        TEXT = f"**нєу [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​**\n╔━━━━━━❰𝗡𝗲𝗶𝗺𝗮𝗻𝗕𝗼𝘁❱━━━━━╗\n\n"
        TEXT += f"┣⪼ **му σωиєя​ : [иєιмαивσу](https://t.me/NeimanBoy_OP)**\n\n"
        TEXT += f"┣⪼ **иєιмαи νєяѕισи :** `M3.3`\n"
        TEXT += f"┣⪼ **ρутнσи νєяѕισи :** `3.11.3`\n"
        TEXT += f"┣⪼ **ᴛєℓєтнσи νєяѕισи :** `{__version__}`\n╚━━━━━━━━━━━━━━━━━━╝"
        await event.client.send_file(
                    event.chat_id,
                    "https://te.legra.ph/file/d6687f21d185a4a9edc15.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
      )
