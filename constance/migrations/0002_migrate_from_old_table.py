from logging import getLogger

from django.core.management.color import no_style
from django.db import migrations

logger = getLogger(__name__)


def _migrate_from_old_table(apps, schema_editor) -> None:
    """
    Copies values from old table.
    On new installations just ignore error that table does not exist.
    """
    pass


class Migration(migrations.Migration):
    dependencies = [("constance", "0001_initial")]

    atomic = False

    operations = [
        migrations.RunPython(_migrate_from_old_table, reverse_code=lambda x, y: None),
    ]
