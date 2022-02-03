from __future__ import annotations

from django.db import models


def fill_id_primary_key(Model: models.Model) -> None:
    """
    Fill in default id primary key with values for existing data
    during data migrations when primary key was set to value in database
    """
    instances = Model.objects.all()
    for id_, instance in enumerate(instances, 1):
        instance.id = id_

    Model.objects.bulk_update(instances, ["id"], batch_size=100000)
