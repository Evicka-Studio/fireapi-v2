# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["WebspacesResource", "AsyncWebspacesResource"]


class WebspacesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WebspacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/fireapi-v2-python#accessing-raw-response-data-eg-headers
        """
        return WebspacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebspacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/fireapi-v2-python#with_streaming_response
        """
        return WebspacesResourceWithStreamingResponse(self)

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
        Retrieve information and resource limits of a specific webspace.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return self._get(
            f"/api/webspace/{internal_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncWebspacesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebspacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/fireapi-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebspacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebspacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/fireapi-v2-python#with_streaming_response
        """
        return AsyncWebspacesResourceWithStreamingResponse(self)

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
        Retrieve information and resource limits of a specific webspace.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return await self._get(
            f"/api/webspace/{internal_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class WebspacesResourceWithRawResponse:
    def __init__(self, webspaces: WebspacesResource) -> None:
        self._webspaces = webspaces

        self.retrieve = to_raw_response_wrapper(
            webspaces.retrieve,
        )


class AsyncWebspacesResourceWithRawResponse:
    def __init__(self, webspaces: AsyncWebspacesResource) -> None:
        self._webspaces = webspaces

        self.retrieve = async_to_raw_response_wrapper(
            webspaces.retrieve,
        )


class WebspacesResourceWithStreamingResponse:
    def __init__(self, webspaces: WebspacesResource) -> None:
        self._webspaces = webspaces

        self.retrieve = to_streamed_response_wrapper(
            webspaces.retrieve,
        )


class AsyncWebspacesResourceWithStreamingResponse:
    def __init__(self, webspaces: AsyncWebspacesResource) -> None:
        self._webspaces = webspaces

        self.retrieve = async_to_streamed_response_wrapper(
            webspaces.retrieve,
        )
