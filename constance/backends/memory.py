from threading import Lock

from constance import config
from constance import signals

from . import Backend


class MemoryBackend(Backend):
    """Simple in-memory backend that should be mostly used for testing purposes."""

    _storage = {}
    _lock = Lock()

    def __init__(self):
        super().__init__()

    def get(self, key):
        with self._lock:
            return self._storage.get(key)

    async def aget(self, key):
        # Memory operations are fast enough that we don't need true async here
        pass

    def mget(self, keys):
        if not keys:
            return {}
        with self._lock:
            return {key: self._storage[key] for key in keys if key in self._storage}

    async def amget(self, keys):
        pass

    def set(self, key, value):
        pass

    async def aset(self, key, value):
        # Memory operations are fast enough that we don't need true async here
        pass
