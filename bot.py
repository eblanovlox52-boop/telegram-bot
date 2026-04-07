from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

# ========== НАСТРОЙКИ ==========
TOKEN = "8413279302:AAGx8BRPVon9T1DXNcwNEvETHX8VDmDrUVU"
ADMIN_ID = 8519899945
# ================================

# Данные для аренды NFT (с фотками)
RENT_ITEMS = {
    "rent_7d": {"name": "🏠 Аренда на 7 дней", "price": "100⭐", "photo": "https://telegra.ph/file/placeholder-nft-1.jpg"},
    "rent_30d": {"name": "🏠 Аренда на 30 дней", "price": "300⭐", "photo": "https://telegra.ph/file/placeholder-nft-2.jpg"},
    "rent_90d": {"name": "🏠 Аренда на 90 дней", "price": "700⭐", "photo": "https://telegra.ph/file/placeholder-nft-3.jpg"},
}

# Все NFT с фотками
NFT_ITEMS = {
    "nft_common": {"name": "🖼 Обычный NFT", "price": "150⭐", "photo": "https://telegra.ph/file/placeholder-nft-common.jpg"},
    "nft_rare": {"name": "🎨 Редкий NFT", "price": "400⭐", "photo": "https://telegra.ph/file/placeholder-nft-rare.jpg"},
    "nft_legendary": {"name": "👑 Легендарный NFT", "price": "1000⭐", "photo": "https://telegra.ph/file/placeholder-nft-legend.jpg"},
    "nft_cat": {"name": "🐱 Котик NFT", "price": "250⭐", "photo": "https://telegra.ph/file/placeholder-nft-cat.jpg"},
    "nft_dragon": {"name": "🐉 Дракон NFT", "price": "600⭐", "photo": "https://telegra.ph/file/placeholder-nft-dragon.jpg"},
}

# Звёзды
STARS_ITEMS = {
    "stars_50": {"name": "50⭐", "price": "50₽"},
    "stars_100": {"name": "100⭐", "price": "90₽"},
    "stars_250": {"name": "250⭐", "price": "200₽"},
    "stars_500": {"name": "500⭐", "price": "380₽"},
    "stars_1000": {"name": "1000⭐", "price": "700₽"},
}

# Подарки
GIFT_ITEMS = {
    "gift_common": {"name": "🎁 Обычный подарок", "price": "50⭐"},
    "gift_rare": {"name": "🎁 Улучшенный подарок", "price": "150⭐"},
    "gift_premium": {"name": "🎁 Премиум подарок", "price": "300⭐"},
}

# TON
TON_ITEMS = {
    "ton_1": {"name": "1 TON", "price": "300₽"},
    "ton_5": {"name": "5 TON", "price": "1450₽"},
    "ton_10": {"name": "10 TON", "price": "2800₽"},
}

# Премиум
PREMIUM_ITEMS = {
    "prem_1m": {"name": "1 месяц", "price": "150₽"},
    "prem_3m": {"name": "3 месяца", "price": "400₽"},
    "prem_6m": {"name": "6 месяцев", "price": "750₽"},
    "prem_12m": {"name": "12 месяцев", "price": "1400₽"},
}

