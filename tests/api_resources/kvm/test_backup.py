# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from fireapi_v2 import FireapiV2, AsyncFireapiV2
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBackup:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: FireapiV2) -> None:
        backup = client.kvm.backup.create(
            internal_id="internal_id",
        )
        assert_matches_type(object, backup, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: FireapiV2) -> None:
        backup = client.kvm.backup.create(
            internal_id="internal_id",
            description="description",
        )
        assert_matches_type(object, backup, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: FireapiV2) -> None:
        response = client.kvm.backup.with_raw_response.create(
            internal_id="internal_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backup = response.parse()
        assert_matches_type(object, backup, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: FireapiV2) -> None:
        with client.kvm.backup.with_streaming_response.create(
            internal_id="internal_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backup = response.parse()
            assert_matches_type(object, backup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: FireapiV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_id` but received ''"):
            client.kvm.backup.with_raw_response.create(
                internal_id="",
            )

    @parametrize
    def test_method_delete(self, client: FireapiV2) -> None:
        backup = client.kvm.backup.delete(
            internal_id="internal_id",
            backup_id="backup_id",
        )
        assert_matches_type(object, backup, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: FireapiV2) -> None:
        response = client.kvm.backup.with_raw_response.delete(
            internal_id="internal_id",
            backup_id="backup_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backup = response.parse()
        assert_matches_type(object, backup, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: FireapiV2) -> None:
        with client.kvm.backup.with_streaming_response.delete(
            internal_id="internal_id",
            backup_id="backup_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backup = response.parse()
            assert_matches_type(object, backup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: FireapiV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_id` but received ''"):
            client.kvm.backup.with_raw_response.delete(
                internal_id="",
                backup_id="backup_id",
            )

    @parametrize
    def test_method_create_status(self, client: FireapiV2) -> None:
        backup = client.kvm.backup.create_status(
            internal_id="internal_id",
            backup_id="backup_id",
        )
        assert_matches_type(object, backup, path=["response"])

    @parametrize
    def test_raw_response_create_status(self, client: FireapiV2) -> None:
        response = client.kvm.backup.with_raw_response.create_status(
            internal_id="internal_id",
            backup_id="backup_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backup = response.parse()
        assert_matches_type(object, backup, path=["response"])

    @parametrize
    def test_streaming_response_create_status(self, client: FireapiV2) -> None:
        with client.kvm.backup.with_streaming_response.create_status(
            internal_id="internal_id",
            backup_id="backup_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backup = response.parse()
            assert_matches_type(object, backup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_status(self, client: FireapiV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_id` but received ''"):
            client.kvm.backup.with_raw_response.create_status(
                internal_id="",
                backup_id="backup_id",
            )

    @parametrize
    def test_method_restore(self, client: FireapiV2) -> None:
        backup = client.kvm.backup.restore(
            internal_id="internal_id",
            backup_id="backup_id",
        )
        assert_matches_type(object, backup, path=["response"])

    @parametrize
    def test_raw_response_restore(self, client: FireapiV2) -> None:
        response = client.kvm.backup.with_raw_response.restore(
            internal_id="internal_id",
            backup_id="backup_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backup = response.parse()
        assert_matches_type(object, backup, path=["response"])

    @parametrize
    def test_streaming_response_restore(self, client: FireapiV2) -> None:
        with client.kvm.backup.with_streaming_response.restore(
            internal_id="internal_id",
            backup_id="backup_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backup = response.parse()
            assert_matches_type(object, backup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_restore(self, client: FireapiV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_id` but received ''"):
            client.kvm.backup.with_raw_response.restore(
                internal_id="",
                backup_id="backup_id",
            )

    @parametrize
    def test_method_restore_status(self, client: FireapiV2) -> None:
        backup = client.kvm.backup.restore_status(
            internal_id="internal_id",
            backup_id="backup_id",
        )
        assert_matches_type(object, backup, path=["response"])

    @parametrize
    def test_raw_response_restore_status(self, client: FireapiV2) -> None:
        response = client.kvm.backup.with_raw_response.restore_status(
            internal_id="internal_id",
            backup_id="backup_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backup = response.parse()
        assert_matches_type(object, backup, path=["response"])

    @parametrize
    def test_streaming_response_restore_status(self, client: FireapiV2) -> None:
        with client.kvm.backup.with_streaming_response.restore_status(
            internal_id="internal_id",
            backup_id="backup_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backup = response.parse()
            assert_matches_type(object, backup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_restore_status(self, client: FireapiV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_id` but received ''"):
            client.kvm.backup.with_raw_response.restore_status(
                internal_id="",
                backup_id="backup_id",
            )


class TestAsyncBackup:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncFireapiV2) -> None:
        backup = await async_client.kvm.backup.create(
            internal_id="internal_id",
        )
        assert_matches_type(object, backup, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFireapiV2) -> None:
        backup = await async_client.kvm.backup.create(
            internal_id="internal_id",
            description="description",
        )
        assert_matches_type(object, backup, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFireapiV2) -> None:
        response = await async_client.kvm.backup.with_raw_response.create(
            internal_id="internal_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backup = await response.parse()
        assert_matches_type(object, backup, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFireapiV2) -> None:
        async with async_client.kvm.backup.with_streaming_response.create(
            internal_id="internal_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backup = await response.parse()
            assert_matches_type(object, backup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncFireapiV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_id` but received ''"):
            await async_client.kvm.backup.with_raw_response.create(
                internal_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncFireapiV2) -> None:
        backup = await async_client.kvm.backup.delete(
            internal_id="internal_id",
            backup_id="backup_id",
        )
        assert_matches_type(object, backup, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncFireapiV2) -> None:
        response = await async_client.kvm.backup.with_raw_response.delete(
            internal_id="internal_id",
            backup_id="backup_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backup = await response.parse()
        assert_matches_type(object, backup, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncFireapiV2) -> None:
        async with async_client.kvm.backup.with_streaming_response.delete(
            internal_id="internal_id",
            backup_id="backup_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backup = await response.parse()
            assert_matches_type(object, backup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncFireapiV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_id` but received ''"):
            await async_client.kvm.backup.with_raw_response.delete(
                internal_id="",
                backup_id="backup_id",
            )

    @parametrize
    async def test_method_create_status(self, async_client: AsyncFireapiV2) -> None:
        backup = await async_client.kvm.backup.create_status(
            internal_id="internal_id",
            backup_id="backup_id",
        )
        assert_matches_type(object, backup, path=["response"])

    @parametrize
    async def test_raw_response_create_status(self, async_client: AsyncFireapiV2) -> None:
        response = await async_client.kvm.backup.with_raw_response.create_status(
            internal_id="internal_id",
            backup_id="backup_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backup = await response.parse()
        assert_matches_type(object, backup, path=["response"])

    @parametrize
    async def test_streaming_response_create_status(self, async_client: AsyncFireapiV2) -> None:
        async with async_client.kvm.backup.with_streaming_response.create_status(
            internal_id="internal_id",
            backup_id="backup_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backup = await response.parse()
            assert_matches_type(object, backup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_status(self, async_client: AsyncFireapiV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_id` but received ''"):
            await async_client.kvm.backup.with_raw_response.create_status(
                internal_id="",
                backup_id="backup_id",
            )

    @parametrize
    async def test_method_restore(self, async_client: AsyncFireapiV2) -> None:
        backup = await async_client.kvm.backup.restore(
            internal_id="internal_id",
            backup_id="backup_id",
        )
        assert_matches_type(object, backup, path=["response"])

    @parametrize
    async def test_raw_response_restore(self, async_client: AsyncFireapiV2) -> None:
        response = await async_client.kvm.backup.with_raw_response.restore(
            internal_id="internal_id",
            backup_id="backup_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backup = await response.parse()
        assert_matches_type(object, backup, path=["response"])

    @parametrize
    async def test_streaming_response_restore(self, async_client: AsyncFireapiV2) -> None:
        async with async_client.kvm.backup.with_streaming_response.restore(
            internal_id="internal_id",
            backup_id="backup_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backup = await response.parse()
            assert_matches_type(object, backup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_restore(self, async_client: AsyncFireapiV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_id` but received ''"):
            await async_client.kvm.backup.with_raw_response.restore(
                internal_id="",
                backup_id="backup_id",
            )

    @parametrize
    async def test_method_restore_status(self, async_client: AsyncFireapiV2) -> None:
        backup = await async_client.kvm.backup.restore_status(
            internal_id="internal_id",
            backup_id="backup_id",
        )
        assert_matches_type(object, backup, path=["response"])

    @parametrize
    async def test_raw_response_restore_status(self, async_client: AsyncFireapiV2) -> None:
        response = await async_client.kvm.backup.with_raw_response.restore_status(
            internal_id="internal_id",
            backup_id="backup_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backup = await response.parse()
        assert_matches_type(object, backup, path=["response"])

    @parametrize
    async def test_streaming_response_restore_status(self, async_client: AsyncFireapiV2) -> None:
        async with async_client.kvm.backup.with_streaming_response.restore_status(
            internal_id="internal_id",
            backup_id="backup_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backup = await response.parse()
            assert_matches_type(object, backup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_restore_status(self, async_client: AsyncFireapiV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `internal_id` but received ''"):
            await async_client.kvm.backup.with_raw_response.restore_status(
                internal_id="",
                backup_id="backup_id",
            )
