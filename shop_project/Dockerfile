FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY shop_project .
RUN python manage.py collectstatic --noinput
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "shop_project.asgi:application"]