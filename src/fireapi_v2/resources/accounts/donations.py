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

__all__ = ["DonationsResource", "AsyncDonationsResource"]


class DonationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DonationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/fireapi-v2-python#accessing-raw-response-data-eg-headers
        """
        return DonationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DonationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/fireapi-v2-python#with_streaming_response
        """
        return DonationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Get all information about your donation page, plus donation logs."""
        return self._get(
            "/api/account/donations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncDonationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDonationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/fireapi-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDonationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDonationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/fireapi-v2-python#with_streaming_response
        """
        return AsyncDonationsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Get all information about your donation page, plus donation logs."""
        return await self._get(
            "/api/account/donations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class DonationsResourceWithRawResponse:
    def __init__(self, donations: DonationsResource) -> None:
        self._donations = donations

        self.list = to_raw_response_wrapper(
            donations.list,
        )


class AsyncDonationsResourceWithRawResponse:
    def __init__(self, donations: AsyncDonationsResource) -> None:
        self._donations = donations

        self.list = async_to_raw_response_wrapper(
            donations.list,
        )


class DonationsResourceWithStreamingResponse:
    def __init__(self, donations: DonationsResource) -> None:
        self._donations = donations

        self.list = to_streamed_response_wrapper(
            donations.list,
        )


class AsyncDonationsResourceWithStreamingResponse:
    def __init__(self, donations: AsyncDonationsResource) -> None:
        self._donations = donations

        self.list = async_to_streamed_response_wrapper(
            donations.list,
        )
