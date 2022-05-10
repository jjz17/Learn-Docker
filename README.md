# Learn-Docker
A collection of Docker projects for learning purposes.

## imdb_scraper
source venv/bin/activate
docker build -t python-imdb
docker build -t python-imdb .
docker run -t -i python-imdb

## fastapi_webapp
pip freeze > requirements.txt

docker build -t python-fastapi .
docker run -p 8000:8000 python-fastapi

## find_the_iss
Credit for bearing function: https://gist.github.com/jeromer/2005586

### Ideas
Add feature to calculate time to travel the distance by walking/running/other modes of transport