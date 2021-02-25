FROM kalilinux/kali-rolling
ARG DEBIAN_FRONTEND=noninteractive
ENV TERM xterm-256color
RUN apt-get update && apt upgrade -y && apt-get install sudo -y
WORKDIR /root/userbot
RUN pip3 install -U -r requirements.txt
ENV PATH="/home/userbot/bin:$PATH"
CMD ["python3","-m","userbot"]
