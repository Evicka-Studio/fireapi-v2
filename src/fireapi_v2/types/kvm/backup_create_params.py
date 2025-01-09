# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BackupCreateParams"]


class BackupCreateParams(TypedDict, total=False):
    description: str
    """Backup description (max 24 chars, limited allowed symbols)"""
