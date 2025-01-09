# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["KvmPowerParams"]


class KvmPowerParams(TypedDict, total=False):
    mode: Required[str]
    """The power action to perform (start, stop, reboot, force-stop, etc.)"""