async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("⭐ Купить звёзды", callback_data="buy_stars")],
        [InlineKeyboardButton("💰 Продать звёзды", callback_data="sell_stars")],
        [InlineKeyboardButton("🏠 Аренда NFT", callback_data="rent_nft")],
        [InlineKeyboardButton("🖼 Купить NFT", callback_data="buy_nft")],
        [InlineKeyboardButton("🎁 Купить подарок", callback_data="buy_gift")],
        [InlineKeyboardButton("💎 Купить TON", callback_data="buy_ton")],
        [InlineKeyboardButton("👑 Премиум", callback_data="premium")],
        [InlineKeyboardButton("💳 Пополнить баланс", callback_data="deposit")],
        [InlineKeyboardButton("👤 Профиль", callback_data="profile")],
        [InlineKeyboardButton("📞 Поддержка", callback_data="support")],
        [InlineKeyboardButton("🧮 Калькулятор", callback_data="calculator")],
        [InlineKeyboardButton("ℹ️ Информация", callback_data="info")],
        [InlineKeyboardButton("⭐ Отзывы", callback_data="reviews")],
        [InlineKeyboardButton("🏆 Топ клиентов", callback_data="top")],
        [InlineKeyboardButton("🤝 Партнёрка", callback_data="partner")],
        [InlineKeyboardButton("J❤️", callback_data="j_fun")]
    ]
    
    await update.message.reply_text(
        "✨ ДОБРО ПОЖАЛОВАТЬ В GRAVINDES STORE ✨\n\n"
        "🔥 У нас Вы можете приобрести Telegram Stars, Telegram Premium и арендовать NFT.\n\n"
        "👇 Выберите действие:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def show_rent_nft(update: Update, context):
    keyboard = []
    for key, item in RENT_ITEMS.items():
        keyboard.append([InlineKeyboardButton(f"{item['name']} - {item['price']}", callback_data=f"order_{key}")])
    keyboard.
append([InlineKeyboardButton("🔙 Назад", callback_data="back")])
    
    await update.callback_query.edit_message_text(
        "🏠 АРЕНДА NFT:\n\nВыберите срок аренды:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def show_buy_nft(update: Update, context):
    keyboard = []
    for key, item in NFT_ITEMS.items():
        keyboard.append([InlineKeyboardButton(f"{item['name']} - {item['price']}", callback_data=f"view_nft_{key}")])
    keyboard.append([InlineKeyboardButton("🔙 Назад", callback_data="back")])
    
    await update.callback_query.edit_message_text(
        "🖼 ВЫБЕРИТЕ NFT:\n\nНажмите на NFT чтобы посмотреть фото:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def view_nft(update: Update, context, nft_key):
    nft = NFT_ITEMS[nft_key]
    keyboard = [
        [InlineKeyboardButton("✅ Купить", callback_data=f"order_{nft_key}")],
        [InlineKeyboardButton("🔙 Назад", callback_data="buy_nft")]
    ]
    
    await update.callback_query.delete_message()
    await update.callback_query.message.reply_photo(
        photo=nft["photo"],
        caption=f"🖼 {nft['name']}\n💰 Цена: {nft['price']}\n\nНажмите «Купить» для оформления заказа:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button_handler(update: Update, context):
    query = update.callback_query
    await query.answer()
    user = query.from_user
    
    data = query.data
    
    if data == "buy_stars":
        keyboard = []
        for key, item in STARS_ITEMS.items():
            keyboard.append([InlineKeyboardButton(f"{item['name']} - {item['price']}", callback_data=f"order_{key}")])
        keyboard.append([InlineKeyboardButton("🔙 Назад", callback_data="back")])
        await query.edit_message_text("⭐ ВЫБЕРИТЕ КОЛИЧЕСТВО ЗВЁЗД:", reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif data == "sell_stars":
        await query.edit_message_text(
            "💰 ПРОДАЖА ЗВЁЗД\n\nЦена покупки: 0.8₽ за 1⭐\nМинимальная сумма: 100⭐\n\n📞 Для продажи напишите @Gravindes",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data="back")]]))
    
    elif data == "rent_nft":
        await show_rent_nft(update, context)
    
    elif data == "buy_nft":
        await show_buy_nft(update, context)
    
    elif data == "buy_gift":
        keyboard = []
        for key, item in GIFT_ITEMS.items():
            keyboard.append([InlineKeyboardButton(f"{item['name']} - {item['price']}", callback_data=f"order_{key}")])
        keyboard.append([InlineKeyboardButton("🔙 Назад", callback_data="back")])
        await query.edit_message_text("🎁 ВЫБЕРИТЕ ПОДАРОК:", reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif data == "buy_ton":
        keyboard = []
        for key, item in TON_ITEMS.items():
            keyboard.append([InlineKeyboardButton(f"{item['name']} - {item['price']}", callback_data=f"order_{key}")])
        keyboard.append([InlineKeyboardButton("🔙 Назад", callback_data="back")])
        await query.edit_message_text("💎 ВЫБЕРИТЕ КОЛИЧЕСТВО TON:", reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif data == "premium":
        keyboard = []
        for key, item in PREMIUM_ITEMS.items():
            keyboard.append([InlineKeyboardButton(f"{item['name']} - {item['price']}", callback_data=f"order_{key}")])
        keyboard.append([InlineKeyboardButton("🔙 Назад", callback_data="back")])
        await query.edit_message_text("👑 ВЫБЕРИТЕ ПРЕМИУМ:", reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif data == "deposit":
        await query.edit_message_text(
            "💳 ПОПОЛНЕНИЕ БАЛАНСА\n\nМинимальная сумма: 100₽\nСпособы оплаты: Карты РФ, Криптовалюта, Telegram Stars\n\n📞 Для пополнения напишите @Gravindes",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data="back")]]))
    
    elif data == "profile":
        await query.edit_message_text(
            f"👤 ПРОФИЛЬ\n\n🆔 ID: {user.id}\n📝 Имя: {user.first_name}\n📝 Username: @{user.username if user.
username else 'нет'}\n💰 Баланс: 0₽\n\n⭐ Куплено звёзд: 0\n🖼 Куплено NFT: 0",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data="back")]]))
    
    elif data == "support":
        await query.edit_message_text(
            "📞 ПОДДЕРЖКА\n\n👤 @Gravindes\n⏰ 24/7\n⚡ Ответ 2-5 минут\n\n🔒 Гарантия возврата средств",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data="back")]]))
    
    elif data == "calculator":
        await query.edit_message_text(
            "🧮 КАЛЬКУЛЯТОР\n\n100₽ → 110⭐\n500₽ → 560⭐\n1000₽ → 1150⭐\n\n📞 Точный расчёт: @Gravindes",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data="back")]]))
    
    elif data == "info":
        await query.edit_message_text(
            "ℹ️ ИНФОРМАЦИЯ\n\n✨ GRAVINDES STORE\n🔥 Работаем с 2024 года\n⭐ 1000+ довольных клиентов\n🔒 Гарантия качества\n⚡ Моментальная выдача\n\n👤 Владелец: @Gravindes",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data="back")]]))
    
    elif data == "reviews":
        await query.edit_message_text(
            "⭐ ОТЗЫВЫ\n\n«Отличный магазин, всё быстро!» — @client1\n«Лучшие цены на рынке» — @client2\n«Рекомендую, всё честно!» — @client3\n\n📝 Оставить отзыв: @Gravindes",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data="back")]]))
    
    elif data == "top":
        await query.edit_message_text(
            "🏆 ТОП КЛИЕНТОВ\n\n1. @client1 — 50000₽\n2. @client2 — 35000₽\n3. @client3 — 20000₽\n4. @client4 — 15000₽\n5. @client5 — 10000₽\n\n🔥 Стань лучшим клиентом!",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data="back")]]))
    
    elif data == "partner":
        await query.edit_message_text(
            "🤝 ПАРТНЁРСКАЯ ПРОГРАММА\n\n💰 10% с каждого заказа друга\n💸 5% с заказов партнёра\n💳 Выплаты каждый день\n\n📞 Для подключения: @Gravindes",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data="back")]]))
    
    elif data == "j_fun":
        await query.edit_message_text(
            "J❤️\n\nЭто кнопка для хорошего настроения! 😎\n\n@Gravindes желает тебе отличного дня! 🚀",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data="back")]]))
    
    elif data.startswith("view_nft_"):
        nft_key = data.replace("view_nft_", "")
        await view_nft(update, context, nft_key)
    
    elif data == "back":
        await start(update, context)
    
    elif data.startswith("order_"):
        await context.bot.send_message(
            ADMIN_ID,
            f"🛒 НОВЫЙ ЗАКАЗ!\n\n📦 Товар: {data}\n👤 Покупатель: {user.first_name}\n🆔 ID: {user.id}\n📝 Username: @{user.username if user.username else 'нет'}\n🔗 Ссылка: tg://user?id={user.id}"
        )
        await query.edit_message_text(
            "✅ ЗАКАЗ ПРИНЯТ!\n\n📞 @Gravindes свяжется с тобой для оплаты и получения товара.\n\n⏰ Ожидай ответа в ближайшее время!",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 В меню", callback_data="back")]])
        )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

print("✅ GRAVINDES STORE ЗАПУЩЕН!")
app.run_polling()

