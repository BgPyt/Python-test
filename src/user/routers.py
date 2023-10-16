from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy import desc, asc
from sqlalchemy.orm import Session
from src.database import get_session
from src.user.models import User
from src.user.schemes import UserOrderRequest, RegisterUserRequest, UserModel

router = APIRouter()


@router.get('/get-users/', summary='', response_model=List[UserModel])
async def get_users(order: UserOrderRequest = None,
                    session: Session = Depends(get_session)):
    """
    Список пользователей
    """

    users = session.query(User)
    users = {'desc': users.order_by(desc(User.age)), 'asc': users.order_by(asc(User.age))}[order]

    return [UserModel.from_orm(user) for user in users.all()]


@router.post('/register-user/', summary='CreateUser', response_model=UserModel)
async def add_user(user: RegisterUserRequest,
                   session: Session = Depends(get_session)):
    """
    Регистрация пользователя
    """
    user_object = User(**user.dict())
    session.add(user_object)
    session.commit()

    return UserModel.from_orm(user_object)