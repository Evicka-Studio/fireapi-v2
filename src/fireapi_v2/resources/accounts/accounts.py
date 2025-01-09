# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .services import (
    ServicesResource,
    AsyncServicesResource,
    ServicesResourceWithRawResponse,
    AsyncServicesResourceWithRawResponse,
    ServicesResourceWithStreamingResponse,
    AsyncServicesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .affiliate import (
    AffiliateResource,
    AsyncAffiliateResource,
    AffiliateResourceWithRawResponse,
    AsyncAffiliateResourceWithRawResponse,
    AffiliateResourceWithStreamingResponse,
    AsyncAffiliateResourceWithStreamingResponse,
)
from .donations import (
    DonationsResource,
    AsyncDonationsResource,
    DonationsResourceWithRawResponse,
    AsyncDonationsResourceWithRawResponse,
    DonationsResourceWithStreamingResponse,
    AsyncDonationsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.account_info import AccountInfo

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    @cached_property
    def services(self) -> ServicesResource:
        return ServicesResource(self._client)

    @cached_property
    def donations(self) -> DonationsResource:
        return DonationsResource(self._client)

    @cached_property
    def affiliate(self) -> AffiliateResource:
        return AffiliateResource(self._client)

    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EvickaStudio/fireapi-v2#accessing-raw-response-data-eg-headers
        """
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EvickaStudio/fireapi-v2#with_streaming_response
        """
        return AccountsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountInfo:
        """Get the information of your 24fire account."""
        return self._get(
            "/api/account",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountInfo,
        )


class AsyncAccountsResource(AsyncAPIResource):
    @cached_property
    def services(self) -> AsyncServicesResource:
        return AsyncServicesResource(self._client)

    @cached_property
    def donations(self) -> AsyncDonationsResource:
        return AsyncDonationsResource(self._client)

    @cached_property
    def affiliate(self) -> AsyncAffiliateResource:
        return AsyncAffiliateResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EvickaStudio/fireapi-v2#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EvickaStudio/fireapi-v2#with_streaming_response
        """
        return AsyncAccountsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountInfo:
        """Get the information of your 24fire account."""
        return await self._get(
            "/api/account",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountInfo,
        )


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = to_raw_response_wrapper(
            accounts.retrieve,
        )

    @cached_property
    def services(self) -> ServicesResourceWithRawResponse:
        return ServicesResourceWithRawResponse(self._accounts.services)

    @cached_property
    def donations(self) -> DonationsResourceWithRawResponse:
        return DonationsResourceWithRawResponse(self._accounts.donations)

    @cached_property
    def affiliate(self) -> AffiliateResourceWithRawResponse:
        return AffiliateResourceWithRawResponse(self._accounts.affiliate)


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = async_to_raw_response_wrapper(
            accounts.retrieve,
        )

    @cached_property
    def services(self) -> AsyncServicesResourceWithRawResponse:
        return AsyncServicesResourceWithRawResponse(self._accounts.services)

    @cached_property
    def donations(self) -> AsyncDonationsResourceWithRawResponse:
        return AsyncDonationsResourceWithRawResponse(self._accounts.donations)

    @cached_property
    def affiliate(self) -> AsyncAffiliateResourceWithRawResponse:
        return AsyncAffiliateResourceWithRawResponse(self._accounts.affiliate)


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = to_streamed_response_wrapper(
            accounts.retrieve,
        )

    @cached_property
    def services(self) -> ServicesResourceWithStreamingResponse:
        return ServicesResourceWithStreamingResponse(self._accounts.services)

    @cached_property
    def donations(self) -> DonationsResourceWithStreamingResponse:
        return DonationsResourceWithStreamingResponse(self._accounts.donations)

    @cached_property
    def affiliate(self) -> AffiliateResourceWithStreamingResponse:
        return AffiliateResourceWithStreamingResponse(self._accounts.affiliate)


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = async_to_streamed_response_wrapper(
            accounts.retrieve,
        )

    @cached_property
    def services(self) -> AsyncServicesResourceWithStreamingResponse:
        return AsyncServicesResourceWithStreamingResponse(self._accounts.services)

    @cached_property
    def donations(self) -> AsyncDonationsResourceWithStreamingResponse:
        return AsyncDonationsResourceWithStreamingResponse(self._accounts.donations)

    @cached_property
    def affiliate(self) -> AsyncAffiliateResourceWithStreamingResponse:
        return AsyncAffiliateResourceWithStreamingResponse(self._accounts.affiliate)
