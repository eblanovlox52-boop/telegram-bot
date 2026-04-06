from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

TOKEN = "8413279302:AAGx8BRPVon9T1DXNcwNEvETHX8VDmDrUVU"
# ТВОЙ Telegram ID (узнай у @userinfobot)
ADMIN_ID = 8413279302  # ЭТО ТВОЙ ID - сюда приходят заказы!

async def start(update: Update, context):
    user = update.effective_user
    keyboard = [
        [InlineKeyboardButton("⭐ Купить Звёзды", callback_data="stars")],
        [InlineKeyboardButton("🖼 Купить NFT", callback_data="nft")],
        [InlineKeyboardButton("📞 Поддержка", callback_data="support")]
    ]
    await update.message.reply_text(
        f"✨ GRAVINDES STORE ✨\n\n"
        f"Привет, {user.first_name}!\n"
        f"🔥 Самые низкие цены!\n"
        f"👤 Владелец: @Gravindes\n\n"
        f"👇 Выбери товар:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button_handler(update: Update, context):
    query = update.callback_query
    await query.answer()
    user = query.from_user
    
    if query.data == "stars":
        # Отправляем тебе в личку заказ на звёзды
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"🛒 НОВЫЙ ЗАКАЗ!\n\n"
                 f"⭐ Товар: Звёзды Telegram\n"
                 f"👤 Покупатель: {user.first_name} {user.last_name or ''}\n"
                 f"🆔 ID: {user.id}\n"
                 f"📝 Юзернейм: @{user.username if user.username else 'нет'}\n"
                 f"🔗 Ссылка: tg://user?id={user.id}"
        )
        await query.edit_message_text(
            "✅ Заявка отправлена!\n\n"
            "📞 @Gravindes свяжется с тобой в ближайшее время.\n"
            "Обычно ответ приходит в течение 5 минут."
        )
        
    elif query.data == "nft":
        # Отправляем тебе в личку заказ на NFT
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"🛒 НОВЫЙ ЗАКАЗ!\n\n"
                 f"🖼 Товар: NFT-подарок\n"
                 f"👤 Покупатель: {user.first_name} {user.last_name or ''}\n"
                 f"🆔 ID: {user.id}\n"
                 f"📝 Юзернейм: @{user.username if user.username else 'нет'}\n"
                 f"🔗 Ссылка: tg://user?id={user.id}"
        )
        await query.edit_message_text(
            "✅ Заявка отправлена!\n\n"
            "📞 @Gravindes свяжется с тобой в ближайшее время.\n"
            "Обычно ответ приходит в течение 5 минут."
        )
        
    elif query.data == "support":
        await query.edit_message_text(
            "📞 Свяжись с продавцом:\n\n"
            "👤 @Gravindes\n\n"
            "Ответим на все вопросы по товарам и оплате!"
        )

# Запуск бота
app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

print("🚀 Бот GRAVINDES STORE запущен!")
app.run_polling()
