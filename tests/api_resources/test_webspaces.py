# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from fireapi_v2 import FireapiV2, AsyncFireapiV2
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebspaces:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: FireapiV2) -> None:
        webspace = client.webspaces.retrieve(
            "internal_id",
        )
        assert_matches_type(object, webspace, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: FireapiV2) -> None:
        response = client.webspaces.with_raw_response.retrieve(
            "internal_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webspace = response.parse()
        assert_matches_type(object, webspace, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: FireapiV2) -> None:
        with client.webspaces.with_streaming_response.retrieve(
            "internal_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webspace = response.parse()
            assert_matches_type(object, webspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: FireapiV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_id` but received ''"):
            client.webspaces.with_raw_response.retrieve(
                "",
            )


class TestAsyncWebspaces:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFireapiV2) -> None:
        webspace = await async_client.webspaces.retrieve(
            "internal_id",
        )
        assert_matches_type(object, webspace, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFireapiV2) -> None:
        response = await async_client.webspaces.with_raw_response.retrieve(
            "internal_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webspace = await response.parse()
        assert_matches_type(object, webspace, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFireapiV2) -> None:
        async with async_client.webspaces.with_streaming_response.retrieve(
            "internal_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webspace = await response.parse()
            assert_matches_type(object, webspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFireapiV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_id` but received ''"):
            await async_client.webspaces.with_raw_response.retrieve(
                "",
            )
