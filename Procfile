web: python manage.py migrate && python manage.py collectstatic
web: python manage.py runserver 0.0.0.0:$PORT
web: gunicorn deploy1.wsgi --log-file -
