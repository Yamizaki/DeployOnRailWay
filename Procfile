web: python manage.py migrate
web: python manage.py runserver 0.0.0.0:$PORT
web: gunicorn deploy1.wsgi
web:python manage.py collectstatic