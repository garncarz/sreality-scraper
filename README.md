# Sreality ads crawler

As per given assignment:
> Use scrapy framework to scrape the first 500 items (title, image url) from sreality.cz (flats, sell) and save it in the Postgresql database. Implement a simple HTTP server in python and show these 500 items on a simple page (title and image) and put everything to single docker compose command so that I can just run "docker-compose up" in the Github repository and see the scraped ads on http://127.0.0.1:8080 page.

## Possible extensions

- Crawling running in a separate container, maybe using Celery
- Logging, metrics, automated tests
- JS front-end with paging

## Development

`docker-compose build`

`docker-compose run app alembic revision --autogenerate -m "<message>"`

`docker-compose run app alembic upgrade head`

`docker-compose run app scrapy crawl ad_spider`
