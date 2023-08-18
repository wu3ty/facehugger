FROM ubuntu

# Install Linux dependencies
RUN apt-get update && apt-get -y install python3 python3-pip

# Install Python requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Create a working directory and copy application into container
WORKDIR /app
COPY ./app/ .

# Start API
ENTRYPOINT ["python3", "main.py"]
