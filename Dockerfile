FROM python:3.8-slim

WORKDIR /app
COPY requirements.txt . 
RUN pip install -r requirements.txt

COPY . .
EXPOSE 80

# change to gunicorn for production
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver"]


