FROM python:3.14-slim

WORKDIR /app

COPY lesson_29/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY lesson_29/ ./lesson_29/

CMD ["pytest", "-v", "lesson_29/tests/"]