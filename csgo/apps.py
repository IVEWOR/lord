from django.apps import AppConfig


def store_as_webp(sender, **kwargs):
    webp_path = sender.storage.path('.'.join([sender.name, 'webp']))
    sender.image.save(webp_path, 'webp')


class CsgoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'csgo'

    def ready(self):
        from easy_thumbnails.signals import thumbnail_created
        thumbnail_created.connect(store_as_webp)
