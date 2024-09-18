from __future__ import annotations

import functools
import json
from typing import Any

from .residents import Resident
from .snowflake import Snowflake
from .utils import since_epoch


__all__ = (
    "JSONEncoder",
    "dumps",
    "dump",
)


class JSONEncoder(json.JSONEncoder):
    """Custom JSON encoder for serializable class in this API"""

    def default(self, o: Any) -> Any:
        try:
            return super().default(o)

        except TypeError:
            if isinstance(o, Resident):
                return {
                    "id": o.id,
                    "name": o.name,
                    "room": o.room,
                    "birthday": None if o.birthday is None else since_epoch(o.birthday),
                    "phone": o.phone,
                    "email": o.email,
                    "username": o.username,
                }

            if isinstance(o, Snowflake):
                return {
                    "id": o.id,
                }

            raise


dumps = functools.partial(json.dumps, cls=JSONEncoder)
dump = functools.partial(json.dump, cls=JSONEncoder)
