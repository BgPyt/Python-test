FROM python:3.8-slim as backend
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . python_test
WORKDIR ./python_test
CMD alembic upgrade head && uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload