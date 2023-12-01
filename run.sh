#!/usr/bin/env bash

alembic upgrade head
scrapy crawl ad_spider
uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
