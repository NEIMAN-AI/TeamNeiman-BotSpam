from telethon import events, Button

from config import N1, N2, N3, N4, N5, N6, N7, N8, N9, N10, SUDO_USERS, CMD_HNDLR as hl


HELP_STRING = f"★ 𝗜𝘁'𝘀 𝗡𝗲𝗶𝗺𝗮𝗻 𝗕𝗼𝘁𝗦𝗽𝗮𝗺 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪 ★\n\n» **ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ꜰᴏʀ ʜᴇʟᴘ**\n» **ᴅᴇᴠᴇʟᴏᴘᴇʀ: @TeamNeiman**"

HELP_BUTTON = [
    [
      Button.inline(" ꜱᴘᴀᴍ ", data="spam"),
      Button.inline(" ʀᴀɪᴅ ", data="raid")
    ],
    [
      Button.inline(" ᴇxᴛʀᴀ ", data="extra")
    ],
    [
      Button.url(" ᴄʜᴀɴɴᴇʟ ", "https://t.me/TeamNeiman"),
      Button.url(" sᴜᴘᴘᴏʀᴛ ", "https://t.me/Neiman_X_Support")
    ],
    [
      Button.url(" ᴍᴀsᴛᴇʀ ", "https://t.me/Neiman_X_World")
    ]
  ]


@N1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@N2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@N3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@N4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@N5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@N6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@N7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@N8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@N9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@N10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
        try:
          await event.client.send_file(event.chat_id,
              "https://te.legra.ph/file/d6687f21d185a4a9edc15.jpg",
              caption=HELP_STRING,
              buttons=HELP_BUTTON
              )
        except Exception as e:
            await event.client.send_message(event.chat_id, f"An Exception Occured!\n\n**ERROR:** {str(e)}")


extra_msg = f"""
**» ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ:**

𝗨𝘀𝗲𝗿𝗕𝗼𝘁: **ᴜꜱᴇʀʙᴏᴛ ᴄᴍᴅꜱ**
  1) {hl}ping 
  2) {hl}reboot
  3) {hl}sudo <reply to user>  --> Owner Cmd
  4) {hl}logs --> Owner Cmd

𝗘𝗰𝗵𝗼: **ᴛᴏ ᴀᴄᴛɪᴠᴇ ᴇᴄʜᴏ ᴏɴ ᴀɴʏ ᴜꜱᴇʀ**
  1) {hl}echo <reply to user>
  2) {hl}rmecho <reply to user>

𝗟𝗲𝗮𝘃𝗲: **ᴛᴏ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ**
  1) {hl}leave <group/chat id>
  2) {hl}leave : Type in the Group bot will auto leave that group


**© @TeamNeiman**
"""

                 
raid_msg = f"""
**» ʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅꜱ:**

𝗥𝗮𝗶𝗱: **ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜꜱᴇʀ ꜰᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ.**
  1) {hl}raid <count> <username>
  2) {hl}raid <count> <reply to user>

𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱: **ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
  1) {hl}rraid <replying to user>
  2) {hl}rraid <username>

𝗗𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱: **ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
  1) {hl}drraid <replying to user>
  2) {hl}drraid <username>

𝐌𝐑𝐚𝐢𝐝: **ʟᴏᴠᴇ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
  1) {hl}mraid <count> <username>
  2) {hl}mraid <count> <reply to user>

𝐒𝐑𝐚𝐢𝐝: **ꜱʜᴀʏᴀʀɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
  1) {hl}sraid <count> <username>
  2) {hl}sraid <count> <reply to user>

𝐂𝐑𝐚𝐢𝐝: **ᴀʙᴄᴅ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
  1) {hl}craid <count> <username>
  2) {hl}craid <count> <reply to user>


**© @TeamNeiman**
"""

