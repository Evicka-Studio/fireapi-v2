# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import webspaces
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, FireapiV2Error
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.kvm import kvm
from .resources.kvms import kvms
from .resources.domains import domains
from .resources.accounts import accounts

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "FireapiV2",
    "AsyncFireapiV2",
    "Client",
    "AsyncClient",
]


class FireapiV2(SyncAPIClient):
    accounts: accounts.AccountsResource
    domains: domains.DomainsResource
    kvms: kvms.KvmsResource
    kvm: kvm.KvmResource
    webspaces: webspaces.WebspacesResource
    with_raw_response: FireapiV2WithRawResponse
    with_streaming_response: FireapiV2WithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous fireapi-v2 client instance.

        This automatically infers the `api_key` argument from the `X_FIRE_APIKEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("X_FIRE_APIKEY")
        if api_key is None:
            raise FireapiV2Error(
                "The api_key client option must be set either by passing api_key to the client or by setting the X_FIRE_APIKEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("FIREAPI_V2_BASE_URL")
        if base_url is None:
            base_url = f"https://manage.24fire.de"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.accounts = accounts.AccountsResource(self)
        self.domains = domains.DomainsResource(self)
        self.kvms = kvms.KvmsResource(self)
        self.kvm = kvm.KvmResource(self)
        self.webspaces = webspaces.WebspacesResource(self)
        self.with_raw_response = FireapiV2WithRawResponse(self)
        self.with_streaming_response = FireapiV2WithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-Fire-Apikey": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncFireapiV2(AsyncAPIClient):
    accounts: accounts.AsyncAccountsResource
    domains: domains.AsyncDomainsResource
    kvms: kvms.AsyncKvmsResource
    kvm: kvm.AsyncKvmResource
    webspaces: webspaces.AsyncWebspacesResource
    with_raw_response: AsyncFireapiV2WithRawResponse
    with_streaming_response: AsyncFireapiV2WithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async fireapi-v2 client instance.

        This automatically infers the `api_key` argument from the `X_FIRE_APIKEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("X_FIRE_APIKEY")
        if api_key is None:
            raise FireapiV2Error(
                "The api_key client option must be set either by passing api_key to the client or by setting the X_FIRE_APIKEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("FIREAPI_V2_BASE_URL")
        if base_url is None:
            base_url = f"https://manage.24fire.de"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.accounts = accounts.AsyncAccountsResource(self)
        self.domains = domains.AsyncDomainsResource(self)
        self.kvms = kvms.AsyncKvmsResource(self)
        self.kvm = kvm.AsyncKvmResource(self)
        self.webspaces = webspaces.AsyncWebspacesResource(self)
        self.with_raw_response = AsyncFireapiV2WithRawResponse(self)
        self.with_streaming_response = AsyncFireapiV2WithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-Fire-Apikey": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class FireapiV2WithRawResponse:
    def __init__(self, client: FireapiV2) -> None:
        self.accounts = accounts.AccountsResourceWithRawResponse(client.accounts)
        self.domains = domains.DomainsResourceWithRawResponse(client.domains)
        self.kvms = kvms.KvmsResourceWithRawResponse(client.kvms)
        self.kvm = kvm.KvmResourceWithRawResponse(client.kvm)
        self.webspaces = webspaces.WebspacesResourceWithRawResponse(client.webspaces)


class AsyncFireapiV2WithRawResponse:
    def __init__(self, client: AsyncFireapiV2) -> None:
        self.accounts = accounts.AsyncAccountsResourceWithRawResponse(client.accounts)
        self.domains = domains.AsyncDomainsResourceWithRawResponse(client.domains)
        self.kvms = kvms.AsyncKvmsResourceWithRawResponse(client.kvms)
        self.kvm = kvm.AsyncKvmResourceWithRawResponse(client.kvm)
        self.webspaces = webspaces.AsyncWebspacesResourceWithRawResponse(client.webspaces)


class FireapiV2WithStreamedResponse:
    def __init__(self, client: FireapiV2) -> None:
        self.accounts = accounts.AccountsResourceWithStreamingResponse(client.accounts)
        self.domains = domains.DomainsResourceWithStreamingResponse(client.domains)
        self.kvms = kvms.KvmsResourceWithStreamingResponse(client.kvms)
        self.kvm = kvm.KvmResourceWithStreamingResponse(client.kvm)
        self.webspaces = webspaces.WebspacesResourceWithStreamingResponse(client.webspaces)


class AsyncFireapiV2WithStreamedResponse:
    def __init__(self, client: AsyncFireapiV2) -> None:
        self.accounts = accounts.AsyncAccountsResourceWithStreamingResponse(client.accounts)
        self.domains = domains.AsyncDomainsResourceWithStreamingResponse(client.domains)
        self.kvms = kvms.AsyncKvmsResourceWithStreamingResponse(client.kvms)
        self.kvm = kvm.AsyncKvmResourceWithStreamingResponse(client.kvm)
        self.webspaces = webspaces.AsyncWebspacesResourceWithStreamingResponse(client.webspaces)


Client = FireapiV2

AsyncClient = AsyncFireapiV2
