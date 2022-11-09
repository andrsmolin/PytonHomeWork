import controller as c
import view as v
import modul_use_telefone_book as m_u_tb
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

my_token = "token"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(v.start())


async def read(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Введите фамилию (для возврата в основное меню - /start):')
    # return (MessageHandler(filters.TEXT, input))
    app.add_handler(MessageHandler(filters.TEXT, input))
    # def read():
#     #     await update.message.reply_text(f'Введите фамилию (для возврата в основное меню - /start):')
#     app.add_handler(MessageHandler(filters.TEXT, input))


async def read2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Введите фамилию, имя, номер телефона и должность (для возврата в основное меню - /start)')
    app.add_handler(MessageHandler(filters.TEXT, create))

    return


async def read3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for i in range(0, 1):
        await update.message.reply_text(f'Введите id (для возврата в основное меню - /start)')
        app.add_handler(MessageHandler(filters.TEXT, delete))
    # delete()
    return


async def input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.lower()
    tel_dect = m_u_tb.return_data()
    count = 0
    for i in range(1, len(tel_dect)+1):
        if tel_dect[i]['surname'].lower().find(msg) >= 0:
            await update.message.reply_text(f'{tel_dect[i]}')
            count += 1
    else:
        if count == 0:
            await update.message.reply_text(f'Контакт не найден')
        await update.message.reply_text(f'Выйти в основное меню? /start \n продолжить поиск (введите фамилию):')
    app = ApplicationBuilder().token(my_token).build()
    return


async def create(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tel_dect = m_u_tb.return_data()
    new_cont = update.message.text.split()
    if len(new_cont) < 4:
        new_cont = ''
        return
    surname = new_cont[0]
    name = new_cont[1]
    number_person = new_cont[2]
    status = new_cont[3]
    i = len(tel_dect)+1
    tel_dect[i] = {'idd': i, 'surname': surname, 'name': name,
                   'telefon': number_person, 'status': status}
    m_u_tb.exp_dect(tel_dect)
    await update.message.reply_text(f'{tel_dect[i]} \n /start')


async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    idd = update.message.text
    tel_dect = m_u_tb.return_data()
    if idd.isdigit() and 0 < int(idd) <= len(tel_dect):
        tel_dect[int(idd)] = {'idd': idd, 'surname': 'delete',
                              'name': 'delete', 'telefon': '_', 'status': '_'}
        m_u_tb.exp_dect(tel_dect)
    else:
        await update.message.reply_text('повторите ввод')
        return


def rest():
    app = ApplicationBuilder().token(my_token).build()


app = ApplicationBuilder().token(my_token).build()

# app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("start", start))
# app.add_handler(MessageHandler(filters.TEXT, create))
# app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
app.add_handler(CommandHandler("1", read))
app.add_handler(CommandHandler("2", read2))
app.add_handler(CommandHandler("3", read3))
# app.add_handler(CommandHandler("4", start))


app.run_polling()
msg = "0"
# s = ""
