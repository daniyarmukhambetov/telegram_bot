#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.         
"""
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic inline bot example. Applies different text transformations.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import logging
import time
from uuid import uuid4
from do import do
from datetime import datetime
from threading import Thread
from help import get_main

from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent, Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, CallbackContext, Filters, MessageHandler, ConversationHandler
from telegram.utils.helpers import escape_markdown

def update():
    while True:
        get_main()
        time.sleep(86400)

# Enable logging
gor = 'fishes'

temp = 'https://horo.mail.ru/prediction/{}/today/'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

d = {
    'Овен':'aries',
    'Телец':'taurus',
    'Близнецы':'gemini',
    'Рак':'cancer',
    'Лев':'leo',
    'Дева':'virgo',
    'Весы':'libra',
    'Скорпион':'scorpious',
    'Стрелец':'sagittarius',
    'Козерог':'capricorn',
    'Водолей':'aquarius',
    'Рыбы':'pisces'
}
d1 = {
    'Овен':'aries',
    'Телец':'taurus',
    'Близнецы':'gemini',
    'Рак':'cancer',
    'Лев':'leo',
    'Дева':'virgo',
    'Весы':'libra',
    'Скорпион':'scorpious',
    'Стрелец':'sagittarius',
    'Козерог':'capricorn',
    'Водолей':'aquarius',
    'Рыбы':'pisces'
}
l = [
'овен',
    'телец',
    'близнецы',
    'рак',
    'лев',
    'дева',
    'весы',
    'скорпион',
    'стрелец',
    'козерог',
    'водолей',
    'рыбы'
]
segodnya = ' сегодня'
zavtra = ' завтра'
nedelya = ' неделя'
mesyac = ' месяц'
zhyl = ' год'
# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Привет!')


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def inlinequery(update: Update, context: CallbackContext) -> None:
    """Handle the inline query."""
    query = update.inline_query.query
    print(query + ' inline')        
 


    if query.lower() in l:
            results = [
                InlineQueryResultArticle(
                id=str(uuid4()),
                title=f"{query.lower()} сегодня",
                #f'{do(f'{query.lower()}')
                input_message_content=InputTextMessageContent(
                    do(f'{query.lower() + segodnya}')),
                ),
                InlineQueryResultArticle(
                    id=str(uuid4()),
                    title=f'{query.lower()} завтра',
                    input_message_content=InputTextMessageContent(
                        f'{do(query.lower()+ zavtra)}'
                    ),
                ),
                InlineQueryResultArticle(
                    id=str(uuid4()),
                    title=f'{query.lower()} неделя',
                    input_message_content=InputTextMessageContent(
                        f'{do(query.lower()+ nedelya)}'
                    ),
                ),
                InlineQueryResultArticle(
                    id=str(uuid4()),
                    title=f'{query.lower()} месяц',
                    input_message_content=InputTextMessageContent(
                        f'{do(query.lower()+ mesyac)}'
                    ),
                ),
                InlineQueryResultArticle(
                    id=str(uuid4()),
                    title=f'{query.lower()} год',
                    input_message_content=InputTextMessageContent(
                        f'{do(query.lower()+ zhyl)}'
                    ),
                ),
                # InlineQueryResultArticle(
                #     id=str(uuid4()),
                #     title=f'{query.lower()} характеристика',
                #     input_message_content=InputTextMessageContent(
                #         do(f'{query.lower()}', 'характер')
                #     ),
                # ),
            ]
    else:
        return

    update.inline_query.answer(results)


'*****************************************'
DATE, SEND = range(2)

def send(update: Update, context: CallbackContext):
    text = update.message.text
    file_name = text
    print(file_name)
    # if date.lower == 'сегодня':
    #     date = ''
    update.message.reply_text(
        do(file_name),
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


def date123(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    reply_keyboard = [
        [f'{text} Сегодня', f'{text} Завтра'],
        [f'{text} Неделя', f'{text} Месяц'],
        [f'{text} Год'],
    ]    
    update.message.reply_text(
        'Выбирай!',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=False
        ),
    )
    return SEND

def start(update: Update, context: CallbackContext) -> int:
    """Starts the conversation and asks the user about their gender."""
    reply_keyboard = [
['овен',
    'телец',
    'близнецы'],
    ['рак',
    'лев',
    'дева'],
    ['весы',
    'скорпион',
    'стрелец'],
    ['козерог',
    'водолей',
    'рыбы']
]

    update.message.reply_text(
        'Привет! Я бот гороскоп и помогу тебе с предсказаниями!',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=False, input_field_placeholder='Выбери знак зодиака!'
        ),
    )
    return DATE
    


def cancel(update: Update, context: CallbackContext) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'Bye! I hope we can talk again some day.', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END

def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    cur_time = str(datetime.now().time())
    print(cur_time)

    updater = Updater("1843783243:AAE81UBulb6UnSZ_zDZHvXqOiWfhRqpQop8")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    # on different commands - answer in Telegram
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)], 
        states = {
        DATE : [MessageHandler(Filters.text & ~Filters.command, date123)],
        SEND : [MessageHandler(Filters.text & ~Filters.command, send)]

    },
        fallbacks=[CommandHandler('cancel', cancel)],    
    )

    dispatcher.add_handler(conv_handler)

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(InlineQueryHandler(inlinequery))

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

def bot():

    th1 = Thread(target=update, args=())
    th2 = Thread(target=main, args=())
    th1.start()
    time.sleep(100)
    th2.start()

if __name__ == "__main__":
    main()