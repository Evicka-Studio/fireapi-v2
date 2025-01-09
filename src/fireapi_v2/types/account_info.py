# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["AccountInfo", "Data", "DataInvoiceAddress"]


class DataInvoiceAddress(BaseModel):
    city: Optional[str] = None

    country: Optional[str] = None

    name: Optional[str] = None

    number: Optional[str] = None

    street: Optional[str] = None

    zip: Optional[str] = None


class Data(BaseModel):
    balance: Optional[float] = None

    discord_id: Optional[str] = None

    email: Optional[str] = None

    firstname: Optional[str] = None

    invoice_address: Optional[DataInvoiceAddress] = None

    is_plus_user: Optional[bool] = None

    lastname: Optional[str] = None

    profile_image: Optional[str] = None

    registry_date: Optional[datetime] = None


class AccountInfo(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status: Optional[str] = None
