from models.btm import BotAdmin, BotUser, Group
from sqlalchemy.orm import Session


def get_admins(db: Session):
    return db.query(BotAdmin).all()


def get_users(db: Session):
    users = db.query(BotUser).all()
    groups = db.query(Group).all()
    return users + groups
