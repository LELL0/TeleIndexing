FROM alpine:latest

RUN apk update
RUN apk add python3 py3-pip
RUN mkdir app
COPY requirements.txt app/requirements.txt
COPY teleIndexer.py app/teleIndexer.py
WORKDIR app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3","teleIndexer.py"]