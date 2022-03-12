# Copyright (C) 2021 By AmortMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **مرحبآ عزيزي↤「 [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) 」!**\n
🤖 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) **
** يتيح لك تشغيل الموسيقى والفيديو في مجموعات من خلال المكالمات الجديدة في Telegram! **
💡 ** اكتشف جميع أوامر البوت وكيفية عملها من خلال النقر على زر »📚 الأوامر! **
🔖 ** لمعرفة كيفية استخدام هذا البوت ، يرجى النقر فوق » زر دليل الاستخدام! **
""",
        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        "ضيفني في رومڪـ💝🥂. ",

                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",

                    )

                ],

                [InlineKeyboardButton("اإزاإي تسـ~ـــتعملني💝🥂. ", callback_data="cbhowtouse")],

                [

                    InlineKeyboardButton("اإلمطوꫂر🥵💖", url=f"https://t.me/{OWNER_NAME}"),

                ],

                [

                InlineKeyboardButton("اإوꫂاإمر اإلمطوꫂر💝🥂. ", callback_data="mbbasic"),

                ],

                [

                InlineKeyboardButton("اإوꫂاإمر اإلمشـ~ـــرفين💝🥂. ", callback_data="cbbasic"),

                ],

                [

                InlineKeyboardButton("اإوꫂاإمر اإلاإعضاإء𓆩❤️𓆪", callback_data="vbbasic"),

                    )

                ],

            ]

        ),

        disable_web_page_preview=True,

    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f""" 🫀الدليل الأساسي لاستخدام هذا البوت:🫀 

 1 ↤🫀 أولاً ، أضفني إلى مجموعتك 🫀

 2 ↤🫀 بعد ذلك ، قم بترقيتي كمشرف ومنح جميع الصلاحيات باستثناء الوضع الخفي 🫀

 3 ↤🫀 بعد ترقيتي ، اكتب .تحديث في المجموعة لتحديث بيانات المشرفين 🫀

 3 ↤🫀 أضف @{ASSISTANT_NAME} إلى مجموعتك أو اكتب .استدعاء لدعوة حساب المساعد 🫀

 4 ↤🫀 قم بتشغيل المكالمة  أولاً قبل البدء في تشغيل الفيديو / الموسيقى 🫀

 5 ↤🫀 في بعض الأحيان، يمكن تساعدك إعاده تحميل البوت باستخدام الأمر  .تحديث في إصلاح بعض المشكلات 🫀

 🫀 إذا لم ينضم البوت إلى المكالمة ، فتأكد من تشغيل المكالمة  بالفعل ، أو اكتب .غادر ثم اكتب .استدعاء مرة أخرى 🫀

 🔱 مطور السورس @V_O_O
__""" ,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **press the button below to read the explanation and see the list of available commands !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 Sudo Cmd", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 Basic Cmd", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("mbbasic"))
async def mbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 مرحبا بك يامطوري في اوامرك التالية:

» .مسح - تنظيف جميع الملفات الخادم
» .حذف - تنظيف جميع الملفات التي تم تنزيلها
» .حدث - تحديث البوت الى اخر اصدار
»  .الاصدار - اضهار معلومات النظام
» .حدث - لتحديث البوت الى احدث اصدار
»  .ريستارت - اعادة تشغيل البوت
» .غادر المجموعات - لمغادرة حساب المساعد من كل المجموعات
مطور السورس @V_O_O
__""", 
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙رجوع", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("ebbasic"))
async def ebbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 مرحبا بك هذا هي اوامر المشرفين:

» .مؤقتا - لايقاف الاغنية مؤقتا
» .كمل - لاستمرار الاغنية المتوقفة
» .تخطي - لتخطي اغنية , فيديو
» .اسكت - لانتهاء تشغيل الموسيقى
» .كتم - لكتم حساب المساعد
» .احجي - لالغاء كتم حساب المساعد
» .ضبط 1-200 - لضبط حجم الصوت
» .تحديث - اعادة تشغيل وتحديث بيانات
» .استدعاء - دعوة حساب المساعد للمجموعة
» .غادر - لخروج حساب مساعد من لمجموعة

المطور @V_O_O
__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbstart")]]
        ),
    )
    
    
@Client.on_callback_query(filters.regex("vbbasic"))
async def vbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ها هي اوامر الاعضاء✨ 

» .شغل »「اسم الأغنية / رابط」تشغيل الصوت mp3 في المكالمة 

 » .فيد »「اسم / رابط الفيديو」 تشغيل الفيديو داخل المكالمه 

» .تشغيل صوت »「رابط 」تشغيل صوت بث مباشر

 » .مباشر +「رابط」» تشغيل بث مباشر من اليوتيوب 

»  .بحث + 「اسم」» للبحث عن الاغاني

» .صوت + 「اسم」» لتنزيل صوت من اليوتيوب

» .فيديو + 「اسم」» لتنزيل فيديو من اليوتيوب

» .كلمات + 「اسم」» استخراج كلمات الاغنية

 ⚜ مطور السورس فينوم @V_O_O
__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbstart")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the sudo commands:

» /rmw - clean all raw files
» /rmd - clean all downloaded files
» /sysinfo - show the system information
» /update - update your bot to latest version
» /restart - restart your bot
» /leaveall - order userbot to leave from all group

 ⚡ ادارة سورس العزايزي @php_7
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **الإعدادات** {query.message.chat.title}\n\n⏸ : ايقاف التشغيل موقتآ\n▶️ : استئناف التشغيل\n🔇 : كتم الصوت\n🔊 : الغاء كتم الصوت\n⏹ : ايقاف التشغيل",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 اغلاق", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ قائمة التشغيل فارغه", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    await query.message.delete()
