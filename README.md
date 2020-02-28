# Skelleton Script for offering a ML model behind an API

Basic setup to offer a datascience prototype (e.g. machine learning model) behind an API using python, flask, and docker.


### requires: 
- serialized file of trained ML-model
- predict method that transforms the required input into a prediction using the trained ML-model
- docker and python 3 installed


### outputs:
- miniconda docker container including
	- running python environment according to `environment.yml`
	- running `main.py` app within newly created environment
	- flask API that serves the datascience prototype
	- swagger spec of API based on docstring of a predict function within `main.py`


