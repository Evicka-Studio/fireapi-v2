# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from fireapi_v2 import FireapiV2, AsyncFireapiV2
from tests.utils import assert_matches_type
from fireapi_v2.types import AccountInfo

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: FireapiV2) -> None:
        account = client.accounts.retrieve()
        assert_matches_type(AccountInfo, account, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: FireapiV2) -> None:
        response = client.accounts.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountInfo, account, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: FireapiV2) -> None:
        with client.accounts.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountInfo, account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccounts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFireapiV2) -> None:
        account = await async_client.accounts.retrieve()
        assert_matches_type(AccountInfo, account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFireapiV2) -> None:
        response = await async_client.accounts.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountInfo, account, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFireapiV2) -> None:
        async with async_client.accounts.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountInfo, account, path=["response"])

        assert cast(Any, response.is_closed) is True
