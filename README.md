# everis-challenge

## FLASK/PYTHON - RESTFUL API

* a dockerized restful api app builded with Flask and python 

/greetings: message —> “Hello World from $HOSTNAME”.
/square: message —>  number: X, square: Y.

### Prerequisites
 - Install python3,  on your machine
 - prepare a Virtual environmet using pipenv
 - [docker] installed 

 ### Tree Files & description

| Plugin | README |
| ------ | ------ |
| app.py | the flask/python code of the app |
| Dockerfile | docker commands to assemble the image |


### Build the docker image
- build the image
```sh
docker build -t task1api .
```

[docker]: <https://www.docker.com/products>