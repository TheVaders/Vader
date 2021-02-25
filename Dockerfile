FROM python:3.9.2-slim-buster
RUN pip3 install --upgrade pip setuptools 
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
WORKDIR /root/userbot/
RUN chmod +x /usr/local/bin/*
CMD ["bash","./KRAKEN/start.sh"]
