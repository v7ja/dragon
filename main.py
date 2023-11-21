import json
from pyromod import listen
from threading import Thread
from pyrogram import Client, filters
import os
import sys
import asyncio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from catch import catch
from list_catch import list_catch
from long_time import long_time
#from proxy_scrape import http_proxies, start_scrap
api_id = 18922496
api_hash = '371d1dc33eccaa19bb0814a27bb98f3c'
token = "5908403050:AAGBvrh-nvXQtMcdADCiSUBLoHqOZSCdklk"
bot = Client("Bot", bot_token=token, api_hash=api_hash, api_id=api_id)
dev = 5701395951
admins = [5701395951, 1694386561]
stats = []
force_stop = []
threads_num = 3
api_id = 18922496
api_hash = '371d1dc33eccaa19bb0814a27bb98f3c'


def dump(data):
    with open('data.json', "w", encoding="utf-8") as f:
        json.dump(data, f)


def load():
    with open('data.json', "r", encoding="utf-8") as f:
        return json.load(f)


keyboard = InlineKeyboardMarkup(
    [[InlineKeyboardButton("Random usernames", callback_data="checker"), InlineKeyboardButton("List usernames", callback_data="list_catch")],
     [
        InlineKeyboardButton("Delete accounts", callback_data="delete"),
     InlineKeyboardButton("Add accounts", callback_data="add")
     ],
     [
        InlineKeyboardButton("Stop checker", callback_data="stopper")
     # 'InlineKeyboardButton("Checker status", callback_data="status")'
     ], [InlineKeyboardButton(text="Dev", url="t.me/R0R77")]])


async def run_chath(session, ch, user_id, acc, username_shape):
    await catch(session, ch, user_id, acc, username_shape, bot)


async def run_list_chath(session, ch, user_id, acc, list):
    await list_catch(session, ch, user_id, acc, bot, list)

data = load()
for i in data:
    for j in data[i]:
        try:
            if j != "accounts":
                if data[i][j]['status'] == "on":
                    session = data[i][j]["session"]
                    ch = data[i][j]["ch"]
                    user_id = i
                    acc = j
                    if data[i][j]["catcher"] == "random":
                        for b in range(threads_num):
                            t = Thread(target=asyncio.run,
                                       args=(run_chath(session, ch, user_id, acc), ))
                            t.start()
                    else:
                        for b in range(threads_num):
                            list = data[i][j]["list"]
                            t = Thread(target=asyncio.run,
                                       args=(run_list_chath(session, ch, user_id, acc, list), ))
                            t.start()

        except Exception as e:
            print(e)


# Start msg


@bot.on_message(filters.command("start"))
async def start(bot, msg):
    if msg.from_user.id not in admins:
        pass
    await bot.send_message(msg.chat.id,
                           "اهلا بك في البوت ! \nاختر امر من الاوامر ادناه .",
                           reply_markup=keyboard)

# Random catch forward


async def random_catch_forward(call):
    cid = call.message.chat.id
    user_id = str(call.from_user.id)
    data = load()
    try:
        data[user_id]["accounts"]
    except:
        await bot.send_message(cid, "ليس لديك اي حساب ! .")
        return
    keyboard2 = InlineKeyboardMarkup([])
    for i in range(int(data[user_id]["accounts"])):
        i += 1
        i = str(i)
        session = data[user_id][str(i)]["session"]
        try:
            client = Client("", session_string=session)
            await client.start()
            me = await client.get_me()
            keyboard2.inline_keyboard += [[
                InlineKeyboardButton(me.first_name, callback_data="start:" + i)
            ]]
            await client.stop()
        except:
            pass
    keyboard2.inline_keyboard += [[
        InlineKeyboardButton("Dev", url="t.me/R0R77")
    ]]
    await bot.send_message(cid, "brelin the best :)", reply_markup=keyboard2)

# List catch forward


