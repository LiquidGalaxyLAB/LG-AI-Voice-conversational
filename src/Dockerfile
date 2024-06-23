FROM python:3.9-slim

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y git

COPY . .

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install git+https://github.com/suno-ai/bark.git

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
