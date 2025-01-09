# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .backup import (
    BackupResource,
    AsyncBackupResource,
    BackupResourceWithRawResponse,
    AsyncBackupResourceWithRawResponse,
    BackupResourceWithStreamingResponse,
    AsyncBackupResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["KvmsResource", "AsyncKvmsResource"]


class KvmsResource(SyncAPIResource):
    @cached_property
    def backup(self) -> BackupResource:
        return BackupResource(self._client)

    @cached_property
    def with_raw_response(self) -> KvmsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/fireapi-v2-python#accessing-raw-response-data-eg-headers
        """
        return KvmsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KvmsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/fireapi-v2-python#with_streaming_response
        """
        return KvmsResourceWithStreamingResponse(self)


class AsyncKvmsResource(AsyncAPIResource):
    @cached_property
    def backup(self) -> AsyncBackupResource:
        return AsyncBackupResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncKvmsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/fireapi-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKvmsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKvmsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/fireapi-v2-python#with_streaming_response
        """
        return AsyncKvmsResourceWithStreamingResponse(self)


class KvmsResourceWithRawResponse:
    def __init__(self, kvms: KvmsResource) -> None:
        self._kvms = kvms

    @cached_property
    def backup(self) -> BackupResourceWithRawResponse:
        return BackupResourceWithRawResponse(self._kvms.backup)


class AsyncKvmsResourceWithRawResponse:
    def __init__(self, kvms: AsyncKvmsResource) -> None:
        self._kvms = kvms

    @cached_property
    def backup(self) -> AsyncBackupResourceWithRawResponse:
        return AsyncBackupResourceWithRawResponse(self._kvms.backup)


class KvmsResourceWithStreamingResponse:
    def __init__(self, kvms: KvmsResource) -> None:
        self._kvms = kvms

    @cached_property
    def backup(self) -> BackupResourceWithStreamingResponse:
        return BackupResourceWithStreamingResponse(self._kvms.backup)


class AsyncKvmsResourceWithStreamingResponse:
    def __init__(self, kvms: AsyncKvmsResource) -> None:
        self._kvms = kvms

    @cached_property
    def backup(self) -> AsyncBackupResourceWithStreamingResponse:
        return AsyncBackupResourceWithStreamingResponse(self._kvms.backup)
