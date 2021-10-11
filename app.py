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
r = list(cursor.execute("SELECT * FROM schedule"))
links_dict = {}
st = "Link for the Class\n"
for i in r:
    links_dict[i[0]] = st + i[1]

users = ['1090783297', '967948229', '1079579102', '1054397493', '983782432']
subject = ['ds1', 'el1', 'lab', 'cs1', 'ci1', 'pcv1', 'ds2', 'ci2', 'cs2', 'pcv2', 'el2']
staff_list = [['jan', 'ui', 'a', 'met', 'pd', 'ang', 'jan', 'pd', 'met', 'ang', 'ui'],
              ['abi', 'ui', 'a', 'met', 'pd', 'ang', 'abi', 'pd', 'met', 'ang', 'ui'],
              ['abi', 'ui', 'a', 'met', 'pd', 'ang', 'abi', 'pd', 'met', 'ang', 'ui'],
              ['abi', 'nlp', 'b', 'met', 'pd', 'ang', 'abi', 'pd', 'met', 'ang', 'nlp'],
              ['jan', 'ui', 'a', 'moh', 'ac', 'ang', 'jan', 'ac', 'moh', 'ang', 'ui']]

user_dict = {}
for i in range(len(users)):
    user_dict[users[i]] = [subject[j] + '_' + staff_list[i][j] for j in range(len(subject))]


def start(update, context):
    message = 'Welcome to the bot'
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
# give a name to the command and add it to the dispaatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)






cl_1 = datetime.time(hour=8, minute=58, second=00,tzinfo=pytz.timezone('Asia/Kolkata'))
cl_2 = datetime.time(hour=10, minute=58, second=00,tzinfo=pytz.timezone('Asia/Kolkata'))
cl_3 = datetime.time(hour=13, minute=58, second=00,tzinfo=pytz.timezone('Asia/Kolkata'))

cl = [cl_1, cl_2, cl_3]


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1090783297', text=links_dict[user_dict[users[0]][0]])


job_daily = job.run_daily(func, days=(0,0), time=cl_1)

def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1090783297', text=links_dict[user_dict[users[0]][1]])

job_daily = job.run_daily(func, days=(0,0), time=cl_2)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1090783297', text=links_dict[user_dict[users[0]][2]])


job_daily = job.run_daily(func, days=(0,0), time=cl_3)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1090783297', text=links_dict[user_dict[users[0]][3]])


job_daily = job.run_daily(func, days=(1,1), time=cl_1)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1090783297', text=links_dict[user_dict[users[0]][4]])


job_daily = job.run_daily(func, days=(1,1), time=cl_2)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1090783297', text=links_dict[user_dict[users[0]][5]])


job_daily = job.run_daily(func, days=(2,2), time=cl_1)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1090783297', text=links_dict[user_dict[users[0]][6]])


job_daily = job.run_daily(func, days=(2,2), time=cl_2)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1090783297', text=links_dict[user_dict[users[0]][7]])


job_daily = job.run_daily(func, days=(3,3), time=cl_1)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1090783297', text=links_dict[user_dict[users[0]][8]])

job_daily = job.run_daily(func, days=(3,3), time=cl_2)

def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1090783297', text=links_dict[user_dict[users[0]][9]])

job_daily = job.run_daily(func, days=(4,4), time=cl_1)

def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1090783297', text=links_dict[user_dict[users[0]][10]])

job_daily = job.run_daily(func, days=(4,4), time=cl_2)




###
def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='967948229', text=links_dict[user_dict[users[1]][0]])


job_daily = job.run_daily(func, days=(0,0), time=cl_1)

def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='967948229', text=links_dict[user_dict[users[1]][1]])

job_daily = job.run_daily(func, days=(0,0), time=cl_2)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='967948229', text=links_dict[user_dict[users[1]][2]])


job_daily = job.run_daily(func, days=(0,0), time=cl_3)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='967948229', text=links_dict[user_dict[users[1]][3]])


job_daily = job.run_daily(func, days=(1,1), time=cl_1)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='967948229', text=links_dict[user_dict[users[1]][4]])


job_daily = job.run_daily(func, days=(1,1), time=cl_2)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='967948229', text=links_dict[user_dict[users[1]][5]])


job_daily = job.run_daily(func, days=(2,2), time=cl_1)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='967948229', text=links_dict[user_dict[users[1]][6]])


job_daily = job.run_daily(func, days=(2,2), time=cl_2)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='967948229', text=links_dict[user_dict[users[1]][7]])


job_daily = job.run_daily(func, days=(3,3), time=cl_1)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='967948229', text=links_dict[user_dict[users[1]][8]])

job_daily = job.run_daily(func, days=(3,3), time=cl_2)

def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='967948229', text=links_dict[user_dict[users[1]][9]])

job_daily = job.run_daily(func, days=(4,4), time=cl_1)

