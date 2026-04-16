from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.management import BaseCommand
from django.core.management import CommandError
from django.utils.translation import gettext as _

from constance import config
from constance.forms import ConstanceForm
from constance.models import Constance
from constance.utils import get_values


def _set_constance_value(key, value):
    """
    Parses and sets a Constance value from a string
    :param key:
    :param value:
    :return:
    """
    form = ConstanceForm(initial=get_values())

    field = form.fields[key]

    clean_value = field.clean(field.to_python(value))
    setattr(config, key, clean_value)


class Command(BaseCommand):
    help = _("Get/Set In-database config settings handled by Constance")

    GET = "get"
    SET = "set"
    LIST = "list"
    REMOVE_STALE_KEYS = "remove_stale_keys"

    def add_arguments(self, parser):
        pass

    def handle(self, command, key=None, value=None, *args, **options):
        pass
