FROM python:3.10-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

COPY .env .env

EXPOSE 8000

CMD ['uvicorn', 'app.main:app', '--host', '0.0.0.0', '8000' '--reload']

