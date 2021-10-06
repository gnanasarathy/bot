import telegram.ext
from telegram.ext import Updater
import datetime
import pytz
import sqlite3

updater = Updater('2047279107:AAEyhyeOpA76bNa4PH5xFX7Xjdhof0RxZXE', use_context=True)
job = updater.job_queue

db = sqlite3.connect("database.db")
cursor = db.cursor()
db_lis = cursor.execute("SELECT link from schedule")
links = []
for i in db_lis:
    links.append(f"Link for the Class\n{i[0]}")


cl_1 = datetime.time(hour=8, minute=58, second=00,tzinfo=pytz.timezone('Asia/Kolkata'))
cl_2 = datetime.time(hour=14, minute=5, second=00,tzinfo=pytz.timezone('Asia/Kolkata'))
cl_3 = datetime.time(hour=13, minute=58, second=00,tzinfo=pytz.timezone('Asia/Kolkata'))


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1090783297', text=links[0])


job_daily = job.run_daily(func, days=(0,0), time=cl_1)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1090783297', text=links[1])


job_daily = job.run_daily(func, days=(0,0), time=cl_2)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1090783297', text=links[2])


job_daily = job.run_daily(func, days=(0,0), time=cl_3)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1090783297', text=links[3])


job_daily = job.run_daily(func, days=(1,1), time=cl_1)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1090783297', text=links[4])


job_daily = job.run_daily(func, days=(1,1), time=cl_2)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1090783297', text=links[5])


job_daily = job.run_daily(func, days=(2,2), time=cl_1)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1090783297', text=links[6])


job_daily = job.run_daily(func, days=(2,2), time=cl_2)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1090783297', text=links[7])


job_daily = job.run_daily(func, days=(3,3), time=cl_1)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1090783297', text=links[8])

job_daily = job.run_daily(func, days=(3,3), time=cl_2)

def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1090783297', text=links[9])

job_daily = job.run_daily(func, days=(4,4), time=cl_1)

def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1090783297', text=links[10])

job_daily = job.run_daily(func, days=(4,4), time=cl_2)

updater.start_polling()
updater.idle()



