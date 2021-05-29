from channels.db import database_sync_to_async
from django.db import models


class DefaultQuerySet(models.QuerySet):

    @database_sync_to_async
    def async_first(self):
        return self.first()


