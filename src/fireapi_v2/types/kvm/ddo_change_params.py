# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DdoChangeParams"]


class DdoChangeParams(TypedDict, total=False):
    ip_address: str
    """If omitted, applies to all IP addresses"""

    layer4: str
    """dynamic, permanent, or off"""

    layer7: str
    """on or off"""
