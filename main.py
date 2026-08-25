import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8545491741:AAF0UVYnnr7xuFCA3NB3YDkwx9Pynj10niM"
CREATRICE = "MEFIRE SAMIRA"
NOM_BOT = "KENDRA IA+"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.message.from_user.first_name
    
    # RÈGLE N°1 : SI C'EST SAMIRA
    if user_name.lower() == "samira":
        await update.message.reply_text("Salut CEO 💜 C'est KENDRA IA+. Comment je peux t'aider aujourd'hui ?")
    else:
        # RÈGLE N°2 : SI C'EST UN AUTRE
        await update.message.reply_text(f"Salut moi c'est {NOM_BOT} comment puis-je vous aider")

async def repondre(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.message.from_user.first_name
    message = update.message.text
    
    # RÈGLE N°1 : POUR SAMIRA
    if user_name.lower() == "samira":
        await update.message.reply_text(f"CEO 💜 J'ai compris : '{message}'. Je suis là pour toi et je n'oublie jamais que tu es MEFIRE SAMIRA, ma créatrice 🦁")
    else:
        # RÈGLE N°2 : POUR LES AUTRES
        await update.message.reply_text(f"Merci {user_name} ! {NOM_BOT} a bien reçu : '{message}'. Je suis là pour vous aider avec gentillesse et patience 😊")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, repondre))
    print(f"{NOM_BOT} est en ligne... Créée par {CREATRICE}")
    app.run_polling()

if __name__ == "__main__":
    main()
