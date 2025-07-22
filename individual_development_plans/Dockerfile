FROM python:3.13.5-slim
RUN groupadd -r groupdjango && useradd -r -g groupdjango userdj

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
WORKDIR /app/www/sitewomen
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
USER userdj