spam_msg = f"""
**» ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ:**

𝗦𝗽𝗮𝗺: **ꜱᴘᴀᴍꜱ ᴀ ᴍᴇꜱꜱᴀɢᴇ.**
  1) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
  2) {hl}spam <count> <replying any message>

𝗣𝗼𝗿𝗻𝗦𝗽𝗮𝗺: **ᴘᴏʀᴍᴏɢʀᴀᴘʜʏ ꜱᴘᴀᴍ.**
  1) {hl}pspam <count>

𝗛𝗮𝗻𝗴: **ꜱᴘᴀᴍꜱ ʜᴀɴɢɪɴɢ ᴍᴇꜱꜱᴀɢᴇ ꜰᴏʀ ɢɪᴠᴇɴ ᴄᴏᴜɴᴛᴇʀ.**
  1) {hl}hang <counter>


** © @TeamNeiman**
"""                     
           
           
@N1.on(events.CallbackQuery(pattern=r"help_back"))
@N2.on(events.CallbackQuery(pattern=r"help_back"))
@N3.on(events.CallbackQuery(pattern=r"help_back"))
@N4.on(events.CallbackQuery(pattern=r"help_back"))
@N5.on(events.CallbackQuery(pattern=r"help_back"))
@N6.on(events.CallbackQuery(pattern=r"help_back"))
@N7.on(events.CallbackQuery(pattern=r"help_back"))
@N8.on(events.CallbackQuery(pattern=r"help_back"))
@N9.on(events.CallbackQuery(pattern=r"help_back"))
@N10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(
            HELP_STRING,
            buttons=[
              [
                Button.inline(" ꜱᴘᴀᴍ ", data="spam"),
                Button.inline(" ʀᴀɪᴅ ", data="raid")
              ],
              [
                Button.inline(" ᴇxᴛʀᴀ ", data="extra")
              ],
              [
                Button.url(" ᴄʜᴀɴɴᴇʟ ", "https://t.me/TeamNeiman"),
                Button.url(" sᴜᴘᴘᴏʀᴛ ", "https://t.me/Neiman_X_Support")
              ],
              [
                Button.url("ᴍʏ ᴍᴀsᴛᴇʀ", "https://t.me/Neiman_X_Support")
            ]
            ]
    else:
        await event.answer("Make Your Own Neiman Bots !! @TeamNeiman", cache_time=0, alert=True)


@N1.on(events.CallbackQuery(pattern=r"spam"))
@N2.on(events.CallbackQuery(pattern=r"spam"))
@N3.on(events.CallbackQuery(pattern=r"spam"))
@N4.on(events.CallbackQuery(pattern=r"spam"))
@N5.on(events.CallbackQuery(pattern=r"spam"))
@N6.on(events.CallbackQuery(pattern=r"spam"))
@N7.on(events.CallbackQuery(pattern=r"spam"))
@N8.on(events.CallbackQuery(pattern=r"spam"))
@N9.on(events.CallbackQuery(pattern=r"spam"))
@N10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(spam_msg,
              buttons=[[Button.inline("< Back", data="help_back"),],],
              ) 
    else:
        await event.answer("Make Your Own NEIMAN Bots !! @fuck_uff_XD", cache_time=0, alert=True)


@N1.on(events.CallbackQuery(pattern=r"raid"))
@N2.on(events.CallbackQuery(pattern=r"raid"))
@N3.on(events.CallbackQuery(pattern=r"raid"))
@N4.on(events.CallbackQuery(pattern=r"raid"))
@N5.on(events.CallbackQuery(pattern=r"raid"))
@N6.on(events.CallbackQuery(pattern=r"raid"))
@N7.on(events.CallbackQuery(pattern=r"raid"))
@N8.on(events.CallbackQuery(pattern=r"raid"))
@N9.on(events.CallbackQuery(pattern=r"raid"))
@N10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(raid_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
          )
    else:
        await event.answer("Make Your Own Neiman Bots !! @fuck_uff_XD", cache_time=0, alert=True)


@N1.on(events.CallbackQuery(pattern=r"extra"))
@N2.on(events.CallbackQuery(pattern=r"extra"))
@N3.on(events.CallbackQuery(pattern=r"extra"))
@N4.on(events.CallbackQuery(pattern=r"extra"))
@N5.on(events.CallbackQuery(pattern=r"extra"))
@N6.on(events.CallbackQuery(pattern=r"extra"))
@N7.on(events.CallbackQuery(pattern=r"extra"))
@N8.on(events.CallbackQuery(pattern=r"extra"))
@N9.on(events.CallbackQuery(pattern=r"extra"))
@N10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(extra_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
            )
    else:
        await event.answer("Make Your Own Neiman Bots babe !! @fuck_uff_XD", cache_time=0, alert=True)
