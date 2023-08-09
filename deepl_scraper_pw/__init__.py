"""Init."""
import nest_asyncio

from .deepl_tr import deepl_tr

nest_asyncio.apply()
__version__ = "0.1.0a2"

__all__ = ("deepl_tr",)
