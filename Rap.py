# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: EminemRap
# meta developer: @antohella and @ellllsy
# Commands:
# .menu  | .rapgad
# meta banner: https://te.legra.ph/file/3567b02f5c727d7c6c9e4.mp4
# ---------------------------------------------------------------------------------

import random
from asyncio import sleep
import os
from .. import loader, utils
from telethon.tl.functions.users import GetFullUserRequest
import time
from telethon.tl.types import Message
import random
import re


@loader.tds
class EminemRap(loader.Module):

    strings = {"name": "EminemRap"} 
    
    async def client_ready(self, client, db):
        self.db = db
        self.client = client

    async def menucmd(self, message):
        """– показать меню и возможности"""
        args = utils.get_args_raw(message)
        await message.edit("Загрузка меню.")
        await message.edit("Загрузка меню..")
        await message.edit("Загрузка меню...")
        time.sleep(0.1)
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        

        message = await utils.answer(message, self.strings("loading"))
        media_files = ("https://static.tildacdn.info/tild6436-3531-4435-b264-636365666662/tenor.gif", "https://static.tildacdn.info/tild6436-3531-4435-b264-636365666662/tenor.gif", "https://static.tildacdn.info/tild6436-3531-4435-b264-636365666662/tenor.gif")
        try:
            user_id = (
                (
                    (
                        await self._client.get_entity(
                            args if not args.isdigit() else int(args)
                        )
                    ).id
                )
                if args
                else reply.sender_id
            )
        except Exception:
            user_id = self._tg_id

            user = await self._client(GetFullUserRequest(user_id))

            user_ent = user.users[0]

            user_info = (
            "<b>Команды:</b>\n\n"
            f"<b>.rapgad – RapGad eminem\n\n"
            f"<b>🥰 Скоро новый рэп eminema🥰\n"
            )
            chat_id = message.chat.id
            if chat_id:
                 await self.client.send_file(message.peer_id, random.choice(media_files), caption=user_info)

    @loader.owner
    async def rapgadcmd(self, message):
        for _ in range(1):
            for rapgad in [
                "Слушай, мне хотелось все сделать как можно лучше",
                "И у меня был один лишь шанс",
                "Идëт всë не так",
                "Просто мне кажется, что щас что-то должно случиться",
                "Но я не знаю что",
                "И если это то, что я думаю, у нас проблемы, большие",
                "Ну и если же он правда такой псих",
                "Я лучше не рисковал бы",
                "Ты то что хотел доктор",
                "Ощущать себя стал я как рэп бог, рэп бог",
                "Мои люди руки подняли в небо, в небо",
                "Хотели убрать, но это никто не смог, не смог",
                "Мне говорили ты робот, ну да, я рэп бот",
                "Навык делать реп, будто компьютер, это в крови",
                "Походу есть это во мне с детства",
                "И предохранитель мой не держит",
                "И дал мне сделать мой рэп денег",
               "Выживал и делал эти тексты",
              "Пока был Билл Клинтон президентом",
              "И Моника Левински в резиденции.. (отсос)",
              "Я же MC мега честный",
              "И могу я так язвить бесконечно",
              "Треками покалечить (покалечить)",
              "Советую тебе не перечить со мной",
              "Ты же по-любому не желаешь увидать",
              "Какой там для тебя я берегу автомат у себя",
              "ваш рап как шлак, да да, я доказал давно вам",
              "Ведь щас даже я в эту минуту",
              "Проделываю круто",
              "Звуковые трюки",
              "И тебе испуга",
              "Не миновать",
              "И по головам",
              "Надавать",
              "Могу вам",
              "Я не сдался и меня поднял договор мой с эфтермеф резко наверх",
              "Остаться не мог незамеченным взрыв бомб",
              "А для реперов, всех тех, кого бездарем считаю я, это бедствие!",
              "Текстам вашим место в огне",
              "Ваш удел это бедность, вас повергнет мой в бегство шедевр",
              "Ощущать себя стал я как рэп бог, рэп бог",
              "Мои люди руки подняли в небо, в небо",
              "Хотели убрать, но это никто не смог, не смог",
              "Покажу вам, что богом быть это легко, легко",
             "Каждый хочет получить этот ключ и раскрыть бессмертия в рэпе секрет мой",
             "Но ведь, а если быть честным, дело в том что с детства я дерзкий",
             " А ведь люди таких ценят и верят",
             "Я хотел до небес долететь, но врезался в землю, пиу",
             "Для MC это урок по рифмам",
             "Чтобы им знать, я же будто Баста Раймс",
             "Недореперов я учу читать",
             "Меня воспитывал Раким, Лаким Шабаз, Тупак, и",
             "Дабл ю, эй Кьб, Эй Док, Рин, Елла, Изи, спасибо, стал Слим",
             "Рвать и метать, я же был на это вдохновлен неслабо",
             "И вот Ран Ди-Эм-Си однажды, завел в зал рок н ролла славы",
             "Хоть даже в храме окутан пламенем грехов, и в зале славы",
             "Будто нарик я поставлен буду на стену позора в дальний угол",
             "Ты думаешь это игра? но ты пересек ту грань",
             "Я казню вас, не забудете вы этот ужас",
             "Ты на гея похож",
             "Глядя на тебя не могу сдержать смеха и слов (ха ха)",
             "Ты выглядишь неважно на моём фоне",
             "Будто тебя переехал вагон",
             "О нет ведь, он гей ведь — твердят все об одном",
             "И тычут большой палец тебе",
             "Ежедневно выполнять указы лейбла готов",
             "Эй, голубой, ну и где гонор твой?",
             "Я думал всегда своей головой",
             "Ну а ты же лишь марионетка и нет своего в тебе ничего",
             "Место моё занять у тебя не удастся",
             "Ты беспонтовый бездарь и лох",
             "Ощущать себя стал я как рэп бог, рэп бог",
             "Мои люди руки подняли в небо, в небо",
             "Я неуязвим, называть меня можешь Рембо, Рембо",
             "Но я не добряк как он, живет во мне зло",
             "Я генерал Зод с Криптона, встань на колени без слов, без слов",
             "Если ты Тор, то я Один",
             "Ты ни на что не годен",
             "Меня не стоит трогать",
             "Или ты будешь взорван бомбой",
             "Я с головою в ссоре",
             "Уничтожу вскоре вас",
             "Ведь я озлоблен словно зомби",
             "А ты же ведь никто в хип-хопе!",
             "Я доберман, ты пудель",
             "Братьями никогда не будем",
             "Я вернулся и по сравнению со мной",
             "Школьник ты ссаный будто (я здесь)",
             "Моя правда рубит нещадно и грубо",
             "Свой дар пущу во благо я людям",
             "Вот почему мне щас захотелось убедиться",
             "Что я помогаю избегать смуту",
             " И дам шанс я",
             "Чтобы ты в себя поверил и стал счастлив",
            "Но я берегу пару панчлайнов",
        "Реперы на меня ведь так лают",
        "Этим они все заполучить хотят славы",
        "На их попытки я клал!",
            "Меня же не поломать, я доказал",
           "Это вам, мой рэп не стал слаб",
           "Я не продал его за нал и не смогла",
           "Меня одолеть эта попса",
           "Но лишь наверх я поднялся",
           "Цензурить кто то меня стал",
           "Ну например вот, альбом если мой взять старый",
           "Там я хотел сказать что в Колумбайне",
           "Возьму детей и возьму АК, но не дали мне сказать так!",
           "Видишь, это щас прокатило, а значит уже я не так велик",
           "Но, стал уже я богом, пережив так много",
           " Ты остался ещë в 2004-м",
           "Не могу понять на кой чёрт",
           "Из себя ты репера корчишь",
           "Ты будешь порван, ты еще в норме?",
           "Нахер все нормы!",
           "Я недавно купил себе новый бластер",
           "И он жару даст вам всем, как Фаболоусу Рей Джей дал",
           "Ведь Фаб говорит, что было по гейски петь с мужиком под фортепиано",
           "Блин чувак, это было на ТВ с утра до ночи прямо",
           "Потом Джей в ответ на следующий день в эфире сказал",
           "Эй Фэб, ты покойник!",
           "Я вам покажу теперь нереальный скилл (Джей Джей Фэт)",
           "Сама лама дума лама",
          "Я новатор и не человек я даже",
          "Доказать это вам надо",
          "Слова, сказанные вами",
          "Рикошетом отлетают",
          "Я поставлю на места вас",
          "И не сдамся никогда я",
          "Как бы этого не ждали вы",
          "Читать не перестану я",
          "И с каждым треком заново",
          "Лишь открываю занавес",
          "Я снова потрясаю вас",
          "А хейтеры все замерли",
          "У них приступы зависти",
          "Когда качаю залы я",
          "Понятно что я людям нужен",
          "Твои треки режут уши",
          "О, стал попсой он",
          "Сказал ты, а самого от зависти контузит",
          "Твой рап это попса",
          "Я нашел как завязать их в узел",
          "И стал ядерным стайл",
          "Наводящим на реперов ужас",
          "Не могу я понять как он смог, не могу найти я слов",
          "Говори, когда найдешь слова",
          "А пока???",
          "Раунд!",
          
          
          
          
           
        


            


           
            ]:
                await message.edit(rapgad)
                await sleep(1.6)
                        
                
