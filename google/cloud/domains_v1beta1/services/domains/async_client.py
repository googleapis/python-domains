# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict
import functools
import re
from typing import Dict, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core.client_options import ClientOptions
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.cloud.domains_v1beta1.services.domains import pagers
from google.cloud.domains_v1beta1.types import domains
from google.protobuf import empty_pb2  # type: ignore
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from google.type import money_pb2  # type: ignore
from .transports.base import DomainsTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import DomainsGrpcAsyncIOTransport
from .client import DomainsClient


class DomainsAsyncClient:
    """The Cloud Domains API enables management and configuration of
    domain names.
    """

    _client: DomainsClient

    DEFAULT_ENDPOINT = DomainsClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = DomainsClient.DEFAULT_MTLS_ENDPOINT

    registration_path = staticmethod(DomainsClient.registration_path)
    parse_registration_path = staticmethod(DomainsClient.parse_registration_path)
    common_billing_account_path = staticmethod(
        DomainsClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        DomainsClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(DomainsClient.common_folder_path)
    parse_common_folder_path = staticmethod(DomainsClient.parse_common_folder_path)
    common_organization_path = staticmethod(DomainsClient.common_organization_path)
    parse_common_organization_path = staticmethod(
        DomainsClient.parse_common_organization_path
    )
    common_project_path = staticmethod(DomainsClient.common_project_path)
    parse_common_project_path = staticmethod(DomainsClient.parse_common_project_path)
    common_location_path = staticmethod(DomainsClient.common_location_path)
    parse_common_location_path = staticmethod(DomainsClient.parse_common_location_path)

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            DomainsAsyncClient: The constructed client.
        """
        return DomainsClient.from_service_account_info.__func__(DomainsAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            DomainsAsyncClient: The constructed client.
        """
        return DomainsClient.from_service_account_file.__func__(DomainsAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return DomainsClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> DomainsTransport:
        """Returns the transport used by the client instance.

        Returns:
            DomainsTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(DomainsClient).get_transport_class, type(DomainsClient)
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, DomainsTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the domains client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.DomainsTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = DomainsClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def search_domains(
        self,
        request: Union[domains.SearchDomainsRequest, dict] = None,
        *,
        location: str = None,
        query: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> domains.SearchDomainsResponse:
        r"""Searches for available domain names similar to the provided
        query.

        Availability results from this method are approximate; call
        ``RetrieveRegisterParameters`` on a domain before registering to
        confirm availability.


        .. code-block::

            from google.cloud import domains_v1beta1

            def sample_search_domains():
                # Create a client
                client = domains_v1beta1.DomainsClient()

                # Initialize request argument(s)
                request = domains_v1beta1.SearchDomainsRequest(
                    query="query_value",
                    location="location_value",
                )

                # Make the request
                response = client.search_domains(request=request)

                # Handle response
                print(response)

        Args:
            request (Union[google.cloud.domains_v1beta1.types.SearchDomainsRequest, dict]):
                The request object. Request for the `SearchDomains`
                method.
            location (:class:`str`):
                Required. The location. Must be in the format
                ``projects/*/locations/*``.

                This corresponds to the ``location`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            query (:class:`str`):
                Required. String used to search for
                available domain names.

                This corresponds to the ``query`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.domains_v1beta1.types.SearchDomainsResponse:
                Response for the SearchDomains method.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([location, query])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = domains.SearchDomainsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if location is not None:
            request.location = location
        if query is not None:
            request.query = query

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.search_domains,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("location", request.location),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def retrieve_register_parameters(
        self,
        request: Union[domains.RetrieveRegisterParametersRequest, dict] = None,
        *,
        location: str = None,
        domain_name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> domains.RetrieveRegisterParametersResponse:
        r"""Gets parameters needed to register a new domain name, including
        price and up-to-date availability. Use the returned values to
        call ``RegisterDomain``.


        .. code-block::

            from google.cloud import domains_v1beta1

            def sample_retrieve_register_parameters():
                # Create a client
                client = domains_v1beta1.DomainsClient()

                # Initialize request argument(s)
                request = domains_v1beta1.RetrieveRegisterParametersRequest(
                    domain_name="domain_name_value",
                    location="location_value",
                )

                # Make the request
                response = client.retrieve_register_parameters(request=request)

                # Handle response
                print(response)

        Args:
            request (Union[google.cloud.domains_v1beta1.types.RetrieveRegisterParametersRequest, dict]):
                The request object. Request for the
                `RetrieveRegisterParameters` method.
            location (:class:`str`):
                Required. The location. Must be in the format
                ``projects/*/locations/*``.

                This corresponds to the ``location`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            domain_name (:class:`str`):
                Required. The domain name. Unicode
                domain names must be expressed in
                Punycode format.

                This corresponds to the ``domain_name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.domains_v1beta1.types.RetrieveRegisterParametersResponse:
                Response for the RetrieveRegisterParameters method.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([location, domain_name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = domains.RetrieveRegisterParametersRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if location is not None:
            request.location = location
        if domain_name is not None:
            request.domain_name = domain_name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.retrieve_register_parameters,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("location", request.location),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def register_domain(
        self,
        request: Union[domains.RegisterDomainRequest, dict] = None,
        *,
        parent: str = None,
        registration: domains.Registration = None,
        yearly_price: money_pb2.Money = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Registers a new domain name and creates a corresponding
        ``Registration`` resource.

        Call ``RetrieveRegisterParameters`` first to check availability
        of the domain name and determine parameters like price that are
        needed to build a call to this method.

        A successful call creates a ``Registration`` resource in state
        ``REGISTRATION_PENDING``, which resolves to ``ACTIVE`` within
        1-2 minutes, indicating that the domain was successfully
        registered. If the resource ends up in state
        ``REGISTRATION_FAILED``, it indicates that the domain was not
        registered successfully, and you can safely delete the resource
        and retry registration.


        .. code-block::

            from google.cloud import domains_v1beta1

            def sample_register_domain():
                # Create a client
                client = domains_v1beta1.DomainsClient()

                # Initialize request argument(s)
                registration = domains_v1beta1.Registration()
                registration.domain_name = "domain_name_value"
                registration.contact_settings.privacy = "REDACTED_CONTACT_DATA"
                registration.contact_settings.registrant_contact.email = "email_value"
                registration.contact_settings.registrant_contact.phone_number = "phone_number_value"
                registration.contact_settings.admin_contact.email = "email_value"
                registration.contact_settings.admin_contact.phone_number = "phone_number_value"
                registration.contact_settings.technical_contact.email = "email_value"
                registration.contact_settings.technical_contact.phone_number = "phone_number_value"

                request = domains_v1beta1.RegisterDomainRequest(
                    parent="parent_value",
                    registration=registration,
                )

                # Make the request
                operation = client.register_domain(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()
                print(response)

        Args:
            request (Union[google.cloud.domains_v1beta1.types.RegisterDomainRequest, dict]):
                The request object. Request for the `RegisterDomain`
                method.
            parent (:class:`str`):
                Required. The parent resource of the ``Registration``.
                Must be in the format ``projects/*/locations/*``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            registration (:class:`google.cloud.domains_v1beta1.types.Registration`):
                Required. The complete ``Registration`` resource to be
                created.

                This corresponds to the ``registration`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            yearly_price (:class:`google.type.money_pb2.Money`):
                Required. Yearly price to register or
                renew the domain. The value that should
                be put here can be obtained from
                RetrieveRegisterParameters or
                SearchDomains calls.

                This corresponds to the ``yearly_price`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.domains_v1beta1.types.Registration` The Registration resource facilitates managing and configuring domain name
                   registrations.

                   There are several ways to create a new Registration
                   resource:

                   To create a new Registration resource, find a
                   suitable domain name by calling the SearchDomains
                   method with a query to see available domain name
                   options. After choosing a name, call
                   RetrieveRegisterParameters to ensure availability and
                   obtain information like pricing, which is needed to
                   build a call to RegisterDomain.

                   Another way to create a new Registration is to
                   transfer an existing domain from another registrar.
                   First, go to the current registrar to unlock the
                   domain for transfer and retrieve the domain's
                   transfer authorization code. Then call
                   RetrieveTransferParameters to confirm that the domain
                   is unlocked and to get values needed to build a call
                   to TransferDomain.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, registration, yearly_price])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = domains.RegisterDomainRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if registration is not None:
            request.registration = registration
        if yearly_price is not None:
            request.yearly_price = yearly_price

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.register_domain,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            domains.Registration,
            metadata_type=domains.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def retrieve_transfer_parameters(
        self,
        request: Union[domains.RetrieveTransferParametersRequest, dict] = None,
        *,
        location: str = None,
        domain_name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> domains.RetrieveTransferParametersResponse:
        r"""Gets parameters needed to transfer a domain name from another
        registrar to Cloud Domains. For domains managed by Google
        Domains, transferring to Cloud Domains is not supported.

        Use the returned values to call ``TransferDomain``.


        .. code-block::

            from google.cloud import domains_v1beta1

            def sample_retrieve_transfer_parameters():
                # Create a client
                client = domains_v1beta1.DomainsClient()

                # Initialize request argument(s)
                request = domains_v1beta1.RetrieveTransferParametersRequest(
                    domain_name="domain_name_value",
                    location="location_value",
                )

                # Make the request
                response = client.retrieve_transfer_parameters(request=request)

                # Handle response
                print(response)

        Args:
            request (Union[google.cloud.domains_v1beta1.types.RetrieveTransferParametersRequest, dict]):
                The request object. Request for the
                `RetrieveTransferParameters` method.
            location (:class:`str`):
                Required. The location. Must be in the format
                ``projects/*/locations/*``.

                This corresponds to the ``location`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            domain_name (:class:`str`):
                Required. The domain name. Unicode
                domain names must be expressed in
                Punycode format.

                This corresponds to the ``domain_name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.domains_v1beta1.types.RetrieveTransferParametersResponse:
                Response for the RetrieveTransferParameters method.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([location, domain_name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = domains.RetrieveTransferParametersRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if location is not None:
            request.location = location
        if domain_name is not None:
            request.domain_name = domain_name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.retrieve_transfer_parameters,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("location", request.location),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def transfer_domain(
        self,
        request: Union[domains.TransferDomainRequest, dict] = None,
        *,
        parent: str = None,
        registration: domains.Registration = None,
        yearly_price: money_pb2.Money = None,
        authorization_code: domains.AuthorizationCode = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Transfers a domain name from another registrar to Cloud Domains.
        For domains managed by Google Domains, transferring to Cloud
        Domains is not supported.

        Before calling this method, go to the domain's current registrar
        to unlock the domain for transfer and retrieve the domain's
        transfer authorization code. Then call
        ``RetrieveTransferParameters`` to confirm that the domain is
        unlocked and to get values needed to build a call to this
        method.

        A successful call creates a ``Registration`` resource in state
        ``TRANSFER_PENDING``. It can take several days to complete the
        transfer process. The registrant can often speed up this process
        by approving the transfer through the current registrar, either
        by clicking a link in an email from the registrar or by visiting
        the registrar's website.

        A few minutes after transfer approval, the resource transitions
        to state ``ACTIVE``, indicating that the transfer was
        successful. If the transfer is rejected or the request expires
        without being approved, the resource can end up in state
        ``TRANSFER_FAILED``. If transfer fails, you can safely delete
        the resource and retry the transfer.


        .. code-block::

            from google.cloud import domains_v1beta1

            def sample_transfer_domain():
                # Create a client
                client = domains_v1beta1.DomainsClient()

                # Initialize request argument(s)
                registration = domains_v1beta1.Registration()
                registration.domain_name = "domain_name_value"
                registration.contact_settings.privacy = "REDACTED_CONTACT_DATA"
                registration.contact_settings.registrant_contact.email = "email_value"
                registration.contact_settings.registrant_contact.phone_number = "phone_number_value"
                registration.contact_settings.admin_contact.email = "email_value"
                registration.contact_settings.admin_contact.phone_number = "phone_number_value"
                registration.contact_settings.technical_contact.email = "email_value"
                registration.contact_settings.technical_contact.phone_number = "phone_number_value"

                request = domains_v1beta1.TransferDomainRequest(
                    parent="parent_value",
                    registration=registration,
                )

                # Make the request
                operation = client.transfer_domain(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()
                print(response)

        Args:
            request (Union[google.cloud.domains_v1beta1.types.TransferDomainRequest, dict]):
                The request object. Request for the `TransferDomain`
                method.
            parent (:class:`str`):
                Required. The parent resource of the ``Registration``.
                Must be in the format ``projects/*/locations/*``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            registration (:class:`google.cloud.domains_v1beta1.types.Registration`):
                Required. The complete ``Registration`` resource to be
                created.

                You can leave ``registration.dns_settings`` unset to
                import the domain's current DNS configuration from its
                current registrar. Use this option only if you are sure
                that the domain's current DNS service does not cease
                upon transfer, as is often the case for DNS services
                provided for free by the registrar.

                This corresponds to the ``registration`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            yearly_price (:class:`google.type.money_pb2.Money`):
                Required. Acknowledgement of the price to transfer or
                renew the domain for one year. Call
                ``RetrieveTransferParameters`` to obtain the price,
                which you must acknowledge.

                This corresponds to the ``yearly_price`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            authorization_code (:class:`google.cloud.domains_v1beta1.types.AuthorizationCode`):
                The domain's transfer authorization
                code. You can obtain this from the
                domain's current registrar.

                This corresponds to the ``authorization_code`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.domains_v1beta1.types.Registration` The Registration resource facilitates managing and configuring domain name
                   registrations.

                   There are several ways to create a new Registration
                   resource:

                   To create a new Registration resource, find a
                   suitable domain name by calling the SearchDomains
                   method with a query to see available domain name
                   options. After choosing a name, call
                   RetrieveRegisterParameters to ensure availability and
                   obtain information like pricing, which is needed to
                   build a call to RegisterDomain.

                   Another way to create a new Registration is to
                   transfer an existing domain from another registrar.
                   First, go to the current registrar to unlock the
                   domain for transfer and retrieve the domain's
                   transfer authorization code. Then call
                   RetrieveTransferParameters to confirm that the domain
                   is unlocked and to get values needed to build a call
                   to TransferDomain.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any(
            [parent, registration, yearly_price, authorization_code]
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = domains.TransferDomainRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if registration is not None:
            request.registration = registration
        if yearly_price is not None:
            request.yearly_price = yearly_price
        if authorization_code is not None:
            request.authorization_code = authorization_code

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.transfer_domain,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            domains.Registration,
            metadata_type=domains.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def list_registrations(
        self,
        request: Union[domains.ListRegistrationsRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListRegistrationsAsyncPager:
        r"""Lists the ``Registration`` resources in a project.

        .. code-block::

            from google.cloud import domains_v1beta1

            def sample_list_registrations():
                # Create a client
                client = domains_v1beta1.DomainsClient()

                # Initialize request argument(s)
                request = domains_v1beta1.ListRegistrationsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_registrations(request=request)
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.domains_v1beta1.types.ListRegistrationsRequest, dict]):
                The request object. Request for the `ListRegistrations`
                method.
            parent (:class:`str`):
                Required. The project and location from which to list
                ``Registration``\ s, specified in the format
                ``projects/*/locations/*``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.domains_v1beta1.services.domains.pagers.ListRegistrationsAsyncPager:
                Response for the ListRegistrations method.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = domains.ListRegistrationsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_registrations,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListRegistrationsAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_registration(
        self,
        request: Union[domains.GetRegistrationRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> domains.Registration:
        r"""Gets the details of a ``Registration`` resource.

        .. code-block::

            from google.cloud import domains_v1beta1

            def sample_get_registration():
                # Create a client
                client = domains_v1beta1.DomainsClient()

                # Initialize request argument(s)
                request = domains_v1beta1.GetRegistrationRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_registration(request=request)

                # Handle response
                print(response)

        Args:
            request (Union[google.cloud.domains_v1beta1.types.GetRegistrationRequest, dict]):
                The request object. Request for the `GetRegistration`
                method.
            name (:class:`str`):
                Required. The name of the ``Registration`` to get, in
                the format ``projects/*/locations/*/registrations/*``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.domains_v1beta1.types.Registration:
                The Registration resource facilitates managing and configuring domain name
                   registrations.

                   There are several ways to create a new Registration
                   resource:

                   To create a new Registration resource, find a
                   suitable domain name by calling the SearchDomains
                   method with a query to see available domain name
                   options. After choosing a name, call
                   RetrieveRegisterParameters to ensure availability and
                   obtain information like pricing, which is needed to
                   build a call to RegisterDomain.

                   Another way to create a new Registration is to
                   transfer an existing domain from another registrar.
                   First, go to the current registrar to unlock the
                   domain for transfer and retrieve the domain's
                   transfer authorization code. Then call
                   RetrieveTransferParameters to confirm that the domain
                   is unlocked and to get values needed to build a call
                   to TransferDomain.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = domains.GetRegistrationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_registration,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def update_registration(
        self,
        request: Union[domains.UpdateRegistrationRequest, dict] = None,
        *,
        registration: domains.Registration = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates select fields of a ``Registration`` resource, notably
        ``labels``. To update other fields, use the appropriate custom
        update method:

        -  To update management settings, see
           ``ConfigureManagementSettings``
        -  To update DNS configuration, see ``ConfigureDnsSettings``
        -  To update contact information, see
           ``ConfigureContactSettings``


        .. code-block::

            from google.cloud import domains_v1beta1

            def sample_update_registration():
                # Create a client
                client = domains_v1beta1.DomainsClient()

                # Initialize request argument(s)
                request = domains_v1beta1.UpdateRegistrationRequest(
                )

                # Make the request
                operation = client.update_registration(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()
                print(response)

        Args:
            request (Union[google.cloud.domains_v1beta1.types.UpdateRegistrationRequest, dict]):
                The request object. Request for the `UpdateRegistration`
                method.
            registration (:class:`google.cloud.domains_v1beta1.types.Registration`):
                Fields of the ``Registration`` to update.
                This corresponds to the ``registration`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. The field mask describing which fields to
                update as a comma-separated list. For example, if only
                the labels are being updated, the ``update_mask`` is
                ``"labels"``.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.domains_v1beta1.types.Registration` The Registration resource facilitates managing and configuring domain name
                   registrations.

                   There are several ways to create a new Registration
                   resource:

                   To create a new Registration resource, find a
                   suitable domain name by calling the SearchDomains
                   method with a query to see available domain name
                   options. After choosing a name, call
                   RetrieveRegisterParameters to ensure availability and
                   obtain information like pricing, which is needed to
                   build a call to RegisterDomain.

                   Another way to create a new Registration is to
                   transfer an existing domain from another registrar.
                   First, go to the current registrar to unlock the
                   domain for transfer and retrieve the domain's
                   transfer authorization code. Then call
                   RetrieveTransferParameters to confirm that the domain
                   is unlocked and to get values needed to build a call
                   to TransferDomain.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([registration, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = domains.UpdateRegistrationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if registration is not None:
            request.registration = registration
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_registration,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("registration.name", request.registration.name),)
            ),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            domains.Registration,
            metadata_type=domains.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def configure_management_settings(
        self,
        request: Union[domains.ConfigureManagementSettingsRequest, dict] = None,
        *,
        registration: str = None,
        management_settings: domains.ManagementSettings = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates a ``Registration``'s management settings.

        .. code-block::

            from google.cloud import domains_v1beta1

            def sample_configure_management_settings():
                # Create a client
                client = domains_v1beta1.DomainsClient()

                # Initialize request argument(s)
                request = domains_v1beta1.ConfigureManagementSettingsRequest(
                    registration="registration_value",
                )

                # Make the request
                operation = client.configure_management_settings(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()
                print(response)

        Args:
            request (Union[google.cloud.domains_v1beta1.types.ConfigureManagementSettingsRequest, dict]):
                The request object. Request for the
                `ConfigureManagementSettings` method.
            registration (:class:`str`):
                Required. The name of the ``Registration`` whose
                management settings are being updated, in the format
                ``projects/*/locations/*/registrations/*``.

                This corresponds to the ``registration`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            management_settings (:class:`google.cloud.domains_v1beta1.types.ManagementSettings`):
                Fields of the ``ManagementSettings`` to update.
                This corresponds to the ``management_settings`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. The field mask describing which fields to
                update as a comma-separated list. For example, if only
                the transfer lock is being updated, the ``update_mask``
                is ``"transfer_lock_state"``.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.domains_v1beta1.types.Registration` The Registration resource facilitates managing and configuring domain name
                   registrations.

                   There are several ways to create a new Registration
                   resource:

                   To create a new Registration resource, find a
                   suitable domain name by calling the SearchDomains
                   method with a query to see available domain name
                   options. After choosing a name, call
                   RetrieveRegisterParameters to ensure availability and
                   obtain information like pricing, which is needed to
                   build a call to RegisterDomain.

                   Another way to create a new Registration is to
                   transfer an existing domain from another registrar.
                   First, go to the current registrar to unlock the
                   domain for transfer and retrieve the domain's
                   transfer authorization code. Then call
                   RetrieveTransferParameters to confirm that the domain
                   is unlocked and to get values needed to build a call
                   to TransferDomain.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([registration, management_settings, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = domains.ConfigureManagementSettingsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if registration is not None:
            request.registration = registration
        if management_settings is not None:
            request.management_settings = management_settings
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.configure_management_settings,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("registration", request.registration),)
            ),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            domains.Registration,
            metadata_type=domains.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def configure_dns_settings(
        self,
        request: Union[domains.ConfigureDnsSettingsRequest, dict] = None,
        *,
        registration: str = None,
        dns_settings: domains.DnsSettings = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates a ``Registration``'s DNS settings.

        .. code-block::

            from google.cloud import domains_v1beta1

            def sample_configure_dns_settings():
                # Create a client
                client = domains_v1beta1.DomainsClient()

                # Initialize request argument(s)
                request = domains_v1beta1.ConfigureDnsSettingsRequest(
                    registration="registration_value",
                )

                # Make the request
                operation = client.configure_dns_settings(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()
                print(response)

        Args:
            request (Union[google.cloud.domains_v1beta1.types.ConfigureDnsSettingsRequest, dict]):
                The request object. Request for the
                `ConfigureDnsSettings` method.
            registration (:class:`str`):
                Required. The name of the ``Registration`` whose DNS
                settings are being updated, in the format
                ``projects/*/locations/*/registrations/*``.

                This corresponds to the ``registration`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            dns_settings (:class:`google.cloud.domains_v1beta1.types.DnsSettings`):
                Fields of the ``DnsSettings`` to update.
                This corresponds to the ``dns_settings`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. The field mask describing which fields to
                update as a comma-separated list. For example, if only
                the name servers are being updated for an existing
                Custom DNS configuration, the ``update_mask`` is
                ``"custom_dns.name_servers"``.

                When changing the DNS provider from one type to another,
                pass the new provider's field name as part of the field
                mask. For example, when changing from a Google Domains
                DNS configuration to a Custom DNS configuration, the
                ``update_mask`` is ``"custom_dns"``. //

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.domains_v1beta1.types.Registration` The Registration resource facilitates managing and configuring domain name
                   registrations.

                   There are several ways to create a new Registration
                   resource:

                   To create a new Registration resource, find a
                   suitable domain name by calling the SearchDomains
                   method with a query to see available domain name
                   options. After choosing a name, call
                   RetrieveRegisterParameters to ensure availability and
                   obtain information like pricing, which is needed to
                   build a call to RegisterDomain.

                   Another way to create a new Registration is to
                   transfer an existing domain from another registrar.
                   First, go to the current registrar to unlock the
                   domain for transfer and retrieve the domain's
                   transfer authorization code. Then call
                   RetrieveTransferParameters to confirm that the domain
                   is unlocked and to get values needed to build a call
                   to TransferDomain.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([registration, dns_settings, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = domains.ConfigureDnsSettingsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if registration is not None:
            request.registration = registration
        if dns_settings is not None:
            request.dns_settings = dns_settings
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.configure_dns_settings,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("registration", request.registration),)
            ),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            domains.Registration,
            metadata_type=domains.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def configure_contact_settings(
        self,
        request: Union[domains.ConfigureContactSettingsRequest, dict] = None,
        *,
        registration: str = None,
        contact_settings: domains.ContactSettings = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates a ``Registration``'s contact settings. Some changes
        require confirmation by the domain's registrant contact .


        .. code-block::

            from google.cloud import domains_v1beta1

            def sample_configure_contact_settings():
                # Create a client
                client = domains_v1beta1.DomainsClient()

                # Initialize request argument(s)
                request = domains_v1beta1.ConfigureContactSettingsRequest(
                    registration="registration_value",
                )

                # Make the request
                operation = client.configure_contact_settings(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()
                print(response)

        Args:
            request (Union[google.cloud.domains_v1beta1.types.ConfigureContactSettingsRequest, dict]):
                The request object. Request for the
                `ConfigureContactSettings` method.
            registration (:class:`str`):
                Required. The name of the ``Registration`` whose contact
                settings are being updated, in the format
                ``projects/*/locations/*/registrations/*``.

                This corresponds to the ``registration`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            contact_settings (:class:`google.cloud.domains_v1beta1.types.ContactSettings`):
                Fields of the ``ContactSettings`` to update.
                This corresponds to the ``contact_settings`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. The field mask describing which fields to
                update as a comma-separated list. For example, if only
                the registrant contact is being updated, the
                ``update_mask`` is ``"registrant_contact"``.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.domains_v1beta1.types.Registration` The Registration resource facilitates managing and configuring domain name
                   registrations.

                   There are several ways to create a new Registration
                   resource:

                   To create a new Registration resource, find a
                   suitable domain name by calling the SearchDomains
                   method with a query to see available domain name
                   options. After choosing a name, call
                   RetrieveRegisterParameters to ensure availability and
                   obtain information like pricing, which is needed to
                   build a call to RegisterDomain.

                   Another way to create a new Registration is to
                   transfer an existing domain from another registrar.
                   First, go to the current registrar to unlock the
                   domain for transfer and retrieve the domain's
                   transfer authorization code. Then call
                   RetrieveTransferParameters to confirm that the domain
                   is unlocked and to get values needed to build a call
                   to TransferDomain.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([registration, contact_settings, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = domains.ConfigureContactSettingsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if registration is not None:
            request.registration = registration
        if contact_settings is not None:
            request.contact_settings = contact_settings
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.configure_contact_settings,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("registration", request.registration),)
            ),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            domains.Registration,
            metadata_type=domains.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def export_registration(
        self,
        request: Union[domains.ExportRegistrationRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Exports a ``Registration`` resource, such that it is no longer
        managed by Cloud Domains.

        When an active domain is successfully exported, you can continue
        to use the domain in `Google
        Domains <https://domains.google/>`__ until it expires. The
        calling user becomes the domain's sole owner in Google Domains,
        and permissions for the domain are subsequently managed there.
        The domain does not renew automatically unless the new owner
        sets up billing in Google Domains.


        .. code-block::

            from google.cloud import domains_v1beta1

            def sample_export_registration():
                # Create a client
                client = domains_v1beta1.DomainsClient()

                # Initialize request argument(s)
                request = domains_v1beta1.ExportRegistrationRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.export_registration(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()
                print(response)

        Args:
            request (Union[google.cloud.domains_v1beta1.types.ExportRegistrationRequest, dict]):
                The request object. Request for the `ExportRegistration`
                method.
            name (:class:`str`):
                Required. The name of the ``Registration`` to export, in
                the format ``projects/*/locations/*/registrations/*``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.domains_v1beta1.types.Registration` The Registration resource facilitates managing and configuring domain name
                   registrations.

                   There are several ways to create a new Registration
                   resource:

                   To create a new Registration resource, find a
                   suitable domain name by calling the SearchDomains
                   method with a query to see available domain name
                   options. After choosing a name, call
                   RetrieveRegisterParameters to ensure availability and
                   obtain information like pricing, which is needed to
                   build a call to RegisterDomain.

                   Another way to create a new Registration is to
                   transfer an existing domain from another registrar.
                   First, go to the current registrar to unlock the
                   domain for transfer and retrieve the domain's
                   transfer authorization code. Then call
                   RetrieveTransferParameters to confirm that the domain
                   is unlocked and to get values needed to build a call
                   to TransferDomain.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = domains.ExportRegistrationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.export_registration,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            domains.Registration,
            metadata_type=domains.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def delete_registration(
        self,
        request: Union[domains.DeleteRegistrationRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes a ``Registration`` resource.

        This method works on any ``Registration`` resource using
        `Subscription or Commitment
        billing </domains/pricing#billing-models>`__, provided that the
        resource was created at least 1 day in the past.

        For ``Registration`` resources using `Monthly
        billing </domains/pricing#billing-models>`__, this method works
        if:

        -  ``state`` is ``EXPORTED`` with ``expire_time`` in the past
        -  ``state`` is ``REGISTRATION_FAILED``
        -  ``state`` is ``TRANSFER_FAILED``

        When an active registration is successfully deleted, you can
        continue to use the domain in `Google
        Domains <https://domains.google/>`__ until it expires. The
        calling user becomes the domain's sole owner in Google Domains,
        and permissions for the domain are subsequently managed there.
        The domain does not renew automatically unless the new owner
        sets up billing in Google Domains.


        .. code-block::

            from google.cloud import domains_v1beta1

            def sample_delete_registration():
                # Create a client
                client = domains_v1beta1.DomainsClient()

                # Initialize request argument(s)
                request = domains_v1beta1.DeleteRegistrationRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_registration(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()
                print(response)

        Args:
            request (Union[google.cloud.domains_v1beta1.types.DeleteRegistrationRequest, dict]):
                The request object. Request for the `DeleteRegistration`
                method.
            name (:class:`str`):
                Required. The name of the ``Registration`` to delete, in
                the format ``projects/*/locations/*/registrations/*``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

                   The JSON representation for Empty is empty JSON
                   object {}.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = domains.DeleteRegistrationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_registration,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=domains.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def retrieve_authorization_code(
        self,
        request: Union[domains.RetrieveAuthorizationCodeRequest, dict] = None,
        *,
        registration: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> domains.AuthorizationCode:
        r"""Gets the authorization code of the ``Registration`` for the
        purpose of transferring the domain to another registrar.

        You can call this method only after 60 days have elapsed since
        the initial domain registration.


        .. code-block::

            from google.cloud import domains_v1beta1

            def sample_retrieve_authorization_code():
                # Create a client
                client = domains_v1beta1.DomainsClient()

                # Initialize request argument(s)
                request = domains_v1beta1.RetrieveAuthorizationCodeRequest(
                    registration="registration_value",
                )

                # Make the request
                response = client.retrieve_authorization_code(request=request)

                # Handle response
                print(response)

        Args:
            request (Union[google.cloud.domains_v1beta1.types.RetrieveAuthorizationCodeRequest, dict]):
                The request object. Request for the
                `RetrieveAuthorizationCode` method.
            registration (:class:`str`):
                Required. The name of the ``Registration`` whose
                authorization code is being retrieved, in the format
                ``projects/*/locations/*/registrations/*``.

                This corresponds to the ``registration`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.domains_v1beta1.types.AuthorizationCode:
                Defines an authorization code.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([registration])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = domains.RetrieveAuthorizationCodeRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if registration is not None:
            request.registration = registration

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.retrieve_authorization_code,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("registration", request.registration),)
            ),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def reset_authorization_code(
        self,
        request: Union[domains.ResetAuthorizationCodeRequest, dict] = None,
        *,
        registration: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> domains.AuthorizationCode:
        r"""Resets the authorization code of the ``Registration`` to a new
        random string.

        You can call this method only after 60 days have elapsed since
        the initial domain registration.


        .. code-block::

            from google.cloud import domains_v1beta1

            def sample_reset_authorization_code():
                # Create a client
                client = domains_v1beta1.DomainsClient()

                # Initialize request argument(s)
                request = domains_v1beta1.ResetAuthorizationCodeRequest(
                    registration="registration_value",
                )

                # Make the request
                response = client.reset_authorization_code(request=request)

                # Handle response
                print(response)

        Args:
            request (Union[google.cloud.domains_v1beta1.types.ResetAuthorizationCodeRequest, dict]):
                The request object. Request for the
                `ResetAuthorizationCode` method.
            registration (:class:`str`):
                Required. The name of the ``Registration`` whose
                authorization code is being reset, in the format
                ``projects/*/locations/*/registrations/*``.

                This corresponds to the ``registration`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.domains_v1beta1.types.AuthorizationCode:
                Defines an authorization code.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([registration])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = domains.ResetAuthorizationCodeRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if registration is not None:
            request.registration = registration

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.reset_authorization_code,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("registration", request.registration),)
            ),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution("google-cloud-domains",).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("DomainsAsyncClient",)
