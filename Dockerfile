FROM python:3.10
WORKDIR /app

RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get -y install build-essential libssl-dev libffi-dev libblas3 libc6 liblapack3 gcc python3-dev python3-pip cython3
RUN apt-get -y install python3-numpy python3-scipy
RUN apt-get install -y netcat

COPY /requirements.txt requirements.txt

RUN pip install -r requirements.txt --no-cache-dir

COPY . .



CMD ["bash", "/app/wait-for-it.sh"]