import telebot

# ያገኘኸው አዲሱ Token እዚህ ገብቷል
API_TOKEN = '8668684957:AAE1DSVKsIVM5RhDXJUF8gE8ZMnDaRFk-Zc'
bot = telebot.TeleBot(API_TOKEN)

# የጠቅላላ እውቀት መረጃዎች (እዚህ ጋር የፈለግከውን ጥያቄና መልስ መጨመር ትችላለህ)
knowledge_base = {
    "ኢትዮጵያ": "ኢትዮጵያ በምስራቅ አፍሪካ የምትገኝ፣ የራሷ ፊደልና የቀን አቆጣጠር ያላት ጥንታዊት ሀገር ናት። 🇪🇹",
    "አባይ": "አባይ በዓለም ላይ ረጅሙ ወንዝ ሲሆን፣ መነሻውም ኢትዮጵያ ውስጥ ጣና ሐይቅ ነው። 🌊",
    "ኮምፒውተር": "ኮምፒውተር መረጃዎችን ለመቀበል፣ ለማቀነባበርና ለማከማቸት የሚረዳ ኤሌክትሮኒክ መሣሪያ ነው። 💻",
    "ፀሐይ": "ፀሐይ ለምድር የብርሃንና የሙቀት ምንጭ የሆነች ግዙፍ ኮከብ ናት። ☀️",
    "ጤና": "ጤናማ ለመሆን የተመጣጠነ ምግብ መመገብ፣ ስፖርት መስራትና በቂ እንቅልፍ ማግኘት ያስፈልጋል። 🍎"
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "ሰላም! እኔን ማንኛውንም የጠቅላላ እውቀት ጥያቄ መጠየቅ ትችላለህ። 🧠")

@bot.message_handler(func=lambda message: True)
def answer_anything(message):
    user_query = message.text.strip()
    found = False

    # 1. በዝርዝሩ ውስጥ ካለ መፈለግ
    for key in knowledge_base:
        if key in user_query:
            bot.reply_to(message, knowledge_base[key])
            found = True
            break
    
    # 2. የሒሳብ ስሌት ከሆነ መስራት
    if not found and any(op in user_query for op in ['+', '-', '*', '/']):
        try:
            result = eval(user_query)
            bot.reply_to(message, f"የስሌቱ ውጤት፦ {result} ነው")
            found = True
        except:
            pass

    # 3. መልሱ ካልተገኘ
    if not found:
        bot.reply_to(message, f"ይቅርታ፣ ስለ '{user_query}' እስካሁን መረጃ የለኝም። ግን አጥንቼ እንድነግርህ መዝግቤዋለሁ! ✅")

print("🚀 ቦቱ ሁሉንም ጥያቄዎች ለመመለስ ዝግጁ ነው!")
bot.infinity_polling()
