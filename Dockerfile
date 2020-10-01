FROM ubuntu:18.04

RUN apt-get update 
RUN apt-get install -y python3-pip
RUN apt-get install -y git

RUN adduser flasky
USER flasky
WORKDIR /home/flasky

RUN git clone https://github.com/sriram161/starwarsV.git

RUN pip3 install -r /home/flasky/starwarsV/requirements.txt

EXPOSE 5000

WORKDIR /home/flasky/starwarsV/application
RUN git checkout master
RUN git pull

CMD ["python3", "server.py"]