# 📬 Telegram Notification Bot

Бот-уведомитель на базе `Aiogram` и `FastAPI`, предназначенный для отправки сообщений VIP-пользователям.

## 🚀 Возможности

- Асинхронная работа с Telegram через [aiogram](https://github.com/aiogram/aiogram)
- Интеграция с PostgreSQL через `SQLAlchemy`
- Управление уведомлениями: включить/выключить
- Базовая проверка на VIP-статус
- Миграции с Alembic
- `.env` конфигурация

## ⚙️ Установка

```bash
git clone https://github.com/Blur1ng/telegram-notification.git
cd telegram-notification
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
🔐 Переменные окружения
Создайте .env файл в корне проекта:
```ini
TOKEN=your_telegram_bot_token
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/dbname
```
🧩Структура проекта
```bash
.
├── app/
│   ├── db/
│   │   ├── models.py          # SQLAlchemy модели
│   │   └── postgre_con.py     # Асинхронное подключение к БД
│   ├── notification/
│   │   ├── sqlalchemy_classes.py 
│   │   └── telegram/
│   │       └── telegram_main.py  # Основной Telegram-бот
├── alembic/
├── main.py                    # start app
├── .env                        
├── requirements.txt
└── README.md
```
