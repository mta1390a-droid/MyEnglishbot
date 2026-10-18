# -*- coding: utf-8 -*-
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# ✅ توکن ربات
TOKEN = "8583951782:AAFPczZtUNffaaPTGMl4CeON1WDkPeJzwe4"

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# ==========================================
# 📚 دیتای کامل دروس (لغات و گرامر)
# ==========================================
LESSONS = {
    "1": {
        "title": "درس ۱: Personality | شخصیت",
        "vocab": (
            "📖 <b>جزوه جامع لغات درس ۱</b>\n"
            "➖➖➖➖➖➖➖➖➖➖➖➖\n"
            "💬 <b>مکالمه:</b>\n"
            "• <b>Who is your best friend?</b> (بهترین دوستت کیه؟)\n"
            "• <b>What's he like?</b> (او چه شخصیتی داره؟)\n"
            "• <b>He's clever and kind.</b> (او باهوش و مهربانه.)\n\n"
            "🔹 <b>صفات شخصیتی:</b>\n"
            "• <b>Clever</b>: باهوش\n• <b>Kind</b>: مهربان\n• <b>Hard-working</b>: سخت‌کوش\n"
            "• <b>Helpful</b>: کمک‌کننده\n• <b>Talkative</b>: پرحرف\n• <b>Neat</b>: تمیز و مرتب\n"
            "• <b>Upset</b>: ناراحت\n• <b>Funny</b>: بامزه\n• <b>Patient</b>: صبور\n"
            "• <b>Quiet</b>: ساکت / کم‌حرف\n• <b>Serious</b>: جدی\n• <b>Angry</b>: عصبانی\n"
            "• <b>Brave</b>: شجاع\n• <b>Careless</b>: بی‌دقت\n• <b>Cruel</b>: بی‌رحم\n"
            "• <b>Rude</b>: بی‌ادب\n• <b>Nervous</b>: مضطرب\n• <b>Selfish</b>: خودخواه\n"
            "• <b>Lazy</b>: تنبل\n• <b>Shy</b>: خجالتی\n• <b>Generous</b>: بخشنده"
        ),
        "grammar": (
            "📝 <b>جزوه جامع گرامر درس ۱</b>\n"
            "➖➖➖➖➖➖➖➖➖➖➖➖\n"
            "🔹 <b>۱. فعل to be (بودن):</b>\n"
            "• I <b>am</b> (I'm) / He/She/It <b>is</b> (He's...)\n"
            "• We/You/They <b>are</b> (We're...)\n\n"
            "🔹 <b>۲. سوالی کردن:</b>\n"
            "• <b>Are</b> you hard-working? -> Yes, I am.\n"
            "• <b>Is</b> he clever? -> No, he isn't.\n\n"
            "🔹 <b>۳. منفی کردن:</b>\n"
            "• I <b>am not</b> talkative.\n• He <b>is not</b> (isn't) shy.\n\n"
            "🔹 <b>۴. ساختار There is / There are:</b>\n"
            "• <b>There is</b> an eraser. (مفرد)\n• <b>There are</b> many students. (جمع)"
        )
    },
    "2": {
        "title": "درس ۲: Travel | سفر",
        "vocab": (
            "📖 <b>جزوه جامع لغات درس ۲</b>\n"
            "➖➖➖➖➖➖➖➖➖➖➖➖\n"
            "💬 <b>مکالمه:</b>\n"
            "• <b>I have a reservation here.</b> (من اینجا رزرو دارم.)\n"
            "• <b>Are you staying here?</b> (آیا اینجا می‌مانید؟)\n"
            "• <b>Hope you enjoy your stay.</b> (امیدوارم لذت ببرید.)\n\n"
            "🔹 <b>لغات سفر:</b>\n"
            "• <b>Buy a ticket</b>: بلیط خریدن\n• <b>Check the passport</b>: چک پاسپورت\n"
            "• <b>Check in</b>: ثبت‌نام کردن\n• <b>Check the timetable</b>: چک جدول زمانی\n"
            "• <b>Take off</b>: بلند شدن هواپیما\n• <b>Land</b>: فرود آمدن هواپیما\n"
            "• <b>Book a hotel</b>: هتل رزرو کردن\n• <b>Fill out a form</b>: پر کردن فرم\n"
            "• <b>Pack for a trip</b>: بار بستن\n• <b>Talk to a receptionist</b>: صحبت با پذیرش\n"
            "• <b>Weigh the baggage</b>: وزن کردن بار\n• <b>Baggage reclaim</b>: تحویل بار\n"
            "• <b>Board the plane</b>: سوار هواپیما شدن\n• <b>Make a voyage</b>: سفر دریایی کردن\n"
            "• <b>Take an express train</b>: سوار قطار سریع‌السیر شدن\n• <b>Pay toll</b>: پرداخت عوارض\n"
            "• <b>Exchange money</b>: تبدیل پول"
        ),
        "grammar": (
            "📝 <b>جزوه جامع گرامر درس ۲</b>\n"
            "➖➖➖➖➖➖➖➖➖➖➖➖\n"
            "🔹 <b>حال استمراری (Present Continuous):</b>\n"
            "برای کارهایی که همین الان در حال انجام است.\n"
            "ساختار: <b>am/is/are + فعل + ing</b>\n\n"
            "🔹 <b>مثال:</b>\n"
            "• I <b>am speaking</b> English.\n"
            "• He <b>is buying</b> a ticket.\n"
            "• They <b>are traveling</b>.\n\n"
            "🔹 <b>سوالی:</b> <b>Are</b> you <b>visiting</b> Tehran?\n"
            "🔹 <b>منفی:</b> I <b>am not</b> speaking Persian.\n\n"
            "🔹 <b>سوالات Wh:</b>\n"
            "• <b>Who is</b> speaking English?\n• <b>What is</b> he doing?\n"
            "• <b>Where is</b> Ali going?\n• <b>How are</b> they traveling?"
        )
    },
    "3": {
        "title": "درس ۳: Festivals | جشن‌ها",
        "vocab": (
            "📖 <b>جزوه جامع لغات درس ۳</b>\n"
            "➖➖➖➖➖➖➖➖➖➖➖➖\n"
            "💬 <b>مکالمه:</b>\n"
            "• <b>Do you get New Year gifts too?</b> (آیا هدیه سال نو می‌گیری؟)\n"
            "• <b>Does your grandmother cook the meal?</b> (آیا مادربزرگت غذا می‌پزد؟)\n"
            "• <b>Actually, she doesn't.</b> (در واقع، او نمی‌پزد.)\n\n"
            "🔹 <b>لغات جشن‌ها:</b>\n"
            "• <b>Make lunch/dinner</b>: ناهار/شام درست کردن\n• <b>Bake a cake</b>: کیک پختن\n"
            "• <b>Set the table</b>: چیدن میز\n• <b>Sing the national anthem</b>: سرود ملی خواندن\n"
            "• <b>Hold a ceremony</b>: مراسم برگزار کردن\n• <b>Clear the table</b>: جمع کردن میز\n"
            "• <b>Commemorate martyrs</b>: یادبود شهدا\n• <b>Islamic-Iranian culture</b>: فرهنگ اسلامی-ایرانی\n"
            "• <b>Islamic revolution anniversary</b>: سالگرد انقلاب اسلامی"
        ),
        "grammar": (
            "📝 <b>جزوه جامع گرامر درس ۳</b>\n"
            "➖➖➖➖➖➖➖➖➖➖➖➖\n"
            "🔹 <b>حال ساده (Present Simple):</b>\n"
            "برای عادت‌ها و کارهای روزمره.\n"
            "• با I, You, We, They فعل ساده است: I <b>like</b> spring.\n"
            "• با He, She, It فعل s/es می‌گیرد: He <b>likes</b> spring.\n\n"
            "🔹 <b>سوالی:</b>\n"
            "• <b>Do</b> you buy new clothes? -> Yes, I do.\n"
            "• <b>Does</b> she cook lunch? -> No, she doesn't.\n"
            "⚠️ <b>نکته طلایی:</b> بعد از Does، فعل ساده می‌شود (بدون s).\n\n"
            "🔹 <b>منفی:</b> I <b>don't</b> buy / He <b>doesn't</b> buy.\n\n"
            "🔹 <b>صفات ملکی:</b>\n"
            "• my (مال من) / your (مال تو) / his (مال او) / her (مال او)\n"
            "• its (مال آن) / our (مال ما) / their (مال آنها)"
        )
    },
    "4": {
        "title": "درس ۴: Services | خدمات",
        "vocab": (
            "📖 <b>جزوه جامع لغات درس ۴</b>\n"
            "➖➖➖➖➖➖➖➖➖➖➖➖\n"
            "💬 <b>مکالمه:</b>\n"
            "• <b>Can you help me please?</b> (می‌توانید کمکم کنید؟)\n"
            "• <b>What time does it open?</b> (چه ساعتی باز می‌شود؟)\n"
            "• <b>It opens at 8.</b> (ساعت ۸ باز می‌شود.)\n\n"
            "🔹 <b>لغات خدمات:</b>\n"
            "• <b>Open an account</b>: حساب باز کردن\n• <b>Take out money (ATM)</b>: برداشت پول\n"
            "• <b>Put out fire</b>: آتش را خاموش کردن\n• <b>Hire a taxi</b>: تاکسی گرفتن\n"
            "• <b>Get on a bus</b>: سوار اتوبوس شدن\n• <b>Get off a bus</b>: پیاده شدن از اتوبوس\n"
            "• <b>Send an e-mail</b>: ایمیل فرستادن\n• <b>Recharge the E-ticket</b>: شارژ بلیط\n"
            "• <b>Ask the information desk</b>: پرسیدن از میز اطلاعات\n• <b>Call the emergency (115)</b>: تماس با اورژانس"
        ),
        "grammar": (
            "📝 <b>جزوه جامع گرامر درس ۴</b>\n"
            "➖➖➖➖➖➖➖➖➖➖➖➖\n"
            "🔹 <b>سوالات Wh (Wh Questions):</b>\n"
            "• <b>What</b>: چه (What is that?)\n• <b>Where</b>: کجا (Where do you live?)\n"
            "• <b>When</b>: چه زمانی (When does she wake up?)\n• <b>Who</b>: چه کسی (Who is your best friend?)\n"
            "• <b>Why</b>: چرا (Why do you need help?)\n• <b>How</b>: چطور (How do you come to school?)\n\n"
            "🔹 <b>قیدهای تکرار:</b> (قبل از فعل اصلی می‌آیند)\n"
            "• <b>Always</b>: همیشه (100%)\n• <b>Usually</b>: معمولاً\n• <b>Often</b>: اغلب\n"
            "• <b>Sometimes</b>: گاهی\n• <b>Never</b>: هرگز (0%)\n"
            "مثال: We are <b>sometimes</b> busy. / She <b>always</b> studies hard."
        )
    },
    "5": {
        "title": "درس ۵: Media | رسانه",
        "vocab": (
            "📖 <b>جزوه جامع لغات درس ۵</b>\n"
            "➖➖➖➖➖➖➖➖➖➖➖➖\n"
            "💬 <b>مکالمه:</b>\n"
            "• <b>Did you enjoy your weekend?</b> (آخر هفته خوبی داشتی؟)\n"
            "• <b>I attended Fajr Film Festival.</b> (در جشنواره فیلم فجر شرکت کردم.)\n"
            "• <b>Could you please give me the address?</b> (می‌شود آدرس را بدهید؟)\n\n"
            "🔹 <b>لغات رسانه:</b>\n"
            "• <b>Text a message</b>: پیام دادن\n• <b>Interview somebody</b>: مصاحبه با کسی\n"
            "• <b>Receive an e-mail</b>: دریافت ایمیل\n• <b>Update a blog</b>: آپدیت وبلاگ\n"
            "• <b>Participate in an online course</b>: شرکت در دوره آنلاین\n"
            "• <b>Connect to the Internet</b>: وصل شدن به اینترنت\n"
            "• <b>See a war movie</b>: دیدن فیلم جنگی\n• <b>Change the TV channels</b>: تغییر کانال‌ها\n"
            "• <b>Install an antivirus program</b>: نصب آنتی‌ویروس"
        ),
        "grammar": (
            "📝 <b>جزوه جامع گرامر درس ۵</b>\n"
            "➖➖➖➖➖➖➖➖➖➖➖➖\n"
            "🔹 <b>گذشته ساده (Past Simple):</b>\n"
            "افعال باقاعده (با ed):\n"
            "• watch → watched / listen → listened / connect → connected\n"
            "مثال: They <b>watched</b> a movie.\n\n"
            "🔹 <b>افعال بی‌قاعده:</b>\n"
            "• go → went / have → had / see → saw\n\n"
            "🔹 <b>سوالی (با Did):</b>\n"
            "• <b>Did</b> the girls <b>listen</b> to the radio? -> Yes, they did.\n"
            "⚠️ <b>نکته طلایی:</b> بعد از Did، فعل ساده می‌شود.\n\n"
            "🔹 <b>منفی (با didn't):</b>\n"
            "• He <b>didn't work</b> with his computer.\n\n"
            "🔹 <b>سوالات Wh در گذشته:</b>\n"
            "• <b>Who</b> watched the movie? / <b>What</b> did you do?\n"
            "• <b>When</b> did they download? / <b>Where</b> did she connect?\n\n"
            "🔹 <b>گذشته فعل To Be:</b>\n"
            "• I am → I <b>was</b> / He is → He <b>was</b> / They are → They <b>were</b>"
        )
    },
    "6": {
        "title": "درس ۶: Health | سلامتی",
        "vocab": (
            "📖 <b>جزوه جامع لغات درس ۶</b>\n"
            "➖➖➖➖➖➖➖➖➖➖➖➖\n"
            "💬 <b>مکالمه:</b>\n"
            "• <b>Last summer I fell and broke my leg.</b> (تابستان گذشته پایم شکست.)\n"
            "• <b>I twisted my ankle last winter.</b> (مچ پایم پیچ خورد.)\n"
            "• <b>Can you give me some advice?</b> (می‌توانی توصیه کنی؟)\n\n"
            "🔹 <b>لغات سلامتی و آسیب‌ها:</b>\n"
            "• <b>Break his leg</b>: پای او شکست\n• <b>Burn her hand</b>: دستش سوخت\n"
            "• <b>Hit his head on the door</b>: سرش به در خورد\n• <b>It is bleeding</b>: خونریزی می‌کند\n"
            "• <b>It hurts a lot</b>: خیلی درد می‌کند\n• <b>Cut her finger</b>: انگشتش را برید\n"
            "• <b>Hurt my knee</b>: زانویم آسیب دید\n• <b>Take care of her mother</b>: مراقبت از مادرش\n"
            "• <b>He has some bruises</b>: او کبودی دارد\n• <b>He has a black eye</b>: چشمش کبود است\n"
            "• <b>He had a car crash</b>: او تصادف کرد\n• <b>He has a scar</b>: او جای زخم دارد\n"
            "• <b>She had a heart attack</b>: او سکته قلبی کرد\n• <b>He has his leg in a cast</b>: پایش گچ گرفته است"
        ),
        "grammar": (
            "📝 <b>جزوه جامع گرامر درس ۶</b>\n"
            "➖➖➖➖➖➖➖➖➖➖➖➖\n"
            "🔹 <b>گذشته افعال بی‌قاعده:</b>\n"
            "• break → broke / fall → fell / have → had / hurt → hurt\n"
            "مثال: Mina <b>had</b> an accident.\n\n"
            "🔹 <b>پرسش با Did:</b>\n"
            "• <b>Did</b> Mina <b>have</b> an accident? -> Yes, she did.\n"
            "• <b>Who</b> had an accident? -> Reza.\n\n"
            "🔹 <b>ضمایر مفعولی (Object Pronouns):</b>\n"
            "به جای اسم مفعول:\n"
            "• I → <b>me</b> / You → <b>you</b> / He → <b>him</b> / She → <b>her</b>\n"
            "• It → <b>it</b> / We → <b>us</b> / They → <b>them</b>\n"
            "مثال: Please give it to <b>me</b>."
        )
    }
}

