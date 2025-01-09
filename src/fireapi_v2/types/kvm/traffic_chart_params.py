# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TrafficChartParams"]


class TrafficChartParams(TypedDict, total=False):
    axes_y_label: str

    datapoints: int

    dataset_in_color: str

    dataset_in_label: str

    dataset_out_color: str

    dataset_out_label: str

    output: str
    """Output format (Config or base64 image)"""

    size: str

    summary: str
    """Summation type (DAILY, HOURLY, NONE)"""

    type: str
    """Which traffic type to chart (in, out, both)"""
