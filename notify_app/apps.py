from django.apps import AppConfig

#The app pushes notifications to the front end making the user notified when a post is shared.

class NotifyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notify_app'
