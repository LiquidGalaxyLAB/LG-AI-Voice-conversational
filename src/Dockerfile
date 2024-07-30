FROM python:3.10-slim

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y git

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8440

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8440", "--reload"]
