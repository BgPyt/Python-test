from fastapi import FastAPI
from src.cities.routers import router as city_router
from src.picnics.routers import router as picnic_router
from src.user.routers import router as user_router
import uvicorn

app = FastAPI()
app.include_router(city_router,
                   tags=['City'],
                   prefix='/city')
app.include_router(picnic_router,
                   tags=['Picnic'],
                   prefix='/picnic')
app.include_router(user_router,
                   tags=['User'],
                   prefix='/user')

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.0", port=8000)