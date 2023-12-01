from . import models


class AdPipeline:
    def process_item(self, item, spider):
        ad, created = models.get_or_create(
            models.Ad,
            hash_id=item['hash_id'],
        )
        ad.title = item['title']
        ad.image = item['image']
        models.db_session.add(ad)
        models.db_session.commit()
