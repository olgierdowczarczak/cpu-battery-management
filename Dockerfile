# Dockerfile, Image, Container
FROM python:3.11

COPY src/ ./src

COPY json/ ./json

RUN pip install psutil

CMD [ "python", "./src/main.py" ]
