# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from fireapi_v2 import FireapiV2, AsyncFireapiV2
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKvm:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_power(self, client: FireapiV2) -> None:
        kvm = client.kvm.power(
            internal_id="internal_id",
            mode="mode",
        )
        assert_matches_type(object, kvm, path=["response"])

    @parametrize
    def test_raw_response_power(self, client: FireapiV2) -> None:
        response = client.kvm.with_raw_response.power(
            internal_id="internal_id",
            mode="mode",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kvm = response.parse()
        assert_matches_type(object, kvm, path=["response"])

    @parametrize
    def test_streaming_response_power(self, client: FireapiV2) -> None:
        with client.kvm.with_streaming_response.power(
            internal_id="internal_id",
            mode="mode",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kvm = response.parse()
            assert_matches_type(object, kvm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_power(self, client: FireapiV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_id` but received ''"):
            client.kvm.with_raw_response.power(
                internal_id="",
                mode="mode",
            )


class TestAsyncKvm:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_power(self, async_client: AsyncFireapiV2) -> None:
        kvm = await async_client.kvm.power(
            internal_id="internal_id",
            mode="mode",
        )
        assert_matches_type(object, kvm, path=["response"])

    @parametrize
    async def test_raw_response_power(self, async_client: AsyncFireapiV2) -> None:
        response = await async_client.kvm.with_raw_response.power(
            internal_id="internal_id",
            mode="mode",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kvm = await response.parse()
        assert_matches_type(object, kvm, path=["response"])

    @parametrize
    async def test_streaming_response_power(self, async_client: AsyncFireapiV2) -> None:
        async with async_client.kvm.with_streaming_response.power(
            internal_id="internal_id",
            mode="mode",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kvm = await response.parse()
            assert_matches_type(object, kvm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_power(self, async_client: AsyncFireapiV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_id` but received ''"):
            await async_client.kvm.with_raw_response.power(
                internal_id="",
                mode="mode",
            )
