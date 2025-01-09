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
from ...types.kvm import ddo_change_params
from ..._base_client import make_request_options

__all__ = ["DdosResource", "AsyncDdosResource"]


class DdosResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DdosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/fireapi-v2-python#accessing-raw-response-data-eg-headers
        """
        return DdosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DdosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/fireapi-v2-python#with_streaming_response
        """
        return DdosResourceWithStreamingResponse(self)

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
        Fetch the current DDoS settings for the server's IP addresses.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return self._get(
            f"/api/kvm/{internal_id}/ddos",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def change(
        self,
        internal_id: str,
        *,
        ip_address: str | NotGiven = NOT_GIVEN,
        layer4: str | NotGiven = NOT_GIVEN,
        layer7: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Change the layer4 and layer7 DDoS protection for specific or all IPs.

        **Requires
        24fire+**.

        Args:
          ip_address: If omitted, applies to all IP addresses

          layer4: dynamic, permanent, or off

          layer7: on or off

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return self._post(
            f"/api/kvm/{internal_id}/ddos/change",
            body=maybe_transform(
                {
                    "ip_address": ip_address,
                    "layer4": layer4,
                    "layer7": layer7,
                },
                ddo_change_params.DdoChangeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncDdosResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDdosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/fireapi-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDdosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDdosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/fireapi-v2-python#with_streaming_response
        """
        return AsyncDdosResourceWithStreamingResponse(self)

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
        Fetch the current DDoS settings for the server's IP addresses.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return await self._get(
            f"/api/kvm/{internal_id}/ddos",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def change(
        self,
        internal_id: str,
        *,
        ip_address: str | NotGiven = NOT_GIVEN,
        layer4: str | NotGiven = NOT_GIVEN,
        layer7: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Change the layer4 and layer7 DDoS protection for specific or all IPs.

        **Requires
        24fire+**.

        Args:
          ip_address: If omitted, applies to all IP addresses

          layer4: dynamic, permanent, or off

          layer7: on or off

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return await self._post(
            f"/api/kvm/{internal_id}/ddos/change",
            body=await async_maybe_transform(
                {
                    "ip_address": ip_address,
                    "layer4": layer4,
                    "layer7": layer7,
                },
                ddo_change_params.DdoChangeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class DdosResourceWithRawResponse:
    def __init__(self, ddos: DdosResource) -> None:
        self._ddos = ddos

        self.retrieve = to_raw_response_wrapper(
            ddos.retrieve,
        )
        self.change = to_raw_response_wrapper(
            ddos.change,
        )


class AsyncDdosResourceWithRawResponse:
    def __init__(self, ddos: AsyncDdosResource) -> None:
        self._ddos = ddos

        self.retrieve = async_to_raw_response_wrapper(
            ddos.retrieve,
        )
        self.change = async_to_raw_response_wrapper(
            ddos.change,
        )


class DdosResourceWithStreamingResponse:
    def __init__(self, ddos: DdosResource) -> None:
        self._ddos = ddos

        self.retrieve = to_streamed_response_wrapper(
            ddos.retrieve,
        )
        self.change = to_streamed_response_wrapper(
            ddos.change,
        )


class AsyncDdosResourceWithStreamingResponse:
    def __init__(self, ddos: AsyncDdosResource) -> None:
        self._ddos = ddos

        self.retrieve = async_to_streamed_response_wrapper(
            ddos.retrieve,
        )
        self.change = async_to_streamed_response_wrapper(
            ddos.change,
        )
