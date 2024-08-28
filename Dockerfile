FROM ubuntu

# Install Linux dependencies
RUN apt-get update 
RUN apt-get -y install python3.10 python3-pip python3-venv

# Install Python requirements
COPY requirements.txt .

RUN python3 -m venv my-venv
RUN .  my-venv/bin/activate

RUN pip3 install -r requirements.txt

# Create a working directory and copy application into container
WORKDIR /app
COPY ./app/ .

# Start API
ENTRYPOINT ["python3", "main.py"]
