# Learn-Docker
A collection of Docker projects for learning purposes.

## imdb_scraper
### Terminal Instructions
    source venv/bin/activate
    docker build -t python-imdb .
    docker run -t -i python-imdb

## fastapi_webapp
    pip freeze > requirements.txt

### Terminal Instructions
    docker build -t python-fastapi .
    docker run -p 8000:8000 python-fastapi

## find_the_iss
### Terminal Instructions
    docker build -t python-iss .
    docker run python-iss

Credit for bearing function: https://gist.github.com/jeromer/2005586

### Ideas
Add feature to calculate time to travel the distance by walking/running/other modes of transport
Find free Google Maps API alternative?
Draw a world map with user and iss locations rendered with icons?