# 🟢 سوالات آزمون
QUIZZES = {
    "1": [
        ("What does “kind” mean?", ["مهربان", "عصبانی", "بی‌دقت", "پرحرف"], 0, "kind یعنی مهربان."),
        ("Choose the correct sentence.", ["She are kind.", "She is kind.", "She am kind.", "She be kind."], 1, "برای she از is استفاده می‌کنیم."),
        ("What is he like? — He is ____.", ["clever", "yesterday", "at school", "two books"], 0, "clever ویژگی شخصیتی است."),
        ("“Hard-working” means ____.", ["تنبل", "سخت‌کوش", "بی‌ادب", "مضطرب"], 1, "hard-working یعنی سخت‌کوش."),
        ("Choose the correct form: They ____ helpful.", ["is", "am", "are", "be"], 2, "برای they از are استفاده می‌کنیم."),
    ],
    "2": [
        ("A “tourist” is a ____.", ["گردشگر", "معلم", "پرستار", "راننده"], 0, "tourist یعنی گردشگر."),
        ("Choose the correct sentence.", ["They is waiting.", "They are waiting.", "They am waiting.", "They waiting."], 1, "ساختار: are + waiting."),
        ("I ____ visiting a museum.", ["am", "is", "are", "be"], 0, "با I از am استفاده می‌کنیم."),
        ("Which sentence is in the present continuous?", ["She visits her aunt every week.", "She is visiting her aunt now.", "She visited her aunt.", "She can visit her aunt."], 1, "is visiting حال استمراری است."),
        ("Make this sentence negative: “He is travelling.”", ["He not is travelling.", "He isn't travelling.", "He doesn't travelling.", "He aren't travelling."], 1, "منفی is با isn't است."),
    ],
    "3": [
        ("“Fireworks” means ____.", ["آتش‌بازی", "هدیه", "ایستگاه", "تصادف"], 0, "fireworks یعنی آتش‌بازی."),
        ("____ you celebrate Nowruz?", ["Does", "Do", "Is", "Are"], 1, "برای you از Do استفاده می‌کنیم."),
        ("____ she buy new clothes?", ["Do", "Is", "Does", "Are"], 2, "برای she از Does استفاده می‌کنیم."),
        ("Choose the correct sentence.", ["He celebrate the festival.", "He celebrates the festival.", "He celebrating the festival.", "He are celebrate the festival."], 1, "در جمله مثبت برای he به فعل s اضافه می‌شود."),
        ("Short answer: Does Ali visit his relatives? — Yes, ____.", ["he do", "he does", "he is", "he visits"], 1, "پاسخ کوتاه به Does با he does است."),
    ],
    "4": [
        ("“Firefighter” means ____.", ["آتش‌نشان", "گردشگر", "کارمند بانک", "دانش‌آموز"], 0, "firefighter یعنی آتش‌نشان."),
        ("Which question asks about a person's job?", ["Where does he live?", "What does he do?", "When does it open?", "Why are you here?"], 1, "What does he do? برای پرسیدن شغل است."),
        ("“Always” means ____.", ["هرگز", "گاهی", "همیشه", "به‌ندرت"], 2, "always یعنی همیشه."),
        ("Choose the correct question.", ["What time it opens?", "What time does it open?", "What time does open it?", "What time is it open does?"], 1, "ساختار: What time + does + subject + verb."),
        ("“Recharge” means ____.", ["شارژ کردن", "آسیب دیدن", "آتش‌بازی کردن", "مصاحبه کردن"], 0, "recharge یعنی شارژ کردن."),
    ],
    "5": [
        ("“Interview” means ____.", ["مصاحبه", "تعطیلات", "آسیب", "خویشاوند"], 0, "interview یعنی مصاحبه."),
        ("Past form of “watch” is ____.", ["watching", "watches", "watched", "watch"], 2, "گذشته watch برابر watched است."),
        ("____ they listen to the radio?", ["Do", "Does", "Did", "Are"], 2, "برای گذشته از Did استفاده می‌کنیم."),
        ("Choose the correct sentence.", ["She watched a movie yesterday.", "She watch a movie yesterday.", "She did watched a movie.", "She watching a movie yesterday."], 0, "در گذشته ساده، فعل باقاعده watched می‌شود."),
        ("Short answer: Did Ali connect online? — No, ____.", ["he doesn't", "he didn't", "he isn't", "he wasn't"], 1, "پاسخ کوتاه منفی به Did برابر didn't است."),
    ],
    "6": [
        ("“Bruise” means ____.", ["کبودی", "مصاحبه", "آتش‌بازی", "بلیت"], 0, "bruise یعنی کبودی."),
        ("Past form of “have” is ____.", ["haved", "has", "had", "having"], 2, "گذشته have برابر had است."),
        ("Did Mina ____ an accident?", ["had", "has", "have", "having"], 2, "بعد از did فعل ساده می‌آید."),
        ("Which is an object pronoun?", ["she", "they", "her", "we"], 2, "her ضمیر مفعولی است."),
        ("“Do you need help?” means ____.", ["آیا به کمک نیاز داری؟", "کجا زندگی می‌کنی؟", "چه ساعتی باز می‌شود؟", "آیا فیلم دیدی؟"], 0, "Do you need help? یعنی آیا به کمک نیاز داری؟"),
    ],
}

