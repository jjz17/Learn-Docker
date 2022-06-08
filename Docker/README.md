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

Use folium to create interactive map

## flask_redis

### Tutorial
https://takacsmark.com/docker-compose-tutorial-beginners-by-example-basics/#preparing-the-example

#### Pytest Tutorial
https://drive.google.com/file/d/1l2wvDEYATKBqPM2kRG4debCTnxz29D42/view

### Terminal Instructions
    docker-compose up

#### To run
    curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"name":"Jason"}' \
    localhost:5001  

    curl localhost:5001