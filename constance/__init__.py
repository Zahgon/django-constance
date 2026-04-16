from django.utils.functional import LazyObject


class LazyConfig(LazyObject):
    def _setup(self):
        pass


config = LazyConfig()
