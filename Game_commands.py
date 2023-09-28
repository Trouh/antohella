# name: Команды для игровых ботов
# meta developer: @MetaModules
# Commands:
# .bfg  | .evo  | .bfgb  | .iris

import time

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from .. import loader, utils

class BfgMod(loader.Module):
    """BFG, BFGB, MineEVO команды в любом чате"""

    async def bfgcmd(self, message):
        """— Выполнить команду в боте BFG в любом чате"""
        chat = "@bforgame_bot"
        args = utils.get_args_raw(message)
        text = f"{args}"
        reply = await message.get_reply_message()
        if not text and not reply:
            await message.edit("<b>Нет текста или реплая!</b>")
            return
        await message.edit("<b>Отправляю...</b>")
        async with message.client.conversation(chat) as conv:
            if text:
                try:
                    response = conv.wait_event(
                        events.NewMessage(incoming=True, from_users=1721358063)
                    )
                    await message.client.send_message(chat, text)
                    response = await response
                except YouBlockedUserError:
                    await message.edit("<b>Разблокируй @bforgame_bot!</b>")
                    return
            else:
                try:
                    user = await utils.get_user(reply)
                    response = conv.wait_event(
                        events.NewMessage(incoming=True, from_users=1721358063)
                    )
                    await message.client.send_message(
                        chat, f"{reply.raw_text} (с) {user.first_name}"
                    )
                    response = await response
                except YouBlockedUserError:
                    await message.edit("<b>Разблокируй @bforgame_bot!</b>")
                    return
        if response.text:
            await message.client.send_message(
                message.to_id, f"<b>{response.text}</b>"
            )
            await message.delete()
        if response.media:
            await message.client.send_file(
                message.to_id, response.media, reply_to=reply.id if reply else None
            )
            await message.delete()


    async def evocmd(self, message):
        """— Выполнить команду в боте MineEVO в любом чате"""
        chat = "@mine_evo_bot"
        args = utils.get_args_raw(message)
        text = f"{args}"
        reply = await message.get_reply_message()
        if not text and not reply:
            await message.edit("<b>Нет текста или реплая!</b>")
            return
        await message.edit("<b>Отправляю...</b>")
        async with message.client.conversation(chat) as conv:
            if text:
                try:
                    response = conv.wait_event(
                        events.NewMessage(incoming=True)
                    )
                    await message.client.send_message(chat, text)
                    response = await response
                except YouBlockedUserError:
                    await message.edit("<b>Разблокируй @mine_evo_bot!</b>")
                    return
            else:
                try:
                    user = await utils.get_user(reply)
                    response = conv.wait_event(
                        events.NewMessage(incoming=True)
                    )
                    await message.client.send_message(
                        chat, f"{reply.raw_text} (с) {user.first_name}"
                    )
                    response = await response
                except YouBlockedUserError:
                    await message.edit("<b>Разблокируй @mine_evo_bot!</b>")
                    return
        if response.text:
            await message.client.send_message(
                message.to_id, f"<b>{response.text}</b>"
            )
            await message.delete()
        if response.media:
            await message.client.send_file(
                message.to_id, response.media, reply_to=reply.id if reply else None
            )
            await message.delete()
            
            
    async def bfgbcmd(self, message):
        """— Выполнить команду в боте Bfgb в любом чате"""
        chat = "@bfgbunker_bot"
        args = utils.get_args_raw(message)
        text = f"{args}"
        reply = await message.get_reply_message()
        if not text and not reply:
            await message.edit("<b>Нет текста или реплая!</b>")
            return
        await message.edit("<b>Отправляю...</b>")
        async with message.client.conversation(chat) as conv:
            if text:
                try:
                    response = conv.wait_event(
                        events.NewMessage(incoming=True)
                    )
                    await message.client.send_message(chat, text)
                    response = await response
                except YouBlockedUserError:
                    await message.edit("<b>Разблокируй @bfgbunker_bot!</b>")
                    return
            else:
                try:
                    user = await utils.get_user(reply)
                    response = conv.wait_event(
                        events.NewMessage(incoming=True)
                    )
                    await message.client.send_message(
                        chat, f"{reply.raw_text} (с) {user.first_name}"
                    )
                    response = await response
                except YouBlockedUserError:
                    await message.edit("<b>Разблокируй @bfgbunker_bot!</b>")
                    return
        if response.text:
            await message.client.send_message(
                message.to_id, f"<b>{response.text}</b>"
            )
            await message.delete()
        if response.media:
            await message.client.send_file(
                message.to_id, response.media, reply_to=reply.id if reply else None
            )
            await message.delete()
            
            
    async def iriscmd(self, message):
        """— Выполнить команду в боте Iris в любом чате"""
        chat = "@iris_black_bot"
        args = utils.get_args_raw(message)
        text = f"{args}"
        reply = await message.get_reply_message()
        if not text and not reply:
            await message.edit("<b>Нет текста или реплая!</b>")
            return
        await message.edit("<b>Отправляю...</b>")
        async with message.client.conversation(chat) as conv:
            if text:
                try:
                    response = conv.wait_event(
                        events.NewMessage(incoming=True)
                    )
                    await message.client.send_message(chat, text)
                    response = await response
                except YouBlockedUserError:
                    await message.edit("<b>Разблокируй @iris_black_bot!</b>")
                    return
            else:
                try:
                    user = await utils.get_user(reply)
                    response = conv.wait_event(
                        events.NewMessage(incoming=True)
                    )
                    await message.client.send_message(
                        chat, f"{reply.raw_text} (с) {user.first_name}"
                    )
                    response = await response
                except YouBlockedUserError:
                    await message.edit("<b>Разблокируй @iris_black_bot!</b>")
                    return
        if response.text:
            await message.client.send_message(
                message.to_id, f"<b>{response.text}</b>"
            )
            await message.delete()
        if response.media:
            await message.client.send_file(
                message.to_id, response.media, reply_to=reply.id if reply else None
            )
            await message.delete()
