# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from fireapi_v2 import FireapiV2, AsyncFireapiV2
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDomains:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: FireapiV2) -> None:
        domain = client.domains.retrieve(
            "internal_id",
        )
        assert_matches_type(object, domain, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: FireapiV2) -> None:
        response = client.domains.with_raw_response.retrieve(
            "internal_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(object, domain, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: FireapiV2) -> None:
        with client.domains.with_streaming_response.retrieve(
            "internal_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(object, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: FireapiV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_id` but received ''"):
            client.domains.with_raw_response.retrieve(
                "",
            )


class TestAsyncDomains:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFireapiV2) -> None:
        domain = await async_client.domains.retrieve(
            "internal_id",
        )
        assert_matches_type(object, domain, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFireapiV2) -> None:
        response = await async_client.domains.with_raw_response.retrieve(
            "internal_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(object, domain, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFireapiV2) -> None:
        async with async_client.domains.with_streaming_response.retrieve(
            "internal_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(object, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFireapiV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_id` but received ''"):
            await async_client.domains.with_raw_response.retrieve(
                "",
            )
