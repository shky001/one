# from django.apps import AppConfig
#
#
# class JobsConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'jobs'



from django.apps import AppConfig
import logging
logger = logging.getLogger(__name__)


class JobConfig(AppConfig):
    name = 'jobs'

    def ready(self):
        logger.info("JobConfig ready")
        from jobs.signal_processor import post_save_callback
