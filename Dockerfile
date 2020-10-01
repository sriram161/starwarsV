FROM ubuntu 

RUN apt-get update 
RUN apt-get install -y python3-pip
RUN apt-get install git

COPY requirements.txt /
RUN pip3 install -r requirements.txt

RUN mkdir -p /application
COPY application/ /application

EXPOSE 5000
RUN cd application

CMD [“python3”,”app.py”]