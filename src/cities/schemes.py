from pydantic import BaseModel, Field


class CityModel(BaseModel):
    id: int
    name: str = Field(description='Город', default='Москва')
    weather: str = Field(description='текущая погода в городе', default='15.4')

    class Config:
        orm_mode = True
