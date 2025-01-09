# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .ddos import (
    DdosResource,
    AsyncDdosResource,
    DdosResourceWithRawResponse,
    AsyncDdosResourceWithRawResponse,
    DdosResourceWithStreamingResponse,
    AsyncDdosResourceWithStreamingResponse,
)
from .backup import (
    BackupResource,
    AsyncBackupResource,
    BackupResourceWithRawResponse,
    AsyncBackupResourceWithRawResponse,
    BackupResourceWithStreamingResponse,
    AsyncBackupResourceWithStreamingResponse,
)
from .config import (
    ConfigResource,
    AsyncConfigResource,
    ConfigResourceWithRawResponse,
    AsyncConfigResourceWithRawResponse,
    ConfigResourceWithStreamingResponse,
    AsyncConfigResourceWithStreamingResponse,
)
from .status import (
    StatusResource,
    AsyncStatusResource,
    StatusResourceWithRawResponse,
    AsyncStatusResourceWithRawResponse,
    StatusResourceWithStreamingResponse,
    AsyncStatusResourceWithStreamingResponse,
)
from ...types import kvm_power_params
from .traffic import (
    TrafficResource,
    AsyncTrafficResource,
    TrafficResourceWithRawResponse,
    AsyncTrafficResourceWithRawResponse,
    TrafficResourceWithStreamingResponse,
    AsyncTrafficResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from .monitoring import (
    MonitoringResource,
    AsyncMonitoringResource,
    MonitoringResourceWithRawResponse,
    AsyncMonitoringResourceWithRawResponse,
    MonitoringResourceWithStreamingResponse,
    AsyncMonitoringResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["KvmResource", "AsyncKvmResource"]


class KvmResource(SyncAPIResource):
    @cached_property
    def backup(self) -> BackupResource:
        return BackupResource(self._client)

    @cached_property
    def traffic(self) -> TrafficResource:
        return TrafficResource(self._client)

    @cached_property
    def monitoring(self) -> MonitoringResource:
        return MonitoringResource(self._client)

    @cached_property
    def ddos(self) -> DdosResource:
        return DdosResource(self._client)

    @cached_property
    def config(self) -> ConfigResource:
        return ConfigResource(self._client)

    @cached_property
    def status(self) -> StatusResource:
        return StatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> KvmResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EvickaStudio/fireapi-v2#accessing-raw-response-data-eg-headers
        """
        return KvmResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KvmResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EvickaStudio/fireapi-v2#with_streaming_response
        """
        return KvmResourceWithStreamingResponse(self)

    def power(
        self,
        internal_id: str,
        *,
        mode: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Start, stop, or reboot a KVM server.

        Args:
          mode: The power action to perform (start, stop, reboot, force-stop, etc.)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return self._post(
            f"/api/kvm/{internal_id}/power",
            body=maybe_transform({"mode": mode}, kvm_power_params.KvmPowerParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncKvmResource(AsyncAPIResource):
    @cached_property
    def backup(self) -> AsyncBackupResource:
        return AsyncBackupResource(self._client)

    @cached_property
    def traffic(self) -> AsyncTrafficResource:
        return AsyncTrafficResource(self._client)

    @cached_property
    def monitoring(self) -> AsyncMonitoringResource:
        return AsyncMonitoringResource(self._client)

    @cached_property
    def ddos(self) -> AsyncDdosResource:
        return AsyncDdosResource(self._client)

    @cached_property
    def config(self) -> AsyncConfigResource:
        return AsyncConfigResource(self._client)

    @cached_property
    def status(self) -> AsyncStatusResource:
        return AsyncStatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncKvmResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EvickaStudio/fireapi-v2#accessing-raw-response-data-eg-headers
        """
        return AsyncKvmResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKvmResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EvickaStudio/fireapi-v2#with_streaming_response
        """
        return AsyncKvmResourceWithStreamingResponse(self)

    async def power(
        self,
        internal_id: str,
        *,
        mode: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Start, stop, or reboot a KVM server.

        Args:
          mode: The power action to perform (start, stop, reboot, force-stop, etc.)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return await self._post(
            f"/api/kvm/{internal_id}/power",
            body=await async_maybe_transform({"mode": mode}, kvm_power_params.KvmPowerParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class KvmResourceWithRawResponse:
    def __init__(self, kvm: KvmResource) -> None:
        self._kvm = kvm

        self.power = to_raw_response_wrapper(
            kvm.power,
        )

    @cached_property
    def backup(self) -> BackupResourceWithRawResponse:
        return BackupResourceWithRawResponse(self._kvm.backup)

    @cached_property
    def traffic(self) -> TrafficResourceWithRawResponse:
        return TrafficResourceWithRawResponse(self._kvm.traffic)

    @cached_property
    def monitoring(self) -> MonitoringResourceWithRawResponse:
        return MonitoringResourceWithRawResponse(self._kvm.monitoring)

    @cached_property
    def ddos(self) -> DdosResourceWithRawResponse:
        return DdosResourceWithRawResponse(self._kvm.ddos)

    @cached_property
    def config(self) -> ConfigResourceWithRawResponse:
        return ConfigResourceWithRawResponse(self._kvm.config)

    @cached_property
    def status(self) -> StatusResourceWithRawResponse:
        return StatusResourceWithRawResponse(self._kvm.status)


class AsyncKvmResourceWithRawResponse:
    def __init__(self, kvm: AsyncKvmResource) -> None:
        self._kvm = kvm

        self.power = async_to_raw_response_wrapper(
            kvm.power,
        )

    @cached_property
    def backup(self) -> AsyncBackupResourceWithRawResponse:
        return AsyncBackupResourceWithRawResponse(self._kvm.backup)

    @cached_property
    def traffic(self) -> AsyncTrafficResourceWithRawResponse:
        return AsyncTrafficResourceWithRawResponse(self._kvm.traffic)

    @cached_property
    def monitoring(self) -> AsyncMonitoringResourceWithRawResponse:
        return AsyncMonitoringResourceWithRawResponse(self._kvm.monitoring)

    @cached_property
    def ddos(self) -> AsyncDdosResourceWithRawResponse:
        return AsyncDdosResourceWithRawResponse(self._kvm.ddos)

    @cached_property
    def config(self) -> AsyncConfigResourceWithRawResponse:
        return AsyncConfigResourceWithRawResponse(self._kvm.config)

    @cached_property
    def status(self) -> AsyncStatusResourceWithRawResponse:
        return AsyncStatusResourceWithRawResponse(self._kvm.status)


class KvmResourceWithStreamingResponse:
    def __init__(self, kvm: KvmResource) -> None:
        self._kvm = kvm

        self.power = to_streamed_response_wrapper(
            kvm.power,
        )

    @cached_property
    def backup(self) -> BackupResourceWithStreamingResponse:
        return BackupResourceWithStreamingResponse(self._kvm.backup)

    @cached_property
    def traffic(self) -> TrafficResourceWithStreamingResponse:
        return TrafficResourceWithStreamingResponse(self._kvm.traffic)

    @cached_property
    def monitoring(self) -> MonitoringResourceWithStreamingResponse:
        return MonitoringResourceWithStreamingResponse(self._kvm.monitoring)

    @cached_property
    def ddos(self) -> DdosResourceWithStreamingResponse:
        return DdosResourceWithStreamingResponse(self._kvm.ddos)

    @cached_property
    def config(self) -> ConfigResourceWithStreamingResponse:
        return ConfigResourceWithStreamingResponse(self._kvm.config)

    @cached_property
    def status(self) -> StatusResourceWithStreamingResponse:
        return StatusResourceWithStreamingResponse(self._kvm.status)


class AsyncKvmResourceWithStreamingResponse:
    def __init__(self, kvm: AsyncKvmResource) -> None:
        self._kvm = kvm

        self.power = async_to_streamed_response_wrapper(
            kvm.power,
        )

    @cached_property
    def backup(self) -> AsyncBackupResourceWithStreamingResponse:
        return AsyncBackupResourceWithStreamingResponse(self._kvm.backup)

    @cached_property
    def traffic(self) -> AsyncTrafficResourceWithStreamingResponse:
        return AsyncTrafficResourceWithStreamingResponse(self._kvm.traffic)

    @cached_property
    def monitoring(self) -> AsyncMonitoringResourceWithStreamingResponse:
        return AsyncMonitoringResourceWithStreamingResponse(self._kvm.monitoring)

    @cached_property
    def ddos(self) -> AsyncDdosResourceWithStreamingResponse:
        return AsyncDdosResourceWithStreamingResponse(self._kvm.ddos)

    @cached_property
    def config(self) -> AsyncConfigResourceWithStreamingResponse:
        return AsyncConfigResourceWithStreamingResponse(self._kvm.config)

    @cached_property
    def status(self) -> AsyncStatusResourceWithStreamingResponse:
        return AsyncStatusResourceWithStreamingResponse(self._kvm.status)
