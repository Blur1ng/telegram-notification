from sqlalchemy.future import select
from app.db.models import VIPUser
from app.db.postgre_con import async_session, AsyncSession

class GetData:
    @staticmethod    
    async def get_all_VIPUsers():
        async with async_session() as db:
            db: AsyncSession
            result = await db.execute(select(VIPUser))
            return result.scalars().all()
        
    @staticmethod
    async def get_VIPUser(username: str):
        async with async_session() as db:
            db: AsyncSession
            stmt = select(VIPUser).where(VIPUser.name == username)
            result = await db.execute(stmt)
            user = result.scalars().first()
            return user
        
class SetData:
    @staticmethod
    async def on_notification(user: VIPUser):
        async with async_session() as db:
            db: AsyncSession
            user.notification = True
            await db.commit()

    @staticmethod
    async def off_notification(user: VIPUser):
        async with async_session() as db:
            db: AsyncSession
            user.notification = False
            await db.commit()
    
class AddData:
    @staticmethod
    async def add_VIPUser(username: str):
        async with async_session() as db:
            db: AsyncSession
            db.add(VIPUser(name=username, notification=True)) 
            await db.commit()
