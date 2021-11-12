
def notify():
   bot.send_message(TG_CHAT_ID, message)
   
def choose(TG_CHAT_ID, question):
    bot.create_timer(parse(question), notify)
bot.reply_on_message(choose)
bot.run_bot()
