FROM python:3.8

ENV user kctf
ENV port 8000

RUN apt-get update -y
RUN apt-get install -y sudo python-pip python-dev build-essential musl-dev

RUN adduser --disabled-password $user
COPY ./deploy/ /app/

WORKDIR /app
RUN pip install flask
COPY ./flag /flag

RUN chmod 111 /flag
RUN chown -R kctf:kctf /app

USER $user
EXPOSE $port

ENTRYPOINT ["python"]
CMD ["app.py"]