def main_menu():
    rows = [[InlineKeyboardButton(lesson["title"], callback_data=f"lesson:{key}")] for key, lesson in LESSONS.items()]
    return InlineKeyboardMarkup(rows)

def lesson_menu(lesson_id):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📖 جزوه لغات", callback_data=f"vocab:{lesson_id}"), InlineKeyboardButton("📝 جزوه گرامر", callback_data=f"grammar:{lesson_id}")],
        [InlineKeyboardButton("✍️ شروع آزمون", callback_data=f"quiz:{lesson_id}:0")],
        [InlineKeyboardButton("🏠 فهرست درس‌ها", callback_data="home")],
    ])

def quiz_keyboard(lesson_id, question_index):
    options = QUIZZES[lesson_id][question_index][1]
    rows = []
    for i in range(0, len(options), 2):
        row = [InlineKeyboardButton(options[j], callback_data=f"answer:{lesson_id}:{question_index}:{j}") for j in range(i, min(i + 2, len(options)))]
        rows.append(row)
    return InlineKeyboardMarkup(rows)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! 👋 به ربات آموزش زبان انگلیسی پایه نهم خوش آمدی.\nیک درس را انتخاب کن:", reply_markup=main_menu())

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "home":
        await query.message.reply_text("📚 فهرست درس‌های زبان انگلیسی پایه نهم:\nیک درس را انتخاب کن.", reply_markup=main_menu())
        return

    parts = data.split(":")
    action = parts[0]

    if action == "lesson":
        lesson_id = parts[1]
        await query.message.reply_text(f"📚 شما درس <b>{LESSONS[lesson_id]['title']}</b> را انتخاب کردید.\n\nمی‌خواهید چه کار کنید؟", parse_mode="HTML", reply_markup=lesson_menu(lesson_id))

    elif action == "vocab":
        lesson_id = parts[1]
        await query.message.reply_text(LESSONS[lesson_id]["vocab"], parse_mode="HTML", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ برگشت به درس", callback_data=f"lesson:{lesson_id}")]]))

    elif action == "grammar":
        lesson_id = parts[1]
        await query.message.reply_text(LESSONS[lesson_id]["grammar"], parse_mode="HTML", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ برگشت به درس", callback_data=f"lesson:{lesson_id}")]]))

    elif action == "quiz":
        lesson_id = parts[1]
        question_index = int(parts[2])
        context.user_data[f"quiz_{lesson_id}"] = {"score": 0, "question": 0}
        q_text = QUIZZES[lesson_id][question_index][0]
        prefix = f"📝 <b>آزمون {LESSONS[lesson_id]['title']}</b>\nسؤال {question_index + 1} از {len(QUIZZES[lesson_id])}\n\n"
        await query.message.reply_text(prefix + q_text, parse_mode="HTML", reply_markup=quiz_keyboard(lesson_id, question_index))

    elif action == "answer":
        lesson_id = parts[1]
        question_index = int(parts[2])
        selected = int(parts[3])
        await handle_answer(query, context, lesson_id, question_index, selected)

async def handle_answer(query, context, lesson_id, question_index, selected):
    q_data = QUIZZES[lesson_id][question_index]
    options, correct, explanation = q_data[1], q_data[2], q_data[3]
    key = f"quiz_{lesson_id}"
    state = context.user_data.get(key)
    
    if not state or state.get("question") != question_index:
        await query.answer("این سؤال قبلاً پاسخ داده شده است.", show_alert=True)
        return

    if selected == correct:
        state["score"] += 1
        result = "✅ آفرین! پاسخ درست است."
    else:
        result = f"❌ پاسخ درست نبود. جواب صحیح: {options[correct]}"

    state["question"] = question_index + 1
    feedback = f"{result}\n💡 {explanation}"

    if question_index + 1 < len(QUIZZES[lesson_id]):
        await query.edit_message_text(feedback, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("➡️ سؤال بعدی", callback_data=f"next:{lesson_id}:{question_index + 1}")]]))
    else:
        score = state["score"]
        total = len(QUIZZES[lesson_id])
        percent = round(score / total * 100)
        context.user_data.pop(key, None)
        await query.edit_message_text(f"{feedback}\n\n🏁 <b>آزمون تمام شد!</b>\nنتیجه: <b>{score} از {total}</b> ({percent}٪)", parse_mode="HTML", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔁 تکرار آزمون", callback_data=f"quiz:{lesson_id}:0")], [InlineKeyboardButton("🏠 فهرست درس‌ها", callback_data="home")]]))

async def next_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    _, lesson_id, question_index = query.data.split(":")
    question_index = int(question_index)
    state = context.user_data.get(f"quiz_{lesson_id}")
    
    if not state or state.get("question") != question_index:
        await query.answer("برای ادامه، آزمون را از ابتدا شروع کن.", show_alert=True)
        return
        
    q_text = QUIZZES[lesson_id][question_index][0]
    prefix = f"📝 <b>آزمون {LESSONS[lesson_id]['title']}</b>\nسؤال {question_index + 1} از {len(QUIZZES[lesson_id])}\n\n"
    await query.edit_message_text(prefix + q_text, parse_mode="HTML", reply_markup=quiz_keyboard(lesson_id, question_index))

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(next_question, pattern=r"^next:\d+:\d+$"))
    app.add_handler(CallbackQueryHandler(handle_button))
    print("ربات روشن شد. برای توقف، برنامه را متوقف کن.")
    app.run_polling()

if __name__ == "__main__":
    main()