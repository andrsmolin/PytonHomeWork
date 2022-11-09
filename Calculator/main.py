from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

my_token = "token"


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hi, {update.effective_user.first_name}')


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Введите числа и оператор через пробел \n например, 1 + 2 \n доступные операции:\n +\n -\n *\n /\n ^ (возведение в степень)')


async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    result = 0
    text = update.message.text
    text_1 = text.split()
    print(text_1)
    if len(text_1) != 3:
        return
    a = text_1[0]
    b = text_1[2]
    operator = text_1[1]
    if operator == '+':
        result = int(a) + int(b)
    elif operator == '-':
        result = int(a) - int(b)
    elif operator == '*':
        result = int(a) * int(b)
    elif operator == '/':
        result = int(a) / int(b)
    elif operator == '^':
        result = int(a) ** int(b)
    await update.message.reply_text(f'Ответ: {result}')

app = ApplicationBuilder().token(my_token).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("help", help))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calc))

app.run_polling()
