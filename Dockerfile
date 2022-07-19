FROM jazzdd/alpine-flask 

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY app/ .

ENTRYPOINT ["python", "main.py"]