async def list_catch_forward(call):
    cid = call.message.chat.id
    user_id = str(call.from_user.id)
    data = load()
    try:
        data[user_id]["accounts"]
    except:
        await bot.send_message(cid, "ليس لديك اي حساب ! .")
        return
    keyboard2 = InlineKeyboardMarkup([])
    for i in range(int(data[user_id]["accounts"])):
        i += 1
        i = str(i)
        session = data[user_id][str(i)]["session"]
        try:
            client = Client("", session_string=session)
            await client.start()
            me = await client.get_me()
            keyboard2.inline_keyboard += [[
                InlineKeyboardButton(
                    me.first_name, callback_data="catch_list:" + i)
            ]]
            await client.stop()
        except:
            pass
    keyboard2.inline_keyboard += [[
        InlineKeyboardButton("Dev", url="t.me/R0R77")
    ]]
    await bot.send_message(cid, "jmthon the best :)", reply_markup=keyboard2)

# Tries for each account .


async def tries(call):
    cid = call.message.chat.id
    user_id = str(call.from_user.id)
    data = load()
    try:
        data[user_id]["accounts"]
    except:
        await bot.send_message(cid, "ليس لديك اي حساب ! .")
        return
    keyboard2 = InlineKeyboardMarkup([])
    for i in range(int(data[user_id]["accounts"])):
        i += 1
        i = str(i)
        session = data[user_id][str(i)]["session"]
        try:
            client = Client("", session_string=session)
            await client.start()
            me = await client.get_me()
            tries = data[user_id][str(i)]["tries"]
            keyboard2.inline_keyboard += [[
                InlineKeyboardButton(f"{me.first_name} : {tries}",
                                     callback_data="none")
            ]]
            await client.stop()
        except:
            pass
    keyboard2.inline_keyboard += [[
        InlineKeyboardButton("Dev", url="t.me/R0R77")
    ]]
    await bot.send_message(cid, "jmthon the best :)", reply_markup=keyboard2)

# Stop account , work on random and list catch


async def stop(call):
    cid = call.message.chat.id
    user_id = str(call.from_user.id)
    data = load()
    try:
        data[user_id]["accounts"]
    except:
        await bot.send_message(cid, "ليس لديك اي حساب ! .")
        return
    keyboard2 = InlineKeyboardMarkup([])
    for i in range(int(data[user_id]["accounts"])):
        i += 1
        i = str(i)
        session = data[user_id][str(i)]["session"]
        try:
            client = Client("", session_string=session)
            await client.start()
            me = await client.get_me()
            keyboard2.inline_keyboard += [[
                InlineKeyboardButton(
                    f"{me.first_name}", callback_data="stop:" + i)
            ]]
            await client.stop()
        except:
            pass
    keyboard2.inline_keyboard += [[
        InlineKeyboardButton("Dev", url="t.me/R0R77")
    ]]
    await bot.send_message(cid, "Choice account to stop :", reply_markup=keyboard2)


# Accounts mange


async def add_acccounts(call):
    msg = call.message
    cid = msg.chat.id
    user_id = call.from_user.id
    data = load()
    try:
        data[user_id]["accounts"]
        await bot.send_message(cid, "انت ضايف حساب قبل , لازم تحذفه")
        return
    except:
        pass
    try:
        print(cid)
        count = await bot.ask(cid, "ادخل عدد الحسابات لديك : ")
        count = int(count.text)
    except Exception as e:
        print(e)
        await bot.send_message(cid, "يرجى ادخال رقم ! ")
        return
    for i in range(int(count)):
        i += 1
        s = await bot.ask(cid, f"ادخل كود بايرو للحساب رقم ({i}) : ")
        try:
            data[user_id][i] = {
                "session": s.text,
                "tries": 0,
                "status": "off",
                "ch": "none",
                "stop": "no"
            }
        except:
            data[user_id] = {
                "accounts": int(count),
                i: {
                    "session": s.text,
                    "tries": 0,
                    "status": "off",
                    "ch": "none",
                    "stop": "no"
                }
            }
    dump(data)
    await bot.send_message(cid, "تم اضافة كل الحسابات .")


