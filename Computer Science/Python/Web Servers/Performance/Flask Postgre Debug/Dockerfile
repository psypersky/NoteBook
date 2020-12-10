FROM python:3.7-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

ENV FLASK_ENV development
ENV FLASK_APP flask_app.py
CMD ["python3", "-m", "flask", "run", "--port", "3000", "--host", "0.0.0.0"]
