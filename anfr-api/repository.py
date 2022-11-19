from sqlalchemy import and_
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import false
from datetime import datetime


class TableRepository:
    entity: object = NotImplementedError
    db: Session = NotImplementedError

    def __init__(self, db: Session, entity: object):
        self.db = db
        self.entity = entity

    def get_all(self):
        return self.db.query(self.entity)

    def get_by_id(self, id: int):
        return self.db.query(self.entity).filter(self.entity.id == id).one()

    def find_by_id(self, id: int):
        return self.db.query(self.entity).filter(self.entity.id == id).first()

    def get_actives(self):
        return self.db.query(self.entity).filter(self.entity.is_active == True)

    def get_by_account_id(self, account_id: int):
        return self.db.query(self.entity).filter(self.entity.account_id == account_id)

    def get_actives_by_account_id(self, account_id: int):
        return self.db.query(self.entity).filter \
            (self.entity.is_active == True, self.entity.account_id == account_id)

    def get_by_create_datetime_range(self, from_datetime: datetime, to_datetime: datetime):
        data = self.db.query(self.entity).filter \
            (self.entity.created_datetime >= from_datetime, \
             self.entity.created_datetime <= to_datetime)
        return data

    def add(self, entity, created_by_user_id: int = None):
        entity.created_by = created_by_user_id
        self.db.add(entity)

    def update(self, entity, updated_by_user_id: int = None):
        entity.updated_by = updated_by_user_id

    def delete(self, entity, deleted_by_user_id: int = None):
        entity.is_active = False
        self.update(entity, updated_by_user_id=deleted_by_user_id)

    def permanent_delete(self, entity):
        self.db.delete(entity)