# source env/bin/activate
# pip freeze > requirements.txt
# docker build --tag minihackathon1 .
# docker run -d -p 5000:5000 minihackathon1
# docker ps
# docker stop <container id>
# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker


COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .


EXPOSE 5000

CMD [ "python3", "app.py"]
#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
