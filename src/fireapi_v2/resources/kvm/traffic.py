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
from ...types.kvm import traffic_chart_params
from ..._base_client import make_request_options

__all__ = ["TrafficResource", "AsyncTrafficResource"]


class TrafficResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TrafficResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/fireapi-v2-python#accessing-raw-response-data-eg-headers
        """
        return TrafficResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrafficResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/fireapi-v2-python#with_streaming_response
        """
        return TrafficResourceWithStreamingResponse(self)

    def retrieve(
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
        """
        Retrieve the current month's traffic usage for the specified KVM server.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return self._get(
            f"/api/kvm/{internal_id}/traffic/current",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def chart(
        self,
        internal_id: str,
        *,
        axes_y_label: str | NotGiven = NOT_GIVEN,
        datapoints: int | NotGiven = NOT_GIVEN,
        dataset_in_color: str | NotGiven = NOT_GIVEN,
        dataset_in_label: str | NotGiven = NOT_GIVEN,
        dataset_out_color: str | NotGiven = NOT_GIVEN,
        dataset_out_label: str | NotGiven = NOT_GIVEN,
        output: str | NotGiven = NOT_GIVEN,
        size: str | NotGiven = NOT_GIVEN,
        summary: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Return traffic data in a format suitable for chart rendering or as a Base64
        image. **Requires 24fire+**.

        Args:
          output: Output format (Config or base64 image)

          summary: Summation type (DAILY, HOURLY, NONE)

          type: Which traffic type to chart (in, out, both)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return self._post(
            f"/api/kvm/{internal_id}/traffic/chart",
            body=maybe_transform(
                {
                    "axes_y_label": axes_y_label,
                    "datapoints": datapoints,
                    "dataset_in_color": dataset_in_color,
                    "dataset_in_label": dataset_in_label,
                    "dataset_out_color": dataset_out_color,
                    "dataset_out_label": dataset_out_label,
                    "output": output,
                    "size": size,
                    "summary": summary,
                    "type": type,
                },
                traffic_chart_params.TrafficChartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def log(
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
        """
        Get the 10-minute traffic measurements for the specified KVM server.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return self._get(
            f"/api/kvm/{internal_id}/traffic/log",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncTrafficResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTrafficResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/fireapi-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTrafficResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrafficResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/fireapi-v2-python#with_streaming_response
        """
        return AsyncTrafficResourceWithStreamingResponse(self)

    async def retrieve(
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
        """
        Retrieve the current month's traffic usage for the specified KVM server.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return await self._get(
            f"/api/kvm/{internal_id}/traffic/current",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def chart(
        self,
        internal_id: str,
        *,
        axes_y_label: str | NotGiven = NOT_GIVEN,
        datapoints: int | NotGiven = NOT_GIVEN,
        dataset_in_color: str | NotGiven = NOT_GIVEN,
        dataset_in_label: str | NotGiven = NOT_GIVEN,
        dataset_out_color: str | NotGiven = NOT_GIVEN,
        dataset_out_label: str | NotGiven = NOT_GIVEN,
        output: str | NotGiven = NOT_GIVEN,
        size: str | NotGiven = NOT_GIVEN,
        summary: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Return traffic data in a format suitable for chart rendering or as a Base64
        image. **Requires 24fire+**.

        Args:
          output: Output format (Config or base64 image)

          summary: Summation type (DAILY, HOURLY, NONE)

          type: Which traffic type to chart (in, out, both)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return await self._post(
            f"/api/kvm/{internal_id}/traffic/chart",
            body=await async_maybe_transform(
                {
                    "axes_y_label": axes_y_label,
                    "datapoints": datapoints,
                    "dataset_in_color": dataset_in_color,
                    "dataset_in_label": dataset_in_label,
                    "dataset_out_color": dataset_out_color,
                    "dataset_out_label": dataset_out_label,
                    "output": output,
                    "size": size,
                    "summary": summary,
                    "type": type,
                },
                traffic_chart_params.TrafficChartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def log(
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
        """
        Get the 10-minute traffic measurements for the specified KVM server.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return await self._get(
            f"/api/kvm/{internal_id}/traffic/log",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class TrafficResourceWithRawResponse:
    def __init__(self, traffic: TrafficResource) -> None:
        self._traffic = traffic

        self.retrieve = to_raw_response_wrapper(
            traffic.retrieve,
        )
        self.chart = to_raw_response_wrapper(
            traffic.chart,
        )
        self.log = to_raw_response_wrapper(
            traffic.log,
        )


class AsyncTrafficResourceWithRawResponse:
    def __init__(self, traffic: AsyncTrafficResource) -> None:
        self._traffic = traffic

        self.retrieve = async_to_raw_response_wrapper(
            traffic.retrieve,
        )
        self.chart = async_to_raw_response_wrapper(
            traffic.chart,
        )
        self.log = async_to_raw_response_wrapper(
            traffic.log,
        )


class TrafficResourceWithStreamingResponse:
    def __init__(self, traffic: TrafficResource) -> None:
        self._traffic = traffic

        self.retrieve = to_streamed_response_wrapper(
            traffic.retrieve,
        )
        self.chart = to_streamed_response_wrapper(
            traffic.chart,
        )
        self.log = to_streamed_response_wrapper(
            traffic.log,
        )


class AsyncTrafficResourceWithStreamingResponse:
    def __init__(self, traffic: AsyncTrafficResource) -> None:
        self._traffic = traffic

        self.retrieve = async_to_streamed_response_wrapper(
            traffic.retrieve,
        )
        self.chart = async_to_streamed_response_wrapper(
            traffic.chart,
        )
        self.log = async_to_streamed_response_wrapper(
            traffic.log,
        )
