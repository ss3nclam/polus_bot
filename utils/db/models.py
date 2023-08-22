from sqlalchemy import String, DateTime, BigInteger, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from loader import db_engine


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(BigInteger(), primary_key=True, nullable=False, unique=True, autoincrement=False)
    name: Mapped[str] = mapped_column(String(45), nullable=False)
    role: Mapped[str] = mapped_column(String(45), nullable=False, default='user')
    created_at = mapped_column(DateTime())

    def __repr__(self) -> str:
        return f"id={self.id!r}, name={self.name!r}, role={self.role!r}"


class Entity(Base):
    __tablename__ = 'entities'
    # id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(45), unique=True, nullable=False, primary_key=True)
    info: Mapped[str] = mapped_column(Text(), nullable=True)
    location: Mapped[str] = mapped_column(String(45), nullable=True)
    contacts: Mapped[str] = mapped_column(String(100), nullable=True)
    notifyer: Mapped[str] = mapped_column(String(45), unique=True, nullable=True)
    created_at = mapped_column(DateTime())
    
    def __repr__(self) -> str:
        return f"name={self.name!r}"


# Create tables
def create_tables():
    Base.metadata.create_all(db_engine)


# Add row inside table
# with Session(db_engine) as session:
#     xz = Test(id=34634634, name='kek3', )
#     session.add(xz)
#     session.commit()