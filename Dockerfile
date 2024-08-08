FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3 python3-pip git && \
    apt-get clean

WORKDIR /usr/src/app

COPY ./requirements.txt ./requirements.txt

RUN pip3 install --no-cache-dir --break-system-packages -r ./requirements.txt

COPY ./src .
COPY ./credentials/password.json .

EXPOSE 8440

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8440", "--reload"]