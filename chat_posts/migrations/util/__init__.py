from __future__ import annotations

from django.db import models

def fill_id_primary_key(Model: models.Model) -> None:
    """
    Fill in default id primary key with values for existing data
    during data migrations when primary key was set to value in database
    """
    
    for id_, instance in enumerate(Model.objects.all(), 1):
        instance.id = id_
        instance.save()

