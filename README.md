# Simple RESTful API using Python Flask

This repository contains a minimum RESTful API using Python and Flask. It exposes the endpoint http://HOST:5000/hello. This repository uses a Github Flow branching strategy and Github Actions to run _pylint_ to lint the code and _pytest_ to execute unit tests.

Upon successfull merge into main, a Docker container is built and pushed to Githubs container registry Github Packages.

Finally, the app is deployed to a Kubernetes cluster.
