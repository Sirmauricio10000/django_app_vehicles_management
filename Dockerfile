FROM python:3.9-slim
WORKDIR /app
RUN apt-get update && apt-get install -y gcc build-essential libffi-dev
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE 8000
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]