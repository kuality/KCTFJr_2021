FROM python:3.8

ENV user kctf
ENV port 8000

RUN apt-get update -y
RUN apt-get install -y sudo python-pip python-dev build-essential musl-dev

RUN adduser --disabled-password $user
ADD ./deploy /app
WORKDIR /app
RUN pip install flask
COPY ./flag /flag
RUN chmod 111 /flag

USER $user
EXPOSE $port

ENTRYPOINT ["python"]
CMD ["app.py"]