def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='967948229', text=links_dict[user_dict[users[1]][10]])

job_daily = job.run_daily(func, days=(4,4), time=cl_2)



# ######
def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1079579102', text=links_dict[user_dict[users[2]][0]])


job_daily = job.run_daily(func, days=(0,0), time=cl_1)

def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1079579102', text=links_dict[user_dict[users[2]][1]])

job_daily = job.run_daily(func, days=(0,0), time=cl_2)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1079579102', text=links_dict[user_dict[users[2]][2]])


job_daily = job.run_daily(func, days=(0,0), time=cl_3)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1079579102', text=links_dict[user_dict[users[2]][3]])


job_daily = job.run_daily(func, days=(1,1), time=cl_1)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1079579102', text=links_dict[user_dict[users[2]][4]])


job_daily = job.run_daily(func, days=(1,1), time=cl_2)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1079579102', text=links_dict[user_dict[users[2]][5]])


job_daily = job.run_daily(func, days=(2,2), time=cl_1)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1079579102', text=links_dict[user_dict[users[2]][6]])


job_daily = job.run_daily(func, days=(2,2), time=cl_2)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1079579102', text=links_dict[user_dict[users[2]][7]])


job_daily = job.run_daily(func, days=(3,3), time=cl_1)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1079579102', text=links_dict[user_dict[users[2]][8]])

job_daily = job.run_daily(func, days=(3,3), time=cl_2)

def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1079579102', text=links_dict[user_dict[users[2]][9]])

job_daily = job.run_daily(func, days=(4,4), time=cl_1)

def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1079579102', text=links_dict[user_dict[users[2]][10]])

job_daily = job.run_daily(func, days=(4,4), time=cl_2)




#####

def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1054397493', text=links_dict[user_dict[users[3]][0]])


job_daily = job.run_daily(func, days=(0,0), time=cl_1)

def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1054397493', text=links_dict[user_dict[users[3]][1]])

job_daily = job.run_daily(func, days=(0,0), time=cl_2)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1054397493', text=links_dict[user_dict[users[3]][2]])


job_daily = job.run_daily(func, days=(0,0), time=cl_3)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1054397493', text=links_dict[user_dict[users[3]][3]])


job_daily = job.run_daily(func, days=(1,1), time=cl_1)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1054397493', text=links_dict[user_dict[users[3]][4]])


job_daily = job.run_daily(func, days=(1,1), time=cl_2)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1054397493', text=links_dict[user_dict[users[3]][5]])


job_daily = job.run_daily(func, days=(2,2), time=cl_1)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1054397493', text=links_dict[user_dict[users[3]][6]])


job_daily = job.run_daily(func, days=(2,2), time=cl_2)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1054397493', text=links_dict[user_dict[users[3]][7]])


job_daily = job.run_daily(func, days=(3,3), time=cl_1)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1054397493', text=links_dict[user_dict[users[3]][8]])

job_daily = job.run_daily(func, days=(3,3), time=cl_2)

def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1054397493', text=links_dict[user_dict[users[3]][9]])

job_daily = job.run_daily(func, days=(4,4), time=cl_1)

def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='1054397493', text=links_dict[user_dict[users[3]][10]])

job_daily = job.run_daily(func, days=(4,4), time=cl_2)



# #####

def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='983782432', text=links_dict[user_dict[users[4]][0]])


job_daily = job.run_daily(func, days=(0,0), time=cl_1)

def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='983782432', text=links_dict[user_dict[users[4]][1]])

job_daily = job.run_daily(func, days=(0,0), time=cl_2)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='983782432', text=links_dict[user_dict[users[4]][2]])


job_daily = job.run_daily(func, days=(0,0), time=cl_3)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='983782432', text=links_dict[user_dict[users[4]][3]])


job_daily = job.run_daily(func, days=(1,1), time=cl_1)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='983782432', text=links_dict[user_dict[users[4]][4]])


job_daily = job.run_daily(func, days=(1,1), time=cl_2)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='983782432', text=links_dict[user_dict[users[4]][5]])


job_daily = job.run_daily(func, days=(2,2), time=cl_1)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='983782432', text=links_dict[user_dict[users[4]][6]])


job_daily = job.run_daily(func, days=(2,2), time=cl_2)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='983782432', text=links_dict[user_dict[users[4]][7]])


job_daily = job.run_daily(func, days=(3,3), time=cl_1)


def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='983782432', text=links_dict[user_dict[users[4]][8]])

job_daily = job.run_daily(func, days=(3,3), time=cl_2)

def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='983782432', text=links_dict[user_dict[users[4]][9]])

job_daily = job.run_daily(func, days=(4,4), time=cl_1)

def func(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='983782432', text=links_dict[user_dict[users[4]][10]])

job_daily = job.run_daily(func, days=(4,4), time=cl_2)



updater.start_polling()
updater.idle()
