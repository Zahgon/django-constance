import json
import logging
import pickle
from base64 import b64decode
from importlib import import_module

from django.db import migrations

from constance import settings
from constance.codecs import dumps

logger = logging.getLogger(__name__)


def is_already_migrated(value):
    pass


def import_module_attr(path):
    pass


def migrate_pickled_data(apps, schema_editor) -> None:  # pragma: no cover
    pass


class Migration(migrations.Migration):
    dependencies = [("constance", "0002_migrate_from_old_table")]

    operations = [
        migrations.RunPython(migrate_pickled_data),
    ]
