import telebot

bot = telebot.TeleBot("6131766405:AAEqQcVZ6WsJ6BvvXbOCb--VtVmoKhz7rRE")
gratitude_db = "gratitude_db.txt"

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "привіт! цей бот був створений сквером щоб підняти йому щастяю. команди: /thank_for - записує подяку, /send_txt - надсилає журнал подяк")
  
@bot.message_handler(commands=['thank_for'])
def thank_to(message):
    words = message.text.split()[1:]
    if words:
        gratitude = " ".join(words)
        with open(gratitude_db, 'a') as f:
          f.write(f"\n\n{gratitude}")
        bot.reply_to(message, f"{gratitude} was added to gratitude journal")
    else:
        bot.reply_to(message, "Please provide a name or phrase as an argument.")

@bot.message_handler(commands=['send_txt'])
def send_txt_file_content(m):
    chat_id = m.chat.id
    file_path = gratitude_db

    with open(file_path, 'r') as file:
        content = file.read()
    
    # Split the text each 3000 characters
    splitted_text = telebot.util.split_string(content, 3000)
    for text in splitted_text:
        bot.send_message(chat_id, text)


bot.infinity_polling()