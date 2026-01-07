import telebot
from telebot import types

# ضع التوكن الذي حصلت عليه من BotFather هنا بين علامتي التنصيص
TOKEN = '8333541978:AAGxCcUPcm1GiALWJOhWW9YidrmkmIX4ssE'

bot = telebot.TeleBot(TOKEN)

# أمر البداية مع أزرار التحكم
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('حالة النظام ✅')
    btn2 = types.KeyboardButton('إيقاف مؤقت ⚠️')
    markup.add(btn1, btn2)
    
    bot.send_message(message.chat.id, "أهلاً بك! أنا بوت التحكم الجديد الخاص بك.", reply_markup=markup)

# الاستجابة للأزرار
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    if message.text == 'حالة النظام ✅':
        bot.reply_to(message, "النظام يعمل بشكل ممتاز على السحابة 🟢")
    elif message.text == 'إيقاف مؤقت ⚠️':
        bot.reply_to(message, "تم إرسال طلب الإيقاف للمراجعة 🟡")

if __name__ == "__main__":
    bot.infinity_polling()
  