async def delete_accounts(call):
    msg = call.message
    cid = msg.chat.id
    user_id = call.from_user.id
    try:
        data = load()
        del data[str(user_id)]
        await bot.send_message(cid, "تم حذف جميع الحسابات لديك !")
        dump(data)
    except Exception as e:
        print(e)
        await bot.send_message(cid, "ليس لديك اي حساب ! .")
# Call back query


@bot.on_callback_query()
async def answer(_, call):
    data = call.data
    msg = call.message
    user_id = call.from_user.id
    await call.message.delete()
    if data == "checker":
        await random_catch_forward(call)
    elif "list_catch" == data:
        await list_catch_forward(call)
    elif data == "add":
        await add_acccounts(call)
    elif data == "delete":
        await delete_accounts(call)
    elif data == "status":
        await tries(call)
    elif data == "stopper":
        await stop(call)
    elif "start" in data:
        acc = str(data.split(":")[1])
        ch = await bot.ask(
            call.message.chat.id,
            "ارسل يوزر القناة لتثبيت اليوزر , او ارسل (حساب) للتثبيت على الحساب")
        username_shape = await bot.ask(
            call.message.chat.id,
            "ارسل مثال عليوزرات , مثلا : \n @A_X_B (ثلاثي) \n - X => حرف او رقم عشوائي \n - A => حرف عشوائي \n - B => حرف او رقم عشوائي ")
        data = load()
        session = data[str(user_id)][acc]["session"]
        await bot.send_message(call.message.chat.id, "سيتم بدء الصيد !")
        if "@" in ch.text:
            ch = ch.text.replace("@", "")
        for i in range(threads_num):
            t = Thread(target=asyncio.run,
                       args=(run_chath(session, ch.text, str(user_id), str(acc), username_shape.text), ))
            t.start()
    elif "catch_list" in data:
        acc = str(data.split(":")[1])
        ch = await bot.ask(
            call.message.chat.id,
            "ارسل يوزر القناة لتثبيت اليوزر , او ارسل (حساب) للتثبيت على الحساب")
        list = await bot.ask(
            call.message.chat.id,
            "ارسل لسته اليوزرات مثل : \n @R0R77 \n @jmthon ")
        list = list.text.split("\n")
        if "" in list:
            list.remove("")
        data = load()
        session = data[str(user_id)][acc]["session"]
        await bot.send_message(call.message.chat.id, "سيتم بدء الصيد !")
        if "@" in ch.text:
            ch = ch.text.replace("@", "")
        for i in range(threads_num):
            t = Thread(target=asyncio.run,
                       args=(run_list_chath(session, ch.text, str(user_id), acc, list), ))
            t.start()
    elif "stop" in data:
        acc = str(data.split(":")[1])
        data = load()
        data[str(user_id)][str(acc)]["stop"] = "yes"
        await bot.send_message(msg.chat.id, "Ok, This account will stop .")
        dump(data)

# Dev commands


@bot.on_message(filters.command("long_time"))
async def adder(_, msg):
    await msg.reply("OK")
    for b in range(40):
        Thread(target=asyncio.run, args=(long_time(bot, msg),)).start()


@ bot.on_message(filters.command("adder"))
async def adder(_, msg):
    id = msg.text.split()[1]
    admins.append(int(id))
    pass


@ bot.on_message(filters.command("scrape"))
async def scrape(_, msg):
    start_scrap()

    for i in http_proxies:
        with open("proxies.txt", "a") as f:
            f.write(i+"-")
    await bot.send_message("Seccsufly scrape !")


@ bot.on_message(filters.command("kill"))
async def kill(_, msg):
    if msg.from_user.id == dev:
        await bot.send_message(msg.chat.id, "Ok")
        sys.exit()
    else:
        return


@ bot.on_message(filters.command("restart"))
async def restart(_, msg):
    if msg.from_user.id == dev:
        await bot.send_message(msg.chat.id, "Ok")
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        return


@ bot.on_message(filters.command("cls"))
async def cls(_, msg):
    if msg.from_user.id == dev:
        os.system("clear")
    else:
        return


print('Running')
bot.run()
