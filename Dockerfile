FROM jazzdd/alpine-flask 
#FROM ubuntu

# Install dependencies
#RUN apt-get update && apt-get -y install python3 python3-pip


COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY app/ .

# CMD ["python3","main.py"]
ENTRYPOINT ["python3"]
CMD ["main.py"]

