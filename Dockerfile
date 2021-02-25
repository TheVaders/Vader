FROM python:3.9.2-slim-buster
COPY ./KRAKEN/start.sh .
RUN chmod +x start.sh && sh start.sh
WORKDIR /root/TheVaders/
CMD ["bash", "./KRAKEN/start.sh"]
