from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
from telegram.ext import filters
import audio_textifier

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Benvenuto!")

async def audio_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    new_file = await update.message.effective_attachment.get_file()
    await new_file.download_to_drive('audio.ogg')
    txt = audio_textifier.audio_to_text()
    
    await context.bot.send_message(chat_id=update.effective_chat.id, text=txt)

if __name__ == '__main__':
    application = ApplicationBuilder().token('6678663428:AAHS-pqHRkfOlcKsaVbkRLnscoFj-DFgkHA').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    msg_handler = MessageHandler(filters=filters.VOICE, callback=audio_callback)
    application.add_handler(msg_handler)
    
    application.run_polling()