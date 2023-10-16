from typing import List
from fastapi import APIRouter, Query, HTTPException, Depends
import datetime as dt
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from src.database import get_session
from src.picnics.models import Picnic, PicnicRegistration
from src.picnics.schemes import *

router = APIRouter()


@router.get('/all-picnics/', summary='All Picnics', response_model=List[AllPicnicModelResponse])
async def get_picnics(time: dt.datetime = Query(default=None, description='Время пикника (по умолчанию не задано)'),
                      past: bool = Query(default=True, description='Включая уже прошедшие пикники'),
                      session: Session = Depends(get_session)):
    """
    Список всех пикников
    """
    picnics = session.query(Picnic).outerjoin(PicnicRegistration)
    if time and past:
        picnics = picnics.filter(Picnic.time <= time)
    if time and not past:
        picnics = picnics.filter(Picnic.time == time)

    return [AllPicnicModelResponse.from_orm(obj) for obj in picnics.all()]


@router.post('/picnic-add/', summary='Picnic Add', response_model=PicnicModel)
async def add_picnic(picnic: PicnicCreate, session: Session = Depends(get_session)):
    """
    Добавление пикника
    """
    try:
        stmt = Picnic(city_id=picnic.city_id,
                      time=picnic.time,
                      )
        session.add(stmt)
        session.commit()
    except IntegrityError:
        raise HTTPException(status_code=400, detail=f'Город с id {picnic.city_id} не существует')
    return PicnicModel.from_orm(stmt)


@router.post('/picnic-register/', summary='Picnic Registration', response_model=RegisterPicnicResponse)
async def add_picnic_register(picnic_register: RegisterPicnicCreate, session: Session = Depends(get_session)):
    """
    Регистрация пользователя на пикник
    """
    try:
        stmt = PicnicRegistration(user_id=picnic_register.user_id,
                                  picnic_id=picnic_register.picnic_id,
                                  )
        session.add(stmt)
        session.commit()
    except IntegrityError:
        raise HTTPException(status_code=400, detail='Неверный city_id или user_id')

    return RegisterPicnicResponse.from_orm(stmt)