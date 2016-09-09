# -*- coding: utf-8 -*-

"""libcomxml package"""

try:
    __version__ = __import__('pkg_resources') \
        .get_distribution(__name__).version
except Exception:
    __version__ = 'unknown'