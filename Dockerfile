FROM ubuntu

# Install dependencies
RUN apt-get update && apt-get -y install python3 python3-pip

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY app/ .

ENTRYPOINT ["python3", "main.py"]
