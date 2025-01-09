# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from fireapi_v2 import FireapiV2, AsyncFireapiV2
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDonations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: FireapiV2) -> None:
        donation = client.accounts.donations.list()
        assert_matches_type(object, donation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: FireapiV2) -> None:
        response = client.accounts.donations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        donation = response.parse()
        assert_matches_type(object, donation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: FireapiV2) -> None:
        with client.accounts.donations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            donation = response.parse()
            assert_matches_type(object, donation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDonations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncFireapiV2) -> None:
        donation = await async_client.accounts.donations.list()
        assert_matches_type(object, donation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFireapiV2) -> None:
        response = await async_client.accounts.donations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        donation = await response.parse()
        assert_matches_type(object, donation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFireapiV2) -> None:
        async with async_client.accounts.donations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            donation = await response.parse()
            assert_matches_type(object, donation, path=["response"])

        assert cast(Any, response.is_closed) is True
