# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from fireapi_v2 import FireapiV2, AsyncFireapiV2
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDNS:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: FireapiV2) -> None:
        dns = client.domains.dns.retrieve(
            "internal_id",
        )
        assert_matches_type(object, dns, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: FireapiV2) -> None:
        response = client.domains.dns.with_raw_response.retrieve(
            "internal_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns = response.parse()
        assert_matches_type(object, dns, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: FireapiV2) -> None:
        with client.domains.dns.with_streaming_response.retrieve(
            "internal_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns = response.parse()
            assert_matches_type(object, dns, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: FireapiV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_id` but received ''"):
            client.domains.dns.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_add(self, client: FireapiV2) -> None:
        dns = client.domains.dns.add(
            internal_id="internal_id",
            data="data",
            name="name",
            type="type",
        )
        assert_matches_type(object, dns, path=["response"])

    @parametrize
    def test_raw_response_add(self, client: FireapiV2) -> None:
        response = client.domains.dns.with_raw_response.add(
            internal_id="internal_id",
            data="data",
            name="name",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns = response.parse()
        assert_matches_type(object, dns, path=["response"])

    @parametrize
    def test_streaming_response_add(self, client: FireapiV2) -> None:
        with client.domains.dns.with_streaming_response.add(
            internal_id="internal_id",
            data="data",
            name="name",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns = response.parse()
            assert_matches_type(object, dns, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add(self, client: FireapiV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_id` but received ''"):
            client.domains.dns.with_raw_response.add(
                internal_id="",
                data="data",
                name="name",
                type="type",
            )

    @parametrize
    def test_method_edit(self, client: FireapiV2) -> None:
        dns = client.domains.dns.edit(
            internal_id="internal_id",
            record_id="record_id",
        )
        assert_matches_type(object, dns, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: FireapiV2) -> None:
        dns = client.domains.dns.edit(
            internal_id="internal_id",
            record_id="record_id",
            data="data",
            name="name",
            type="type",
        )
        assert_matches_type(object, dns, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: FireapiV2) -> None:
        response = client.domains.dns.with_raw_response.edit(
            internal_id="internal_id",
            record_id="record_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns = response.parse()
        assert_matches_type(object, dns, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: FireapiV2) -> None:
        with client.domains.dns.with_streaming_response.edit(
            internal_id="internal_id",
            record_id="record_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns = response.parse()
            assert_matches_type(object, dns, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: FireapiV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_id` but received ''"):
            client.domains.dns.with_raw_response.edit(
                internal_id="",
                record_id="record_id",
            )

    @parametrize
    def test_method_remove(self, client: FireapiV2) -> None:
        dns = client.domains.dns.remove(
            internal_id="internal_id",
            record_id="record_id",
        )
        assert_matches_type(object, dns, path=["response"])

    @parametrize
    def test_raw_response_remove(self, client: FireapiV2) -> None:
        response = client.domains.dns.with_raw_response.remove(
            internal_id="internal_id",
            record_id="record_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns = response.parse()
        assert_matches_type(object, dns, path=["response"])

    @parametrize
    def test_streaming_response_remove(self, client: FireapiV2) -> None:
        with client.domains.dns.with_streaming_response.remove(
            internal_id="internal_id",
            record_id="record_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns = response.parse()
            assert_matches_type(object, dns, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove(self, client: FireapiV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_id` but received ''"):
            client.domains.dns.with_raw_response.remove(
                internal_id="",
                record_id="record_id",
            )


class TestAsyncDNS:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFireapiV2) -> None:
        dns = await async_client.domains.dns.retrieve(
            "internal_id",
        )
        assert_matches_type(object, dns, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFireapiV2) -> None:
        response = await async_client.domains.dns.with_raw_response.retrieve(
            "internal_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns = await response.parse()
        assert_matches_type(object, dns, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFireapiV2) -> None:
        async with async_client.domains.dns.with_streaming_response.retrieve(
            "internal_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns = await response.parse()
            assert_matches_type(object, dns, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFireapiV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_id` but received ''"):
            await async_client.domains.dns.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_add(self, async_client: AsyncFireapiV2) -> None:
        dns = await async_client.domains.dns.add(
            internal_id="internal_id",
            data="data",
            name="name",
            type="type",
        )
        assert_matches_type(object, dns, path=["response"])

    @parametrize
    async def test_raw_response_add(self, async_client: AsyncFireapiV2) -> None:
        response = await async_client.domains.dns.with_raw_response.add(
            internal_id="internal_id",
            data="data",
            name="name",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns = await response.parse()
        assert_matches_type(object, dns, path=["response"])

    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncFireapiV2) -> None:
        async with async_client.domains.dns.with_streaming_response.add(
            internal_id="internal_id",
            data="data",
            name="name",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns = await response.parse()
            assert_matches_type(object, dns, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add(self, async_client: AsyncFireapiV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_id` but received ''"):
            await async_client.domains.dns.with_raw_response.add(
                internal_id="",
                data="data",
                name="name",
                type="type",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncFireapiV2) -> None:
        dns = await async_client.domains.dns.edit(
            internal_id="internal_id",
            record_id="record_id",
        )
        assert_matches_type(object, dns, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncFireapiV2) -> None:
        dns = await async_client.domains.dns.edit(
            internal_id="internal_id",
            record_id="record_id",
            data="data",
            name="name",
            type="type",
        )
        assert_matches_type(object, dns, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncFireapiV2) -> None:
        response = await async_client.domains.dns.with_raw_response.edit(
            internal_id="internal_id",
            record_id="record_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns = await response.parse()
        assert_matches_type(object, dns, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncFireapiV2) -> None:
        async with async_client.domains.dns.with_streaming_response.edit(
            internal_id="internal_id",
            record_id="record_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns = await response.parse()
            assert_matches_type(object, dns, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncFireapiV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_id` but received ''"):
            await async_client.domains.dns.with_raw_response.edit(
                internal_id="",
                record_id="record_id",
            )

    @parametrize
    async def test_method_remove(self, async_client: AsyncFireapiV2) -> None:
        dns = await async_client.domains.dns.remove(
            internal_id="internal_id",
            record_id="record_id",
        )
        assert_matches_type(object, dns, path=["response"])

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncFireapiV2) -> None:
        response = await async_client.domains.dns.with_raw_response.remove(
            internal_id="internal_id",
            record_id="record_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns = await response.parse()
        assert_matches_type(object, dns, path=["response"])

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncFireapiV2) -> None:
        async with async_client.domains.dns.with_streaming_response.remove(
            internal_id="internal_id",
            record_id="record_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns = await response.parse()
            assert_matches_type(object, dns, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove(self, async_client: AsyncFireapiV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_id` but received ''"):
            await async_client.domains.dns.with_raw_response.remove(
                internal_id="",
                record_id="record_id",
            )
