# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.kvm import (
    backup_create_params,
    backup_delete_params,
    backup_restore_params,
    backup_create_status_params,
    backup_restore_status_params,
)
from ..._base_client import make_request_options

__all__ = ["BackupResource", "AsyncBackupResource"]


class BackupResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BackupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EvickaStudio/fireapi-v2#accessing-raw-response-data-eg-headers
        """
        return BackupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BackupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EvickaStudio/fireapi-v2#with_streaming_response
        """
        return BackupResourceWithStreamingResponse(self)

    def create(
        self,
        internal_id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Create a new backup for a KVM server.

        **Requires 24fire+**.

        Args:
          description: Backup description (max 24 chars, limited allowed symbols)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return self._post(
            f"/api/kvm/{internal_id}/backup/create",
            body=maybe_transform({"description": description}, backup_create_params.BackupCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def delete(
        self,
        internal_id: str,
        *,
        backup_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Permanently delete a backup.

        **Requires 24fire+**.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return self._delete(
            f"/api/kvm/{internal_id}/backup/delete",
            body=maybe_transform({"backup_id": backup_id}, backup_delete_params.BackupDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def create_status(
        self,
        internal_id: str,
        *,
        backup_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Check the status/progress of the running backup creation task.

        **Requires
        24fire+**.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return self._post(
            f"/api/kvm/{internal_id}/backup/create/status",
            body=maybe_transform({"backup_id": backup_id}, backup_create_status_params.BackupCreateStatusParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def restore(
        self,
        internal_id: str,
        *,
        backup_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Restore a specified backup on a KVM server.

        **Requires 24fire+**.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return self._post(
            f"/api/kvm/{internal_id}/backup/restore",
            body=maybe_transform({"backup_id": backup_id}, backup_restore_params.BackupRestoreParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def restore_status(
        self,
        internal_id: str,
        *,
        backup_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Check the status/progress of the running backup restore task.

        **Requires
        24fire+**.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return self._post(
            f"/api/kvm/{internal_id}/backup/restore/status",
            body=maybe_transform({"backup_id": backup_id}, backup_restore_status_params.BackupRestoreStatusParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncBackupResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBackupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EvickaStudio/fireapi-v2#accessing-raw-response-data-eg-headers
        """
        return AsyncBackupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBackupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EvickaStudio/fireapi-v2#with_streaming_response
        """
        return AsyncBackupResourceWithStreamingResponse(self)

    async def create(
        self,
        internal_id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Create a new backup for a KVM server.

        **Requires 24fire+**.

        Args:
          description: Backup description (max 24 chars, limited allowed symbols)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return await self._post(
            f"/api/kvm/{internal_id}/backup/create",
            body=await async_maybe_transform({"description": description}, backup_create_params.BackupCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def delete(
        self,
        internal_id: str,
        *,
        backup_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Permanently delete a backup.

        **Requires 24fire+**.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return await self._delete(
            f"/api/kvm/{internal_id}/backup/delete",
            body=await async_maybe_transform({"backup_id": backup_id}, backup_delete_params.BackupDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def create_status(
        self,
        internal_id: str,
        *,
        backup_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Check the status/progress of the running backup creation task.

        **Requires
        24fire+**.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return await self._post(
            f"/api/kvm/{internal_id}/backup/create/status",
            body=await async_maybe_transform(
                {"backup_id": backup_id}, backup_create_status_params.BackupCreateStatusParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def restore(
        self,
        internal_id: str,
        *,
        backup_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Restore a specified backup on a KVM server.

        **Requires 24fire+**.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return await self._post(
            f"/api/kvm/{internal_id}/backup/restore",
            body=await async_maybe_transform({"backup_id": backup_id}, backup_restore_params.BackupRestoreParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def restore_status(
        self,
        internal_id: str,
        *,
        backup_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Check the status/progress of the running backup restore task.

        **Requires
        24fire+**.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return await self._post(
            f"/api/kvm/{internal_id}/backup/restore/status",
            body=await async_maybe_transform(
                {"backup_id": backup_id}, backup_restore_status_params.BackupRestoreStatusParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class BackupResourceWithRawResponse:
    def __init__(self, backup: BackupResource) -> None:
        self._backup = backup

        self.create = to_raw_response_wrapper(
            backup.create,
        )
        self.delete = to_raw_response_wrapper(
            backup.delete,
        )
        self.create_status = to_raw_response_wrapper(
            backup.create_status,
        )
        self.restore = to_raw_response_wrapper(
            backup.restore,
        )
        self.restore_status = to_raw_response_wrapper(
            backup.restore_status,
        )


class AsyncBackupResourceWithRawResponse:
    def __init__(self, backup: AsyncBackupResource) -> None:
        self._backup = backup

        self.create = async_to_raw_response_wrapper(
            backup.create,
        )
        self.delete = async_to_raw_response_wrapper(
            backup.delete,
        )
        self.create_status = async_to_raw_response_wrapper(
            backup.create_status,
        )
        self.restore = async_to_raw_response_wrapper(
            backup.restore,
        )
        self.restore_status = async_to_raw_response_wrapper(
            backup.restore_status,
        )


class BackupResourceWithStreamingResponse:
    def __init__(self, backup: BackupResource) -> None:
        self._backup = backup

        self.create = to_streamed_response_wrapper(
            backup.create,
        )
        self.delete = to_streamed_response_wrapper(
            backup.delete,
        )
        self.create_status = to_streamed_response_wrapper(
            backup.create_status,
        )
        self.restore = to_streamed_response_wrapper(
            backup.restore,
        )
        self.restore_status = to_streamed_response_wrapper(
            backup.restore_status,
        )


class AsyncBackupResourceWithStreamingResponse:
    def __init__(self, backup: AsyncBackupResource) -> None:
        self._backup = backup

        self.create = async_to_streamed_response_wrapper(
            backup.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            backup.delete,
        )
        self.create_status = async_to_streamed_response_wrapper(
            backup.create_status,
        )
        self.restore = async_to_streamed_response_wrapper(
            backup.restore,
        )
        self.restore_status = async_to_streamed_response_wrapper(
            backup.restore_status,
        )
