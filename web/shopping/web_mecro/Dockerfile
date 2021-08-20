FROM python:3.8

ENV user kctf
ENV port 5000

RUN apt-get update -y
RUN apt-get install -y wget xvfb unzip curl gnupg
RUN apt-get install -y python3
RUN apt-get install -y python3-pip python-dev build-essential musl-dev gcc

RUN adduser --disabled-password $user
ADD ./web_readbot /home/kctf/
WORKDIR /home/kctf/

RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN wget https://dl.google.com/linux/linux_signing_key.pub
RUN apt-key add linux_signing_key.pub

RUN apt-get update && apt-get install -y google-chrome-stable
RUN rm -rf /etc/apt/sources.list.d/google.list

# Install chromedriver
RUN wget -O /home/kctf/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /home/kctf/chromedriver.zip chromedriver -d /home/kctf/; exit 0
RUN chmod 775 /home/kctf/
RUN chmod 557 /home/kctf/chromedriver

RUN pip3 install selenium bs4
USER $user
EXPOSE $port

ENTRYPOINT ["python"]
CMD ["main.py"]