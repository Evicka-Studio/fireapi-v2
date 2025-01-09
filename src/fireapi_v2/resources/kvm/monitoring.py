# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["MonitoringResource", "AsyncMonitoringResource"]


class MonitoringResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MonitoringResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EvickaStudio/fireapi-v2#accessing-raw-response-data-eg-headers
        """
        return MonitoringResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MonitoringResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EvickaStudio/fireapi-v2#with_streaming_response
        """
        return MonitoringResourceWithStreamingResponse(self)

    def incidences(
        self,
        internal_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Retrieve detected outages and downtime stats.

        **Requires 24fire+**.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return self._get(
            f"/api/kvm/{internal_id}/monitoring/incidences",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def timings(
        self,
        internal_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Retrieve CPU, MEM, and ping stats for the last 30 days.

        **Requires 24fire+**.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return self._get(
            f"/api/kvm/{internal_id}/monitoring/timings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncMonitoringResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMonitoringResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EvickaStudio/fireapi-v2#accessing-raw-response-data-eg-headers
        """
        return AsyncMonitoringResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMonitoringResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EvickaStudio/fireapi-v2#with_streaming_response
        """
        return AsyncMonitoringResourceWithStreamingResponse(self)

    async def incidences(
        self,
        internal_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Retrieve detected outages and downtime stats.

        **Requires 24fire+**.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return await self._get(
            f"/api/kvm/{internal_id}/monitoring/incidences",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def timings(
        self,
        internal_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Retrieve CPU, MEM, and ping stats for the last 30 days.

        **Requires 24fire+**.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return await self._get(
            f"/api/kvm/{internal_id}/monitoring/timings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class MonitoringResourceWithRawResponse:
    def __init__(self, monitoring: MonitoringResource) -> None:
        self._monitoring = monitoring

        self.incidences = to_raw_response_wrapper(
            monitoring.incidences,
        )
        self.timings = to_raw_response_wrapper(
            monitoring.timings,
        )


class AsyncMonitoringResourceWithRawResponse:
    def __init__(self, monitoring: AsyncMonitoringResource) -> None:
        self._monitoring = monitoring

        self.incidences = async_to_raw_response_wrapper(
            monitoring.incidences,
        )
        self.timings = async_to_raw_response_wrapper(
            monitoring.timings,
        )


class MonitoringResourceWithStreamingResponse:
    def __init__(self, monitoring: MonitoringResource) -> None:
        self._monitoring = monitoring

        self.incidences = to_streamed_response_wrapper(
            monitoring.incidences,
        )
        self.timings = to_streamed_response_wrapper(
            monitoring.timings,
        )


class AsyncMonitoringResourceWithStreamingResponse:
    def __init__(self, monitoring: AsyncMonitoringResource) -> None:
        self._monitoring = monitoring

        self.incidences = async_to_streamed_response_wrapper(
            monitoring.incidences,
        )
        self.timings = async_to_streamed_response_wrapper(
            monitoring.timings,
        )
