FROM ubuntu:18.04

RUN sed -i 's/archive.ubuntu.com/mirror.kakao.com/g' /etc/apt/sources.list
ARG DEBIAN_FRONTEND=noninteractive

RUN groupadd -g 2000 picshell
RUN useradd -g 2000 -u 2000 -m picshell

RUN apt-get update
RUN apt-get install apache2 -y
RUN apt-get install apache2-utils -y
RUN apt-get clean

RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:ondrej/php

RUN apt-get install -y php5.6
RUN apt-get install -y php5.6-mysqli

RUN echo AddType application/x-httpd-php .php .phtml .html .htm >> /etc/apache2/mods-enabled/mime.conf

RUN mkdir /var/www/html/upload
RUN chmod 774 /var/www/html/upload

COPY ./deploy/* /var/www/html/

RUN mv /var/www/html/flag.txt /flag.txt

CMD ["apache2ctl", "-D", "FOREGROUND"]