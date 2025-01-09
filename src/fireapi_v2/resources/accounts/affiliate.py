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

__all__ = ["AffiliateResource", "AsyncAffiliateResource"]


class AffiliateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AffiliateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EvickaStudio/fireapi-v2#accessing-raw-response-data-eg-headers
        """
        return AffiliateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AffiliateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EvickaStudio/fireapi-v2#with_streaming_response
        """
        return AffiliateResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Get an overview of the affiliate system data, leads, stats, etc."""
        return self._get(
            "/api/account/affiliate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncAffiliateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAffiliateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EvickaStudio/fireapi-v2#accessing-raw-response-data-eg-headers
        """
        return AsyncAffiliateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAffiliateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EvickaStudio/fireapi-v2#with_streaming_response
        """
        return AsyncAffiliateResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Get an overview of the affiliate system data, leads, stats, etc."""
        return await self._get(
            "/api/account/affiliate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AffiliateResourceWithRawResponse:
    def __init__(self, affiliate: AffiliateResource) -> None:
        self._affiliate = affiliate

        self.retrieve = to_raw_response_wrapper(
            affiliate.retrieve,
        )


class AsyncAffiliateResourceWithRawResponse:
    def __init__(self, affiliate: AsyncAffiliateResource) -> None:
        self._affiliate = affiliate

        self.retrieve = async_to_raw_response_wrapper(
            affiliate.retrieve,
        )


class AffiliateResourceWithStreamingResponse:
    def __init__(self, affiliate: AffiliateResource) -> None:
        self._affiliate = affiliate

        self.retrieve = to_streamed_response_wrapper(
            affiliate.retrieve,
        )


class AsyncAffiliateResourceWithStreamingResponse:
    def __init__(self, affiliate: AsyncAffiliateResource) -> None:
        self._affiliate = affiliate

        self.retrieve = async_to_streamed_response_wrapper(
            affiliate.retrieve,
        )
