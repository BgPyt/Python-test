from datetime import datetime
from typing import List
from src.cities.schemes import CityModel
from src.user.schemes import UserModel
from pydantic import BaseModel, Field


class PicnicModel(BaseModel):
    id: int
    city: CityModel = Field(description='Название города')
    time: datetime = Field(description='Дата пикника')

    class Config:
        orm_mode = True


class PicnicCreate(BaseModel):
    city_id: int = Field(gt=0, description='ID города, где будет проходить пикник')
    time: datetime = Field(description='Дата проведения пикника', default='2023-10-10 08:05:55')


class RegisterPicnicCreate(BaseModel):
    user_id: int = Field(gt=0, description='ID пользователя')
    picnic_id: int = Field(gt=0, description='ID пикника')


class AllPicnicModelResponse(BaseModel):
    id: int
    city: CityModel = Field(description='Название города')
    time: datetime = Field(description='Дата пикника', default='2023-10-10 08:05:55')
    users: List[UserModel]

    class Config:
        orm_mode = True


class RegisterPicnicResponse(BaseModel):
    id: int
    user: UserModel
    picnic: PicnicModel

    class Config:
        orm_mode = True