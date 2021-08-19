FROM ubuntu:18.04

#RUN sed -i 's/archive.ubuntu.com/mirror.kakao.com/g' /etc/apt/sources.list

RUN groupadd -g 2000 sql
RUN useradd -g 2000 -u 2000 -m sql
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y apache2
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:ondrej/php

RUN apt-get install -y php5.6
RUN apt-get install -y php5.6-mysqli

RUN echo AddType application/x-httpd-php .php .phtml .html .htm >> /etc/apache2/mods-enabled/mime.conf

COPY ./deploy/* /var/www/html/
EXPOSE 80
CMD ["apache2ctl","-D","FOREGROUND"]