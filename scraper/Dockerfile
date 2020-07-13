FROM python:3.7.8-slim

RUN mkdir /app

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY scraper.py scraper.py




CMD python scraper.py