import json
from collections import OrderedDict
from datetime import date
from datetime import datetime
from operator import itemgetter

from django import forms
from django import get_version
from django.apps import apps
from django.contrib import admin
from django.contrib import messages
from django.contrib.admin.models import CHANGE
from django.contrib.admin.models import LogEntry
from django.contrib.admin.options import csrf_protect_m
from django.contrib.admin.views.main import PAGE_VAR
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import path
from django.utils.formats import localize
from django.utils.translation import gettext_lazy as _

from . import LazyConfig
from . import settings
from .forms import ConstanceForm
from .utils import get_values

config = LazyConfig()


class ConstanceAdmin(admin.ModelAdmin):
    change_list_template = "admin/constance/change_list.html"
    change_list_form = ConstanceForm

    def __init__(self, model, admin_site):
        model._meta.concrete_model = Config
        super().__init__(model, admin_site)

    def get_urls(self):
        pass

    def get_config_value(self, name, options, form, initial):
        pass

    def get_changelist_form(self, request):
        """Returns a Form class for use in the changelist_view."""
        pass

    @csrf_protect_m
    def changelist_view(self, request, extra_context=None):
        pass

    def history_view(self, request, object_id=None, extra_context=None):
        """Display the change history for constance config values."""
        pass

    def _log_config_change(self, request, changed_fields):
        """
        Create a Django admin LogEntry recording which config fields were changed.

        Uses the standard Django JSON change_message format so that
        LogEntry.get_change_message() can interpret it correctly.
        """
        pass

    def has_add_permission(self, *args, **kwargs):
        pass

    def has_delete_permission(self, *args, **kwargs):
        pass

    def has_view_permission(self, request, obj=None):
        pass

    def has_change_permission(self, request, obj=None):
        pass


class Config:
    class Meta:
        app_label = "constance"
        object_name = "Config"
        concrete_model = None
        model_name = module_name = "config"
        verbose_name_plural = _("config")
        abstract = False
        swapped = False
        is_composite_pk = False

        def get_ordered_objects(self):
            pass

        def get_change_permission(self):
            pass

        @property
        def app_config(self):
            pass

        @property
        def label(self):
            pass

        @property
        def label_lower(self):
            pass

    _meta = Meta()


admin.site.register([Config], ConstanceAdmin)
