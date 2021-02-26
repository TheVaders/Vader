FROM kalilinux/kali-rolling
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt upgrade -y && apt-get install sudo -y

RUN apt-get install -y\
    coreutils \
    apt-utils \
    bash \
    build-essential \
    cmake \
    curl \
    figlet \
    gcc \
    g++ \
    git \
    postgresql \
    postgresql-client \
    postgresql-server-dev-all \
    wget \
    python3 \
    python3-dev \
    python3-pip \
    libreadline-dev \
    sqlite3 \
    ffmpeg \
    libsqlite3-dev
    
RUN apt-get autoremove --purge
RUN pip3 install --upgrade pip setuptools 
RUN pip3 install --upgrade pip
RUN if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi 
RUN if [ ! -e /usr/bin/python ]; then ln -sf /usr/bin/python3 /usr/bin/python; fi 
RUN rm -r /root/.cache
RUN git clone https://github.com/TheVaders/Vader /root/userbot
RUN mkdir /root/userbot/bin/
WORKDIR /root/userbot/
RUN chmod +x /usr/local/bin/*
RUN pip3 install -r requirements.txt
CMD ["bash","./KRAKEN/start.sh"]
