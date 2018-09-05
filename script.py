from telegram.ext import Updater, CommandHandler,Filters,MessageHandler


def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def introduce(bot, update):
    update.message.reply_text(
        'Hello {}, Introduce yourself with your Branch, Year, what you know and what you expect :-) '.format(update.message.from_user.first_name))

def whoarewe(bot,update):
	update.message.reply_text(
		'We? Prince and Harsh are CSE Final Year Students! ping prince @prncvrm | harsh @harshgarg1812')
def _help(bot,update):
	update.message.reply_text(
		'/hello : Say Hello to Bot!\n/introduce : Introduce yourself\n/whoarewe : Know about us!')

updater = Updater('683229425:AAEqxQ_723_Dn4SNL9wbhLHt_0jRR7mnHXY')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('whoarewe', whoarewe))
updater.dispatcher.add_handler(CommandHandler('introduce', introduce))
updater.dispatcher.add_handler(CommandHandler('help', _help))
updater.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members,introduce))
updater.start_polling()
updater.idle()