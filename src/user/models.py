from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship
from src.database import Base
from src.picnics.models import PicnicRegistration


class User(Base):
    """
    Пользователь
    """
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    picnics = relationship('Picnic',
                           secondary=PicnicRegistration.__table__,
                           back_populates='users')


    def __repr__(self):
        return f'<Пользователь {self.surname} {self.name}>'
