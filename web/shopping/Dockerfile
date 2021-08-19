FROM python:3.8

ENV user kctf
ENV port 8000

RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip python-dev build-essential musl-dev gcc

RUN adduser --disabled-password $user
ADD ./shopping /home/kctf/
WORKDIR /home/kctf/
RUN pip3 install flask sqlalchemy flask_wtf wtforms flask_sqlalchemy
USER $user
EXPOSE $port
RUN chmod 755 /home/kctf
RUN touch /home/kctf/Shopping.sqlite
RUN chmod 664 /home/kctf/Shopping.sqlite

#ENTRYPOINT ["python"]
CMD ["python","main.py"]