FROM python:3.8

WORKDIR /usr/src/Face_Match
COPY requirements.txt .
RUN apt-get update ##[edited]
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install --no-cache-dir cmake
RUN pip install --no-cache-dir -r requirements.txt
COPY . .