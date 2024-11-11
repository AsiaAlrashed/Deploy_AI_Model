FROM python:3.12.1

WORKDIR /app_ML

COPY ./requirements.txt /app_ML/requirements.txt

RUN pip install --no-cache-dir -r /app_ML/requirements.txt

COPY ./app /app_ML/app

EXPOSE 8000

CMD [ "uvicorn", "app.main:app","--host", "127.0.0.1", "--port", "5000" ]


