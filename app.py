import telegram.ext
from telegram.ext import Updater, CommandHandler
import datetime
import pytz
import sqlite3

updater = Updater('2047279107:AAEyhyeOpA76bNa4PH5xFX7Xjdhof0RxZXE', use_context=True)
job = updater.job_queue
dispatcher = updater.dispatcher

db = sqlite3.connect("database.db")
cursor = db.cursor()


def start(update, context):
    message = 'Welcome to the bot'
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
# give a name to the command and add it to the dispaatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


subject = ['ds1', 'el1', 'cs1', 'ci1', 'pcv1', 'ds2', 'ci2', 'cs2', 'pcv2', 'el2']
users = ['1090783297', '967948229', '1079579102']
section = ['a', 'a', 'a']
staff_list = [['jan', 'ui', 'met', 'pd', 'ang', 'jan', 'pd', 'met', 'ang', 'ui'],
              ['abi', 'ui', 'met', 'pd', 'ang', 'abi', 'pd', 'met', 'ang', 'ui'],
              ['abi', 'ui', 'met', 'pd', 'ang', 'abi', 'pd', 'met', 'ang', 'ui']]

cl_1 = datetime.time(hour=8, minute=58, second=00,tzinfo=pytz.timezone('Asia/Kolkata'))
cl_2 = datetime.time(hour=13, minute=1, second=00,tzinfo=pytz.timezone('Asia/Kolkata'))
cl_3 = datetime.time(hour=13, minute=58, second=00,tzinfo=pytz.timezone('Asia/Kolkata'))

cl = [cl_1, cl_2, cl_3]


f = 1
query = [subject[q] + '_' + staff_list[0][q] for q in range(len(subject))]
ind = 0
for t in range(5):
    link1 = list(cursor.execute("SELECT link from schedule WHERE class = '{}'".format(query[ind])))
    link2 = list(cursor.execute("SELECT link from schedule WHERE class = '{}'".format(query[ind+1])))
    s = "Link for the Class\n"
    class_t = [s+link1[0][0], s+link2[0][0]]
    day = (t, t)
    for x in range(2):
        def func(context: telegram.ext.CallbackContext):
            context.bot.send_message(chat_id=users[0], text=class_t[x])
        job_daily = job.run_daily(func, days=day, time=cl[x])


    if f:
        lab_q = "lab_" + section[0]
        lab = list(cursor.execute("SELECT link from schedule WHERE class = '{}'".format(lab_q)))
        lab_link = lab[0][0]
        def func(context: telegram.ext.CallbackContext):
            context.bot.send_message(chat_id=users[0], text=lab_link)
        job_daily = job.run_daily(func, days=day, time=cl[2])
        f = 0
    ind += 2


####

f = 1
query = [subject[q] + '_' + staff_list[1][q] for q in range(len(subject))]
ind = 0
for t in range(5):
    link1 = list(cursor.execute("SELECT link from schedule WHERE class = '{}'".format(query[ind])))
    link2 = list(cursor.execute("SELECT link from schedule WHERE class = '{}'".format(query[ind+1])))
    s = "Link for the Class\n"
    class_t = [s+link1[0][0], s+link2[0][0]]
    day = (t, t)
    for x in range(2):
        def func(context: telegram.ext.CallbackContext):
            context.bot.send_message(chat_id=users[1], text=class_t[x])
        job_daily = job.run_daily(func, days=day, time=cl[x])

    if f:
        lab_q = "lab_" + section[1]
        lab = list(cursor.execute("SELECT link from schedule WHERE class = '{}'".format(lab_q)))
        lab_link = lab[0][0]
        def func(context: telegram.ext.CallbackContext):
            context.bot.send_message(chat_id=users[1], text=lab_link)
        job_daily = job.run_daily(func, days=day, time=cl[2])
        f = 0
    ind += 2

###

f = 1
query = [subject[q] + '_' + staff_list[2][q] for q in range(len(subject))]
ind = 0
for t in range(5):
    link1 = list(cursor.execute("SELECT link from schedule WHERE class = '{}'".format(query[ind])))
    link2 = list(cursor.execute("SELECT link from schedule WHERE class = '{}'".format(query[ind+1])))
    s = "Link for the Class\n"
    class_t = [s+link1[0][0], s+link2[0][0]]
    day = (t, t)
    for x in range(2):
        def func(context: telegram.ext.CallbackContext):
            context.bot.send_message(chat_id=users[2], text=class_t[x])
        job_daily = job.run_daily(func, days=day, time=cl[x])

    if f:
        lab_q = "lab_" + section[2]
        lab = list(cursor.execute("SELECT link from schedule WHERE class = '{}'".format(lab_q)))
        lab_link = lab[0][0]
        def func(context: telegram.ext.CallbackContext):
            context.bot.send_message(chat_id=users[2], text=lab_link)
        job_daily = job.run_daily(func, days=day, time=cl[2])
        f = 0
    ind += 2


updater.start_polling()
updater.idle()
