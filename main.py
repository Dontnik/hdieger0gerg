from pytimeparse import parse
import random
import os
import ptbot

def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)

message = "Осталось секунд:"
 
TG_TOKEN = os.environ['TG_TOKEN']

bot = ptbot.Bot(TG_TOKEN)
 

def notify(TG_CHAT_ID):
   bot.send_message(TG_CHAT_ID, 'Время вышло!')

def notify_progress(secs_left, message_id, TG_CHAT_ID, question):
    bot.update_message(TG_CHAT_ID, message_id, f'Осталось секунд:{secs_left}\n{render_progressbar(parse(question), secs_left)}')
def choose(TG_CHAT_ID, question):
   message_id = bot.send_message(TG_CHAT_ID, message)
   bot.create_countdown(parse(question), notify_progress, message_id=message_id,TG_CHAT_ID=TG_CHAT_ID, question=question)
   bot.create_timer(parse(question), notify, TG_CHAT_ID=TG_CHAT_ID)
bot.reply_on_message(choose)
bot.run_bot()