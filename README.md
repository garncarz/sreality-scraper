`docker-compose run app alembic revision --autogenerate -m "<message>"`
`docker-compose run app alembic upgrade head`
`docker-compose run app scrapy crawl ad_spider`
