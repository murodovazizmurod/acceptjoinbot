from database.db import Base
from sqlalchemy import Column, String, Integer, Boolean, DateTime
from database.db import engine

class BotAdmin(Base):
    __tablename__ = "Admin"
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True)
    name = Column(String)

    def __str__(self):
        return self.name


class BotUser(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True)
    name = Column(String)

    def __str__(self):
        return self.name


class Group(Base):
    __tablename__ = "Group"
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True)
    title = Column(String)

    def __str__(self):
        return self.title

