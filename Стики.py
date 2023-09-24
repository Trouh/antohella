# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: Стики вк и тянок
# Author: тоша
# Idea: тоша
# Commands:
# .тянка | .вк
# ---------------------------------------------------------------------------------
# meta developer: @antohella
# meta idea: @antohella
# scope: hikka_only
# scope: hikka_min 1.3.0

import random
from asyncio import sleep

import psutil
import time
from telethon.tl.types import Message

from .. import loader, utils



@loader.tds
class Mod(loader.Module):
    """Отправляет рандом стики вк, тянок, мемов и фотки"""

    strings = {"name": "Рандом стики"}
    
    @loader.command()
    async def тянкаcmd(self, message: Message):
        """--> отправляет рандомную тянку"""
        args =utils.get_args_raw(message)
        await message.edit("Загрузка.")
        await message.edit("Загрузка..")
        await message.edit("Загрузка...")
        time.sleep(0.1)
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        m = random.choice(await self.client.get_messages("@tyanka228uuu", limit=1000))
        if reply:
            await self.client.send_message(message.chat_id, file=m, reply_to=reply)
        else:
            await message.respond(file=m)

        if message.out:
            await message.delete()

    @loader.command()
    async def вкcmd(self, message: Message):
        """--> отправляет рандомный стик из вк"""
        args =utils.get_args_raw(message)
        await message.edit("Загрузка.")
        await message.edit("Загрузка..")
        await message.edit("Загрузка...")
        time.sleep(0.1)
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        m = random.choice(await self.client.get_messages("@vksticksmodule", limit=1000))
        if reply:
            await self.client.send_message(message.chat_id, file=m, reply_to=reply)
        else:
            await message.respond(file=m)

        if message.out:
            await message.delete()
            
    @loader.command()
    async def селтиcmd(self, message: Message):
        """--> отправляет рандомное фото Seltin sweet"""
        args =utils.get_args_raw(message)
        await message.edit("Загрузка.")
        await message.edit("Загрузка..")
        await message.edit("Загрузка...")
        time.sleep(0.1)
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        m = random.choice(await self.client.get_messages("@nichegonovog", limit=1000))
        if reply:
            await self.client.send_message(message.chat_id, file=m, reply_to=reply)
        else:
            await message.respond(file=m)

        if message.out:
            await message.delete()
            
    @loader.command()
    async def мемcmd(self, message: Message):
        """--> отправляет рандомный мем"""
        args =utils.get_args_raw(message)
        await message.edit("Загрузка.")
        await message.edit("Загрузка..")
        await message.edit("Загрузка...")
        time.sleep(0.1)
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        m = random.choice(await self.client.get_messages("@memesmodule", limit=1000))
        if reply:
            await self.client.send_message(message.chat_id, file=m, reply_to=reply)
        else:
            await message.respond(file=m)

        if message.out:
            await message.delete()
