import asyncio
import warnings

from . import settings
from . import utils


class AsyncValueProxy:
    def __init__(self, key, config, default):
        self._key = key
        self._config = config
        self._default = default
        self._value = None
        self._fetched = False

    def __await__(self):
        return self._get_value().__await__()

    async def _get_value(self):
        pass

    def _get_sync_value(self):
        pass

    def __str__(self):
        return str(self._get_sync_value())

    def __repr__(self):
        return repr(self._get_sync_value())

    def __int__(self):
        return int(self._get_sync_value())

    def __float__(self):
        return float(self._get_sync_value())

    def __bool__(self):
        return bool(self._get_sync_value())

    def __eq__(self, other):
        return self._get_sync_value() == other

    def __ne__(self, other):
        return self._get_sync_value() != other

    def __lt__(self, other):
        return self._get_sync_value() < other

    def __le__(self, other):
        return self._get_sync_value() <= other

    def __gt__(self, other):
        return self._get_sync_value() > other

    def __ge__(self, other):
        return self._get_sync_value() >= other

    def __getitem__(self, key):
        return self._get_sync_value()[key]

    def __iter__(self):
        return iter(self._get_sync_value())

    def __len__(self):
        return len(self._get_sync_value())

    def __contains__(self, item):
        return item in self._get_sync_value()

    def __hash__(self):
        return hash(self._get_sync_value())

    def __add__(self, other):
        return self._get_sync_value() + other

    def __sub__(self, other):
        return self._get_sync_value() - other

    def __mul__(self, other):
        return self._get_sync_value() * other

    def __truediv__(self, other):
        return self._get_sync_value() / other


class Config:
    """The global config wrapper that handles the backend."""

    def __init__(self):
        super().__setattr__("_backend", utils.import_module_attr(settings.BACKEND)())

    def _get_sync_value(self, key, default):
        pass

    def __getattr__(self, key):
        if key == "_backend":
            return super().__getattribute__(key)
        try:
            if len(settings.CONFIG[key]) not in (2, 3):
                raise AttributeError(key)
            default = settings.CONFIG[key][0]
        except KeyError as e:
            raise AttributeError(key) from e

        try:
            asyncio.get_running_loop()
        except RuntimeError:
            return self._get_sync_value(key, default)
        return AsyncValueProxy(key, self, default)

    def __setattr__(self, key, value):
        if key == "_backend":
            super().__setattr__(key, value)
            return
        if key not in settings.CONFIG:
            raise AttributeError(key)
        self._backend.set(key, value)
        return

    async def aset(self, key, value):
        pass

    async def amget(self, keys):
        pass

    def __dir__(self):
        return settings.CONFIG.keys()
