import telebot
import google.generativeai as genai

# المعلومات اللي استعملناها قبل شوية
TOKEN = '8436162247:AAHbi-1kc57Itj3efmFaTdqkCaCdMs7-YYE'
GOOGLE_AI_KEY = 'AIzaSyDeYBjZ_bJLhEGjxh_1FfgKTrDQDRLKzrg'

# إعداد عقل جوجل
genai.configure(api_key=GOOGLE_AI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: True)
def ai_chat(message):
    try:
        # لوزة تفكر وتكتب
        bot.send_chat_action(message.chat.id, 'typing')
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        print(f"Error: {e}")

# تشغيل البوت للأبد
print("لوزة العبقرية اشتغلت على ريندر..")
bot.infinity_polling()
