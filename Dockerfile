
FROM python:3.9-alpine

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]

CMD [ "wsgi.py" ]


