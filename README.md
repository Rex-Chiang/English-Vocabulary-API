# English-Vocabulary-API

## Overview
Users can use RESTful API to upload english vocabulary and example that they need to review, and retrieve the vocabulary in random mode.\
This project was deployed on **Fly.io (https://fly.io)**

## Quick start
- Clone this repository
```
git clone https://github.com/Rex-Chiang/english-vocabulary-api.git
cd english-vocabulary-api
```
- Setup environment variables
  - PORT 
      - Required in **gunicorn.conf.py**
      - Host port for server
  - LOG_VERSION
      - Required in **settings.py**
      - Log type for logger
- Setup virtual environment
```
python3 -m venv YourVirtualEnvironmentName
source YourVirtualEnvironmentName/bin/activate
```
- Inatall required libraries
```
pip3 install -r requirements.txt
```
- Run the Django server
```
sh runserver.sh
```

## Deployment
- Clone this repository
```
git clone https://github.com/Rex-Chiang/english-vocabulary-api.git
cd english-vocabulary-api
```
- Setup environment variables
  - PORT 
      - Required in **gunicorn.conf.py**
      - Host port for server
  - LOG_VERSION
      - Required in **settings.py**
      - Log type for logger
- Build and tag docker image
```
docker build -t english-vocabulary-api .
docker tag english-vocabulary-api  YourDockerHubAccount/english-vocabulary-api
```
- Push docker image to DockerHub
```
docker push YourDockerHubAccount/english-vocabulary-api
```
- Init the **Fly.io** application
```
flyctl launch
```
- Setup the **Fly.io** configuraton
  - Refer to **fly.toml**
- Deploy **Fly.io** application
```
flyctl deploy
```
