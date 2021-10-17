import telegram.ext
from telegram.ext import Updater, CommandHandler
import datetime
import pytz
import sqlite3

db = sqlite3.connect("database.db")
cursor = db.cursor()
links_bank = list(cursor.execute("SELECT * FROM schedule"))
links_dict = {i[0]: "Link For the Class\n" + i[1] for i in links_bank}

cl_1 = datetime.time(hour=8, minute=58, second=00, tzinfo=pytz.timezone('Asia/Kolkata'))
cl_2 = datetime.time(hour=10, minute=58, second=00, tzinfo=pytz.timezone('Asia/Kolkata'))
cl_3 = datetime.time(hour=13, minute=58, second=00, tzinfo=pytz.timezone('Asia/Kolkata'))

class PeriodAllloct():
    def __init__(self, user_id, msg):
        self.user_id = user_id
        self.msg = msg

    def period(self, context: telegram.ext.CallbackContext):
        context.bot.send_message(chat_id=self.user_id, text=links_dict[self.msg])


class Scheduler():
    def __init__(self, user_id, staff):
        subject = ['ds1', 'el1', 'lab', 'cs1', 'ci1', 'pcv1', 'ds2', 'ci2', 'cs2', 'pcv2', 'el2']
        self.user_id = user_id
        self.user_key = [subject[j] + '_' + staff[j] for j in range(len(subject))]

    def launch(self, job):
        job.run_daily(PeriodAllloct(self.user_id, self.user_key[0]).period, days=(0, 0), time=cl_1)
        job.run_daily(PeriodAllloct(self.user_id, self.user_key[1]).period, days=(0, 0), time=cl_2)
        job.run_daily(PeriodAllloct(self.user_id, self.user_key[2]).period, days=(0, 0), time=cl_3)
        job.run_daily(PeriodAllloct(self.user_id, self.user_key[3]).period, days=(1, 1), time=cl_1)
        job.run_daily(PeriodAllloct(self.user_id, self.user_key[4]).period, days=(1, 1), time=cl_2)
        job.run_daily(PeriodAllloct(self.user_id, self.user_key[5]).period, days=(2, 2), time=cl_1)
        job.run_daily(PeriodAllloct(self.user_id, self.user_key[6]).period, days=(2, 2), time=cl_2)
        job.run_daily(PeriodAllloct(self.user_id, self.user_key[7]).period, days=(3, 3), time=cl_1)
        job.run_daily(PeriodAllloct(self.user_id, self.user_key[8]).period, days=(3, 3), time=cl_2)
        job.run_daily(PeriodAllloct(self.user_id, self.user_key[9]).period, days=(4, 4), time=cl_1)
        job.run_daily(PeriodAllloct(self.user_id, self.user_key[10]).period, days=(4, 4), time=cl_2)
        return job
