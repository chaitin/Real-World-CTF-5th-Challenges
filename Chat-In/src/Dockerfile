FROM ubuntu:22.04
RUN apt-get update --fix-missing &&\
 apt-get -y dist-upgrade && \
 apt-get install -y lib32z1 xinetd build-essential python3 python3-pip &&\
 apt-get clean

RUN python3 -m pip install openai


COPY ./chat.py /chat.py
COPY ./run.sh /

RUN chmod 777 /run.sh
# other options
CMD bash /run.sh
