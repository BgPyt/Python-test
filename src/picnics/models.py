from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base


class PicnicRegistration(Base):
    """
    Регистрация пользователя на пикник
    """
    __tablename__ = 'picnic_registration'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    picnic_id = Column(Integer, ForeignKey('picnic.id'), nullable=False)
    user = relationship('User')
    picnic = relationship('Picnic')

    def __repr__(self):
        return f'<Регистрация {self.id}>'


class Picnic(Base):
    """
    Пикник
    """
    __tablename__ = 'picnic'

    id = Column(Integer, primary_key=True, autoincrement=True)
    city_id = Column(Integer, ForeignKey('city.id'), nullable=False)
    time = Column(DateTime, nullable=False)
    city = relationship('City', backref='city_id')
    users = relationship('User',
                         secondary=PicnicRegistration.__table__,
                         back_populates='picnics')

    def __repr__(self):
        return f'<Пикник {self.id}>'
