from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.settings import pg_settings

DATABASE_URL = f"postgresql+asyncpg://{pg_settings.user}:{pg_settings.password}@{pg_settings.host}:{pg_settings.port}/{pg_settings.db}"

async_engine = create_async_engine(DATABASE_URL, echo=False)

async_session = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)



