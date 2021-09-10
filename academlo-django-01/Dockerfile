FROM python:3.9.5

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . app
WORKDIR /app

RUN python manage.py migrate
RUN python manage.py makemigrations

RUN python create_fake_data.py

EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
