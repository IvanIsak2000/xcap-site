FROM python:3.10.6

WORKDIR /fastapi

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./src ./src

CMD ["python3", "./src/server.py"]




