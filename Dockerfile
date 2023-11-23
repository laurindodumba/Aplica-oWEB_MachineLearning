FROM python:3

WORKDIR /app

#ADD ./app /app

COPY /requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["flask", "run"]

CMD ["app.py"]

CMD flask run 