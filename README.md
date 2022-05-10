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