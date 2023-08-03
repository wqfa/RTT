import random
import string
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

# توليد ايميل عشوائي من 10 أحرف
def generate_random_email():
    characters = string.ascii_lowercase + string.digits
    email = ''.join(random.choices(characters, k=10)) + "@gmail.com"
    return email

# توليد كلمة مرور عشوائية من 8 أحرف
def generate_random_password():
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choices(characters, k=8))
    return password

# معالجة الرسائل الواردة للبوت
def handle_message(msg):
    if 'chat' not in msg or 'text' not in msg:
        # تجاهل الرسائل الغير صالحة
        return

    chat_id = msg['chat']['id']
    command = msg['text']

    if command == '/start':
        user_name = msg['chat']['first_name']
        welcome_message = f"اهلاً {user_name} انا بوت اعطيك حسابات بيس شغالة قم بـ ارسال /get للحصول ع الحسابات "
        join_channel_button = InlineKeyboardButton(text='انضم بقناتي أولاً', url="https://t.me/C35CS")
        program_button = InlineKeyboardButton(text='Dex 𓏺 ҂ .', url="https://t.me/C15CS")
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[join_channel_button], [program_button]])
        bot.sendMessage(chat_id, welcome_message, reply_markup=keyboard)
    elif command == '/get':
        email = generate_random_email()
        password = generate_random_password()
        message = f"""𝐍𝐞𝐰 ➥•𝐋𝐨𝐠𝐢𝐧 : PES ربـط كونامي
❅─────✧❅✦❅✧──────❅
👤 ➥•𝑬𝒎𝒂𝒊𝒍 :  {email}
📟➥•𝑷𝒂𝒔𝒔𝒘𝒐𝒓𝒅 : {password}
❅─────✧❅✦❅✧──────❅
👤➥【@DevEviI & @C35CS  """
        bot.sendMessage(chat_id, message)
    elif command == '/Dev':
        about_me_message = "↫تفضل وياك دكس @C15CS 🤖 ."
        bot.sendMessage(chat_id, about_me_message)

# استبدال 'YOUR_BOT_TOKEN' بتوكن البوت الخاص بك
bot = telepot.Bot('6461815132:AAHmaHxzxV_DumfiIH2eI38o1ArOO_riXDY')
MessageLoop(bot, handle_message).run_as_thread()

print("Listening for messages...")
while True:
    pass
  
