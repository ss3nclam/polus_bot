from sqlalchemy import String, DateTime, BigInteger
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from loader import db_engine


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(BigInteger(), primary_key=True, nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(45), nullable=False)
    role: Mapped[str] = mapped_column(String(45), nullable=False, default='user')
    created = mapped_column(DateTime())

    def __repr__(self) -> str:
        return f"id={self.id!r}, name={self.name!r}, fullname={self.fullname!r}"


# Create tables
def migrate():
    Base.metadata.create_all(db_engine)


# Add row inside table
# with Session(db_engine) as session:
#     xz = Test(id=34634634, name='kek3', )
#     session.add(xz)
#     session.commit()