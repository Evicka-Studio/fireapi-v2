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
from ..._base_client import make_request_options
from ...types.domains import dns_add_params, dns_edit_params, dns_remove_params

__all__ = ["DNSResource", "AsyncDNSResource"]


class DNSResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DNSResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/fireapi-v2-python#accessing-raw-response-data-eg-headers
        """
        return DNSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DNSResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/fireapi-v2-python#with_streaming_response
        """
        return DNSResourceWithStreamingResponse(self)

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
        Fetch all DNS entries for the specified domain.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return self._get(
            f"/api/domain/{internal_id}/dns",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def add(
        self,
        internal_id: str,
        *,
        data: str,
        name: str,
        type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Add a DNS entry for the given domain.

        **Requires 24fire+**.

        Args:
          data: The content/value of the record.

          name: Subdomain name. Use `*` if needed.

          type: DNS record type (e.g., A, AAAA, TXT, etc.)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return self._put(
            f"/api/domain/{internal_id}/dns/add",
            body=maybe_transform(
                {
                    "data": data,
                    "name": name,
                    "type": type,
                },
                dns_add_params.DNSAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def edit(
        self,
        internal_id: str,
        *,
        record_id: str,
        data: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Edit a DNS entry for the given domain.

        **Requires 24fire+**.

        Args:
          data: New content if changing

          name: New name if changing

          type: New type if changing (e.g., A, AAAA, TXT, etc.)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return self._post(
            f"/api/domain/{internal_id}/dns/edit",
            body=maybe_transform(
                {
                    "record_id": record_id,
                    "data": data,
                    "name": name,
                    "type": type,
                },
                dns_edit_params.DNSEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def remove(
        self,
        internal_id: str,
        *,
        record_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Remove a DNS entry for the given domain.

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
            f"/api/domain/{internal_id}/dns/remove",
            body=maybe_transform({"record_id": record_id}, dns_remove_params.DNSRemoveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncDNSResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDNSResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/fireapi-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDNSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDNSResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/fireapi-v2-python#with_streaming_response
        """
        return AsyncDNSResourceWithStreamingResponse(self)

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
        Fetch all DNS entries for the specified domain.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return await self._get(
            f"/api/domain/{internal_id}/dns",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def add(
        self,
        internal_id: str,
        *,
        data: str,
        name: str,
        type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Add a DNS entry for the given domain.

        **Requires 24fire+**.

        Args:
          data: The content/value of the record.

          name: Subdomain name. Use `*` if needed.

          type: DNS record type (e.g., A, AAAA, TXT, etc.)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return await self._put(
            f"/api/domain/{internal_id}/dns/add",
            body=await async_maybe_transform(
                {
                    "data": data,
                    "name": name,
                    "type": type,
                },
                dns_add_params.DNSAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def edit(
        self,
        internal_id: str,
        *,
        record_id: str,
        data: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Edit a DNS entry for the given domain.

        **Requires 24fire+**.

        Args:
          data: New content if changing

          name: New name if changing

          type: New type if changing (e.g., A, AAAA, TXT, etc.)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not internal_id:
            raise ValueError(f"Expected a non-empty value for `internal_id` but received {internal_id!r}")
        return await self._post(
            f"/api/domain/{internal_id}/dns/edit",
            body=await async_maybe_transform(
                {
                    "record_id": record_id,
                    "data": data,
                    "name": name,
                    "type": type,
                },
                dns_edit_params.DNSEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def remove(
        self,
        internal_id: str,
        *,
        record_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Remove a DNS entry for the given domain.

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
            f"/api/domain/{internal_id}/dns/remove",
            body=await async_maybe_transform({"record_id": record_id}, dns_remove_params.DNSRemoveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class DNSResourceWithRawResponse:
    def __init__(self, dns: DNSResource) -> None:
        self._dns = dns

        self.retrieve = to_raw_response_wrapper(
            dns.retrieve,
        )
        self.add = to_raw_response_wrapper(
            dns.add,
        )
        self.edit = to_raw_response_wrapper(
            dns.edit,
        )
        self.remove = to_raw_response_wrapper(
            dns.remove,
        )


class AsyncDNSResourceWithRawResponse:
    def __init__(self, dns: AsyncDNSResource) -> None:
        self._dns = dns

        self.retrieve = async_to_raw_response_wrapper(
            dns.retrieve,
        )
        self.add = async_to_raw_response_wrapper(
            dns.add,
        )
        self.edit = async_to_raw_response_wrapper(
            dns.edit,
        )
        self.remove = async_to_raw_response_wrapper(
            dns.remove,
        )


class DNSResourceWithStreamingResponse:
    def __init__(self, dns: DNSResource) -> None:
        self._dns = dns

        self.retrieve = to_streamed_response_wrapper(
            dns.retrieve,
        )
        self.add = to_streamed_response_wrapper(
            dns.add,
        )
        self.edit = to_streamed_response_wrapper(
            dns.edit,
        )
        self.remove = to_streamed_response_wrapper(
            dns.remove,
        )


class AsyncDNSResourceWithStreamingResponse:
    def __init__(self, dns: AsyncDNSResource) -> None:
        self._dns = dns

        self.retrieve = async_to_streamed_response_wrapper(
            dns.retrieve,
        )
        self.add = async_to_streamed_response_wrapper(
            dns.add,
        )
        self.edit = async_to_streamed_response_wrapper(
            dns.edit,
        )
        self.remove = async_to_streamed_response_wrapper(
            dns.remove,
        )
