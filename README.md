# Simple RESTful API using Python Flask

This repository contains a minimum RESTful API using Python and Flask. It exposes the endpoint http://HOST:5000/hello. This repository uses a Github Flow branching strategy and Github Actions to run _pylint_ to lint the code and _pytest_ to execute unit tests.

Upon successfull merge into main, a Docker container is built and pushed to Githubs container registry Github Packages.

Finally, the app is deployed to a Kubernetes cluster.

## Local API setup

Running the API locally requires Python 3.9, install that first. Then:

``` bash
python3 -m venv test-api # create virtual environment
source test-api/bin/activate # activate virtual environment
pip3 install -r requirements.txt # install python packages

python3 app/main.py # start API
```

Now, you can access _http://127.0.0.1:5000/hello_.

## Local Docker setup

Building and running Docker containers requires Docker to be installed. Then:
``` bash
docker build -t meine-api . # build Docker container
docker run -it -p 5000:5000 meine-api # run Docker container
```

Now, you can access _http://127.0.0.1:5000/hello_.

## Run latest built Docker container

Requires Docker to be installed. The pull from Docker Hub https://hub.docker.com/r/wu3ty/facehugger:
``` bash
docker pull wu3ty/facehugger:main # pull latest image from Docker Hub
docker run -it -p 5000:5000  wu3ty/facehugger:main # run container
```

Now, you can access _http://127.0.0.1:5000/hello_.
