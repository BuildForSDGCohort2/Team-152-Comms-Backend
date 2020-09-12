release: python manage.py makemigrations
release: python manage.py migrate
release: python manage.py collectstatic
web: uvicorn comms.asgi:application --host 0.0.0.0 --port $PORT
