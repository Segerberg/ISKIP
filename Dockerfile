FROM python:3.11-slim
WORKDIR /home/iskip

COPY app app
COPY iskip.py config.py requirements.txt entrypoint.sh ./

RUN pip install -r requirements.txt

RUN mkdir "data"

RUN flask db init
RUN flask db migrate
RUN flask db upgrade

ENV FLASK_APP iskip.py

VOLUME /data
EXPOSE 5000

ENTRYPOINT ["sh","entrypoint.sh"]

