cd /home/kinsley/KCTFjr-2021/misc &&\
docker-compose down &&\
docker-compose up --no-build -d &&\
cd /home/kinsley/KCTFjr-2021/pwn &&\
docker-compose down &&\
docker-compose up --no-build -d &&\
cd /home/kinsley/KCTFjr-2021/web &&\
docker-compose down &&\
docker-compose up --no-build -d
