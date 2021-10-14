import telegram.ext
from telegram.ext import Updater, CommandHandler
from creater import Scheduler

updater = Updater('2047279107:AAEyhyeOpA76bNa4PH5xFX7Xjdhof0RxZXE', use_context=True)
job = updater.job_queue
dispatcher = updater.dispatcher

def start(update, context):
    message = 'Welcome to the bot'
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

sarathy = Scheduler('1090783297', ['jan', 'ui', 'a', 'met', 'pd', 'ang', 'jan', 'pd', 'met', 'ang', 'ui'])
job = sarathy.launch(job)

gowtham = Scheduler('967948229',['abi', 'ui', 'a', 'met', 'pd', 'ang', 'abi', 'pd', 'met', 'ang', 'ui'])
job = gowtham.launch(job)

dharu = Scheduler('1079579102',['abi', 'ui', 'a', 'met', 'pd', 'ang', 'abi', 'pd', 'met', 'ang', 'ui'])
job = dharu.launch(job)

viswa = Scheduler('1054397493',['abi', 'nlp', 'b', 'met', 'pd', 'ang', 'abi', 'pd', 'met', 'ang', 'nlp'])
job = viswa.launch(job)

murali = Scheduler('983782432',['jan', 'ui', 'a', 'moh', 'ac', 'ang', 'jan', 'ac', 'moh', 'ang', 'ui'])
job = murali.launch(job)

girish = Scheduler('1126599389',['abi', 'nlp', 'a', 'moh', 'pd', 'ang', 'abi', 'pd', 'moh', 'ang', 'nlp'])
job = girish.launch(job)

updater.start_polling()
updater.idle()
