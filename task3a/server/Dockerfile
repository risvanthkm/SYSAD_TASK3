FROM python:3.10.20

RUN apt-get update && apt-get install -y ffmpeg postgresql-client

WORKDIR /server

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . . 

EXPOSE 8080

CMD ["python", "server.py"]
