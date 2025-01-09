# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from fireapi_v2 import FireapiV2, AsyncFireapiV2
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMonitoring:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_incidences(self, client: FireapiV2) -> None:
        monitoring = client.kvm.monitoring.incidences(
            "internal_id",
        )
        assert_matches_type(object, monitoring, path=["response"])

    @parametrize
    def test_raw_response_incidences(self, client: FireapiV2) -> None:
        response = client.kvm.monitoring.with_raw_response.incidences(
            "internal_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitoring = response.parse()
        assert_matches_type(object, monitoring, path=["response"])

    @parametrize
    def test_streaming_response_incidences(self, client: FireapiV2) -> None:
        with client.kvm.monitoring.with_streaming_response.incidences(
            "internal_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitoring = response.parse()
            assert_matches_type(object, monitoring, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_incidences(self, client: FireapiV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_id` but received ''"):
            client.kvm.monitoring.with_raw_response.incidences(
                "",
            )

    @parametrize
    def test_method_timings(self, client: FireapiV2) -> None:
        monitoring = client.kvm.monitoring.timings(
            "internal_id",
        )
        assert_matches_type(object, monitoring, path=["response"])

    @parametrize
    def test_raw_response_timings(self, client: FireapiV2) -> None:
        response = client.kvm.monitoring.with_raw_response.timings(
            "internal_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitoring = response.parse()
        assert_matches_type(object, monitoring, path=["response"])

    @parametrize
    def test_streaming_response_timings(self, client: FireapiV2) -> None:
        with client.kvm.monitoring.with_streaming_response.timings(
            "internal_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitoring = response.parse()
            assert_matches_type(object, monitoring, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_timings(self, client: FireapiV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_id` but received ''"):
            client.kvm.monitoring.with_raw_response.timings(
                "",
            )


class TestAsyncMonitoring:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_incidences(self, async_client: AsyncFireapiV2) -> None:
        monitoring = await async_client.kvm.monitoring.incidences(
            "internal_id",
        )
        assert_matches_type(object, monitoring, path=["response"])

    @parametrize
    async def test_raw_response_incidences(self, async_client: AsyncFireapiV2) -> None:
        response = await async_client.kvm.monitoring.with_raw_response.incidences(
            "internal_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitoring = await response.parse()
        assert_matches_type(object, monitoring, path=["response"])

    @parametrize
    async def test_streaming_response_incidences(self, async_client: AsyncFireapiV2) -> None:
        async with async_client.kvm.monitoring.with_streaming_response.incidences(
            "internal_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitoring = await response.parse()
            assert_matches_type(object, monitoring, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_incidences(self, async_client: AsyncFireapiV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_id` but received ''"):
            await async_client.kvm.monitoring.with_raw_response.incidences(
                "",
            )

    @parametrize
    async def test_method_timings(self, async_client: AsyncFireapiV2) -> None:
        monitoring = await async_client.kvm.monitoring.timings(
            "internal_id",
        )
        assert_matches_type(object, monitoring, path=["response"])

    @parametrize
    async def test_raw_response_timings(self, async_client: AsyncFireapiV2) -> None:
        response = await async_client.kvm.monitoring.with_raw_response.timings(
            "internal_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitoring = await response.parse()
        assert_matches_type(object, monitoring, path=["response"])

    @parametrize
    async def test_streaming_response_timings(self, async_client: AsyncFireapiV2) -> None:
        async with async_client.kvm.monitoring.with_streaming_response.timings(
            "internal_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitoring = await response.parse()
            assert_matches_type(object, monitoring, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_timings(self, async_client: AsyncFireapiV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_id` but received ''"):
            await async_client.kvm.monitoring.with_raw_response.timings(
                "",
            )
