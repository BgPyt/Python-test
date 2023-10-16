from typing import List
from fastapi import APIRouter, HTTPException, Query, Depends
from src.cities.models import City
from src.cities.schemes import CityModel
from sqlalchemy.orm import Session
from src.database import get_session
from src.utils.external_requests import CheckCityExisting

router = APIRouter()


@router.post('/create-city/',
             summary='Create City',
             description='Создание города по его названию',
             response_model=CityModel,
             )
async def add_city(city: str = Query(description="Название города", default=None),
                   session: Session = Depends(get_session)):
    if city is None:
        raise HTTPException(status_code=400, detail='Параметр city должен быть указан')
    check = CheckCityExisting()
    if not check.check_existing(city):
        raise HTTPException(status_code=400, detail='Параметр city должен быть существующим городом')

    city_object = session.query(City).filter(City.name == city.capitalize()).first()
    if city_object is None:
        city_object = City(name=city.capitalize())
        session.add(city_object)
        session.commit()

    return CityModel.from_orm(city_object)


@router.get('/get-cities/',
            summary='Get Cities',
            response_model=List[CityModel])
async def get_cities(q: str = Query(description="Название города", default=None),
                     session: Session = Depends(get_session)):
    """
    Получение списка городов
    """
    cities = session.query(City).filter(City.name.ilike(f'%{q}%'))
    s = cities.all()
    return [CityModel.from_orm(city) for city in s]