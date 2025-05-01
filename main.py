from app.notification.telegram.telegram_main import start_telegram_app
import asyncio

if __name__ == '__main__':
    print("----------------------------------------------------------------------------------------------------------------------")
    asyncio.run(start_telegram_app())