import os

DATABASE = os.getenv('DATABASE', 'postgresql://postgres@db/postgres')

MAX_ITEMS = int(os.getenv('MAX_ITEMS', 500))
ITEM_PIPELINES = {
    'app.pipelines.AdPipeline': 100,
}
SPIDER_MODULES = 'app.spiders'
