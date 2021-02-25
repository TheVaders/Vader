FROM python:3.9.2-slim-buster
RUN git clone https://github.com/TheVaders/Vader /root/userbot
RUN mkdir /root/userbot/bin/
WORKDIR /root/userbot/
RUN chmod +x /usr/local/bin/*
RUN pip3 install -r requirements.txt
CMD ["bash","./KRAKEN/start.sh"]
