from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

# ========== НАСТРОЙКИ ==========
TOKEN = 8413279302:AAGx8BRPVon9T1DXNcwNEvETHX8VDmDrUVU
ADMIN_ID = 8519899945
# ================================

# База пользователей (временно, потом можно подключить БД)
users_balance = {}

async def start(update: Update, context):
    user_id = update.effective_user.id
    if user_id not in users_balance:
        users_balance[user_id] = 0
    
    keyboard = [
        [InlineKeyboardButton("⭐ Купить звёзды", callback_data="buy_stars")],
        [InlineKeyboardButton("💰 Продать звёзды", callback_data="sell_stars")],
        [InlineKeyboardButton("🏠 Аренда NFT", callback_data="rent_nft")],
        [InlineKeyboardButton("🖼 Купить NFT", callback_data="buy_nft")],
        [InlineKeyboardButton("🎁 Купить обычный подарок", callback_data="buy_gift")],
        [InlineKeyboardButton("💎 Купить TON", callback_data="buy_ton")],
        [InlineKeyboardButton("👑 Премиум", callback_data="premium")],
        [InlineKeyboardButton("💳 Пополнить баланс", callback_data="deposit")],
        [InlineKeyboardButton("👤 Профиль", callback_data="profile")],
        [InlineKeyboardButton("📞 Поддержка", callback_data="support")],
        [InlineKeyboardButton("🧮 Калькулятор", callback_data="calculator")],
        [InlineKeyboardButton("ℹ️ Информация", callback_data="info")],
        [InlineKeyboardButton("⭐ Отзывы", callback_data="reviews")],
        [InlineKeyboardButton("🏆 Топ клиентов", callback_data="top")],
        [InlineKeyboardButton("🤝 Создать партнёрского бота", callback_data="partner")]
    ]
    
    await update.message.reply_text(
        f"✨ ДОБРО ПОЖАЛОВАТЬ В GRAVINDES STORE ✨\n\n"
        f"🔥 У нас Вы можете приобрести Telegram Stars, Telegram Premium и арендовать NFT.\n\n"
        f"💰 Текущий баланс: {users_balance[user_id]}₽\n\n"
        f"👇 Выберите действие:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button_handler(update: Update, context):
    query = update.callback_query
    await query.answer()
    user = query.from_user
    user_id = user.id
    
    if query.data == "buy_stars":
        keyboard = [
            [InlineKeyboardButton("50⭐ - 50₽", callback_data="stars_50")],
            [InlineKeyboardButton("100⭐ - 90₽", callback_data="stars_100")],
            [InlineKeyboardButton("250⭐ - 200₽", callback_data="stars_250")],
            [InlineKeyboardButton("500⭐ - 380₽", callback_data="stars_500")],
            [InlineKeyboardButton("1000⭐ - 700₽", callback_data="stars_1000")],
            [InlineKeyboardButton("🔙 Назад", callback_data="back")]
        ]
        await query.edit_message_text("⭐ Выберите количество Звёзд:", reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif query.data == "sell_stars":
        await query.edit_message_text(
            "💰 ПРОДАЖА ЗВЁЗД\n\n"
            "Цена покупки: 0.8₽ за 1⭐\n"
            "Минимальная сумма: 100⭐\n\n"
            "📞 Для продажи напишите @Gravindes",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data="back")]])
        )
    
    elif query.data == "rent_nft":
        keyboard = [
            [InlineKeyboardButton("🏠 Аренда на 7 дней - 100⭐", callback_data="rent_7d")],
            [InlineKeyboardButton("🏠 Аренда на 30 дней - 300⭐", callback_data="rent_30d")],
            [InlineKeyboardButton("🔙 Назад", callback_data="back")]
        ]
        await query.edit_message_text("🏠 ВЫБЕРИТЕ АРЕНДУ NFT:", reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif query.data == "buy_nft":
        keyboard = [
            [InlineKeyboardButton("🖼 Обычный NFT - 150⭐", callback_data="nft_common")],
            [InlineKeyboardButton("🎨 Редкий NFT - 400⭐", callback_data="nft_rare")],
            [InlineKeyboardButton("👑 Легендарный NFT - 1000⭐", callback_data="nft_legend")],
            [InlineKeyboardButton("🔙 Назад", callback_data="back")]
        ]
        await query.
edit_message_text("🖼 ВЫБЕРИТЕ NFT:", reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif query.data == "buy_gift":
        keyboard = [
            [InlineKeyboardButton("🎁 Обычный подарок - 50⭐", callback_data="gift_common")],
            [InlineKeyboardButton("🎁 Улучшенный подарок - 150⭐", callback_data="gift_rare")],
            [InlineKeyboardButton("🔙 Назад", callback_data="back")]
        ]
        await query.edit_message_text("🎁 ВЫБЕРИТЕ ПОДАРОК:", reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif query.data == "buy_ton":
        keyboard = [
            [InlineKeyboardButton("💎 1 TON - 300₽", callback_data="ton_1")],
            [InlineKeyboardButton("💎 5 TON - 1450₽", callback_data="ton_5")],
            [InlineKeyboardButton("💎 10 TON - 2800₽", callback_data="ton_10")],
            [InlineKeyboardButton("🔙 Назад", callback_data="back")]
        ]
        await query.edit_message_text("💎 ВЫБЕРИТЕ КОЛИЧЕСТВО TON:", reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif query.data == "premium":
        keyboard = [
            [InlineKeyboardButton("👑 1 месяц - 150₽", callback_data="prem_1m")],
            [InlineKeyboardButton("👑 3 месяца - 400₽", callback_data="prem_3m")],
            [InlineKeyboardButton("👑 6 месяцев - 750₽", callback_data="prem_6m")],
            [InlineKeyboardButton("👑 12 месяцев - 1400₽", callback_data="prem_12m")],
            [InlineKeyboardButton("🔙 Назад", callback_data="back")]
        ]
        await query.edit_message_text("👑 ВЫБЕРИТЕ ПРЕМИУМ:", reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif query.data == "deposit":
        await query.edit_message_text(
            "💳 ПОПОЛНЕНИЕ БАЛАНСА\n\n"
            "💰 Минимальная сумма: 100₽\n"
            "💳 Способы оплаты:\n"
            "• Карты РФ\n"
            "• Криптовалюта\n"
            "• Telegram Stars\n\n"
            "📞 Для пополнения напишите @Gravindes",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data="back")]])
        )
    
    elif query.data == "profile":
        balance = users_balance.get(user_id, 0)
        await query.edit_message_text(
            f"👤 ПРОФИЛЬ\n\n"
            f"🆔 ID: {user_id}\n"
            f"📝 Имя: {user.first_name}\n"
            f"📝 Username: @{user.username if user.username else 'нет'}\n"
            f"💰 Баланс: {balance}₽\n"
            f"📅 Дата регистрации: {user.id}\n\n"
            f"⭐ Всего куплено звёзд: 0\n"
            f"🖼 Всего куплено NFT: 0",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data="back")]])
        )
    
    elif query.data == "support":
        await query.edit_message_text(
            "📞 ПОДДЕРЖКА\n\n"
            "👤 @Gravindes\n\n"
            "⏰ Время работы: 24/7\n"
            "⚡ Среднее время ответа: 2-5 минут\n\n"
            "🔒 Гарантия возврата средств",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data="back")]])
        )
    
    elif query.data == "calculator":
        await query.edit_message_text(
            "🧮 КАЛЬКУЛЯТОР\n\n"
            "Сколько звёзд можно купить на вашу сумму:\n\n"
            "100₽ → 110⭐\n"
            "500₽ → 560⭐\n"
            "1000₽ → 1150⭐\n\n"
            "📞 Для точного расчёта напишите @Gravindes",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data="back")]])
        )
    
    elif query.data == "info":
        await query.edit_message_text(
            "ℹ️ ИНФОРМАЦИЯ\n\n"
            "✨ GRAVINDES STORE\n\n"
            "🔥 Мы работаем с 2024 года\n"
            "⭐ Более 1000 довольных клиентов\n"
            "🔒 Гарантия качества и возврата\n"
            "⚡ Моментальная выдача товаров\n\n"
            "👤 Владелец: @Gravindes",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data="back")]])
        )
    
    elif query.data == "reviews":
        await query.edit_message_text(
            "⭐ ОТЗЫВЫ\n\n"
"«Отличный магазин, всё быстро!» — @user1\n"
            "«Лучшие цены на звёзды» — @user2\n"
            "«Рекомендую, всё честно» — @user3\n\n"
            "📝 Оставить отзыв: @Gravindes",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data="back")]])
        )
    
    elif query.data == "top":
        await query.edit_message_text(
            "🏆 ТОП КЛИЕНТОВ\n\n"
            "1. @user1 — 50000₽\n"
            "2. @user2 — 35000₽\n"
            "3. @user3 — 20000₽\n\n"
            "🔥 Стань лучшим клиентом!",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data="back")]])
        )
    
    elif query.data == "partner":
        await query.edit_message_text(
            "🤝 ПАРТНЁРСКАЯ ПРОГРАММА\n\n"
            "💰 Зарабатывай с нами!\n\n"
            "• 10% с каждого заказа друга\n"
            "• 5% с заказов партнёра\n"
            "• Выплаты каждый день\n\n"
            "📞 Для подключения: @Gravindes",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data="back")]])
        )
    
    elif query.data == "back":
        await start(update, context)
    
    elif query.data.startswith(("stars_", "rent_", "nft_", "gift_", "ton_", "prem_")):
        # Отправляем заказ админу
        await context.bot.send_message(
            ADMIN_ID,
            f"🛒 НОВЫЙ ЗАКАЗ!\n\n"
            f"📦 Товар: {query.data}\n"
            f"👤 Покупатель: {user.first_name}\n"
            f"🆔 ID: {user_id}\n"
            f"📝 Username: @{user.username if user.username else 'нет'}\n"
            f"🔗 Ссылка: tg://user?id={user_id}"
        )
        await query.edit_message_text(
            "✅ ЗАКАЗ ПРИНЯТ!\n\n"
            "📞 @Gravindes свяжется с тобой для оплаты и выдачи товара.\n\n"
            "⏰ Ожидай ответа в ближайшее время!",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 В меню", callback_data="back")]])
        )

# Запуск
app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

print("✅ GRAVINDES STORE ЗАПУЩЕН!")
app.run_polling()

