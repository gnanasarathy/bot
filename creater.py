import telegram.ext
from telegram.ext import Updater, CommandHandler
import datetime
import pytz
import sqlite3

db = sqlite3.connect("database.db")
cursor = db.cursor()
r = list(cursor.execute("SELECT * FROM schedule"))
links_dict = {}
st = "Link for the Class\n"
for i in r:
    links_dict[i[0]] = st + i[1]

class Scheduler():
    def __init__(self, user_id, staff):
        self.user_id = user_id
        subject = ['ds1', 'el1', 'lab', 'cs1', 'ci1', 'pcv1', 'ds2', 'ci2', 'cs2', 'pcv2', 'el2']
        self.user_key = [subject[j] + '_' + staff[j] for j in range(len(subject))]
        self.cl_1 = datetime.time(hour=8, minute=58, second=00, tzinfo=pytz.timezone('Asia/Kolkata'))
        self.cl_2 = datetime.time(hour=10, minute=58, second=00, tzinfo=pytz.timezone('Asia/Kolkata'))
        self.cl_3 = datetime.time(hour=13, minute=58, second=00, tzinfo=pytz.timezone('Asia/Kolkata'))

    def period1(self, context: telegram.ext.CallbackContext):
        context.bot.send_message(chat_id=self.user_id, text=links_dict[self.user_key[0]])

    def period2(self, context: telegram.ext.CallbackContext):
        context.bot.send_message(chat_id=self.user_id, text=links_dict[self.user_key[1]])

    def period3(self, context: telegram.ext.CallbackContext):
        context.bot.send_message(chat_id=self.user_id, text=links_dict[self.user_key[2]])

    def period4(self, context: telegram.ext.CallbackContext):
        context.bot.send_message(chat_id=self.user_id, text=links_dict[self.user_key[3]])

    def period5(self, context: telegram.ext.CallbackContext):
        context.bot.send_message(chat_id=self.user_id, text=links_dict[self.user_key[4]])

    def period6(self, context: telegram.ext.CallbackContext):
        context.bot.send_message(chat_id=self.user_id, text=links_dict[self.user_key[5]])

    def period7(self, context: telegram.ext.CallbackContext):
        context.bot.send_message(chat_id=self.user_id, text=links_dict[self.user_key[6]])

    def period8(self, context: telegram.ext.CallbackContext):
        context.bot.send_message(chat_id=self.user_id, text=links_dict[self.user_key[7]])

    def period9(self, context: telegram.ext.CallbackContext):
        context.bot.send_message(chat_id=self.user_id, text=links_dict[self.user_key[8]])

    def period10(self, context: telegram.ext.CallbackContext):
        context.bot.send_message(chat_id=self.user_id, text=links_dict[self.user_key[9]])

    def period11(self, context: telegram.ext.CallbackContext):
        context.bot.send_message(chat_id=self.user_id, text=links_dict[self.user_key[10]])

    def launch(self, job):
        job.run_daily(self.period1, days=(0, 0), time=self.cl_1)
        job.run_daily(self.period2, days=(0, 0), time=self.cl_2)
        job.run_daily(self.period3, days=(0, 0), time=self.cl_3)
        job.run_daily(self.period4, days=(1, 1), time=self.cl_1)
        job.run_daily(self.period5, days=(1, 1), time=self.cl_2)
        job.run_daily(self.period6, days=(2, 2), time=self.cl_1)
        job.run_daily(self.period7, days=(2, 2), time=self.cl_2)
        job.run_daily(self.period8, days=(3, 3), time=self.cl_1)
        job.run_daily(self.period9, days=(3, 3), time=self.cl_2)
        job.run_daily(self.period10, days=(4, 4), time=self.cl_1)
        job.run_daily(self.period11, days=(4, 4), time=self.cl_2)
        return job
