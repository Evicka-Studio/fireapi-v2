# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DNSAddParams"]


class DNSAddParams(TypedDict, total=False):
    data: Required[str]
    """The content/value of the record."""

    name: Required[str]
    """Subdomain name. Use `*` if needed."""

    type: Required[str]
    """DNS record type (e.g., A, AAAA, TXT, etc.)"""
