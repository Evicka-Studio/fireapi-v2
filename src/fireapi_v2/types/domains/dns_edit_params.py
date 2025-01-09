# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DNSEditParams"]


class DNSEditParams(TypedDict, total=False):
    record_id: Required[str]

    data: str
    """New content if changing"""

    name: str
    """New name if changing"""

    type: str
    """New type if changing (e.g., A, AAAA, TXT, etc.)"""
