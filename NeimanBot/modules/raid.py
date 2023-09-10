import asyncio

from random import choice

from telethon import events

from config import N1, N2, N3, N4, N5, N6, N7, N8, N9, N10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from NeimanBot.data import RAID, REPLYRAID, NEIMAN, MRAID, SRAID, CRAID, NEIMAN

REPLY_RAID = []


@N1.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@N2.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@N3.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@N4.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@N5.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@N6.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@N7.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@N8.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@N9.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@N10.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
async def raid(e):
    if e.sender_id in SUDO_USERS:
        Nraid = e.text.split(" ", 2)

        if len(Nraid) == 3:
            entity = await e.client.get_entity(Nraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            if uid in NEIMAN:
                await e.reply("иσ, тнιѕ gυуѕ ιѕ тєℓєgяαм'кιиg.")
            elif uid == OWNER_ID:
                await e.reply("иσ, тнιѕ gυу ιѕ σωиєя σf тнєѕє вσтѕ .")
            elif uid in SUDO_USERS:
                await e.reply("иσ, тнιѕ gυу ιѕ α ѕυ∂σ υѕєя.")
            else:
                first_name = entity.first_name
                counter = int(xraid[1])
                username = f"[{first_name}](tg://user?id={uid})"
                for _ in range(counter):
                    reply = choice(RAID)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐑𝐚𝐢𝐝\n  » {hl}raid <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » {hl}raid <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
        except Exception as e:
            print(e)


@N1.on(events.NewMessage(incoming=True))
@N2.on(events.NewMessage(incoming=True))
@N3.on(events.NewMessage(incoming=True))
@N4.on(events.NewMessage(incoming=True))
@N5.on(events.NewMessage(incoming=True))
@N6.on(events.NewMessage(incoming=True))
@N7.on(events.NewMessage(incoming=True))
@N8.on(events.NewMessage(incoming=True))
@N9.on(events.NewMessage(incoming=True))
@N10.on(events.NewMessage(incoming=True))
async def _(event):
    global REPLY_RAID
    check = f"{event.sender_id}_{event.chat_id}"
    if check in REPLY_RAID:
        await asyncio.sleep(0.1)
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(choice(REPLYRAID)),
            reply_to=event.message.id,
        )


@N1.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@N2.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@N3.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@N4.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@N5.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@N6.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@N7.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@N8.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@N9.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@N10.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
async def rraid(e):
    if e.sender_id in SUDO_USERS:
        mkrr = e.text.split(" ", 1)
        if len(mkrr) == 2:
            entity = await e.client.get_entity(mkrr[1])

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)

        try:
            user_id = entity.id
            if user_id in NEIMAN:
                await e.reply("иσ, тнιѕ gυуѕ ιѕ тєℓєgяαм'кιиg.")
            elif user_id == OWNER_ID:
                await e.reply("иσ, тнιѕ gυу ιѕ σωиєя σf тнєѕє вσтѕ .")
            elif user_id in SUDO_USERS:
                await e.reply("иσ, тнιѕ gυу ιѕ α ѕυ∂σ υѕєя.")
            else:
                global REPLY_RAID
                check = f"{user_id}_{e.chat_id}"
                if check not in REPLY_RAID:
                    REPLY_RAID.append(check)
                await e.reply("» ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏʀᴀɪᴅ !! ✅")
        except NameError:
            await e.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝\n  » {hl}rraid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » {hl}rraid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")


@N1.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@N2.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@N3.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@N4.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@N5.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@N6.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@N7.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@N8.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@N9.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@N10.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
async def drraid(e):
    if e.sender_id in SUDO_USERS:
        text = e.text.split(" ", 1)

        if len(text) == 2:
            entity = await e.client.get_entity(text[1])
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)

        try:
            check = f"{entity.id}_{e.chat_id}"
            global REPLY_RAID
            if check in REPLY_RAID:
                REPLY_RAID.remove(check)
            await e.reply("» ʀᴇᴘʟʏ ʀᴀɪᴅ ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ !! ✅")
        except NameError:
            await e.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐃𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝\n  » {hl}drraid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » {hl}drraid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")


@N1.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@N2.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@N3.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@N4.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@N5.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@N6.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@N7.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@N8.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@N9.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@N10.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
async def mraid(e):
    if e.sender_id in SUDO_USERS:
        Nraid = e.text.split(" ", 2)

        if len(Nraid) == 3:
            entity = await e.client.get_entity(Nraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            first_name = entity.first_name
            counter = int(Nraid[1])
            username = f"[{first_name}](tg://user?id={uid})"
            for _ in range(counter):
                reply = choice(MRAID)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝗠𝗥𝗮𝗶𝗱\n  » {hl}mraid <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » {hl}mraid <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
        except Exception as e:
            print(e)


@N1.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@N2.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@N3.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@N4.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@N5.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@N6.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@N7.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@N8.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@N9.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@N10.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
async def sraid(e):
     if e.sender_id in SUDO_USERS:
        Nraid = e.text.split(" ", 2)

        if len(Nraid) == 3:
            entity = await e.client.get_entity(Nraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            first_name = entity.first_name
            counter = int(xraid[1])
            username = f"[{first_name}](tg://user?id={uid})"
            for _ in range(counter):
                reply = choice(SRAID)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝗦𝗥𝗮𝗶𝗱\n  » {hl}sraid <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » {hl}sraid <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
        except Exception as e:
            print(e)


@N1.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@N2.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@N3.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@N4.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@N5.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@N6.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@N7.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@N8.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@N9.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@N10.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
async def craid(e):
    if e.sender_id in SUDO_USERS:
        Nraid = e.text.split(" ", 2)

        if len(Nraid) == 3:
            entity = await e.client.get_entity(Nraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            if uid in NEIMAN:
                await e.reply("иσ, тнιѕ gυуѕ ιѕ тєℓєgяαм'кιиg.")
            elif uid == OWNER_ID:
                await e.reply("иσ, тнιѕ gυу ιѕ σωиєя σf тнєѕє вσтѕ .")
            elif uid in SUDO_USERS:
                await e.reply("иσ, тнιѕ gυу ιѕ α ѕυ∂σ υѕєя.")
            else:
                first_name = entity.first_name
                counter = int(xraid[1])
                username = f"[{first_name}](tg://user?id={uid})"
                for _ in range(counter):
                    reply = choice(CRAID)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐂𝗥𝗮𝗶𝗱\n  » {hl}raid <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » {hl}raid <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
        except Exception as e:
            print(e)
