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
import warnings
from typing import Awaitable, Callable, Dict, Optional, Sequence, Tuple, Union

from google.api_core import gapic_v1  # type: ignore
from google.api_core import grpc_helpers_async  # type: ignore
from google.api_core import operations_v1  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
import packaging.version

import grpc  # type: ignore
from grpc.experimental import aio  # type: ignore

from google.cloud.domains_v1beta1.types import domains
from google.longrunning import operations_pb2  # type: ignore
from .base import DomainsTransport, DEFAULT_CLIENT_INFO
from .grpc import DomainsGrpcTransport


class DomainsGrpcAsyncIOTransport(DomainsTransport):
    """gRPC AsyncIO backend transport for Domains.

    The Cloud Domains API enables management and configuration of
    domain names.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _grpc_channel: aio.Channel
    _stubs: Dict[str, Callable] = {}

    @classmethod
    def create_channel(
        cls,
        host: str = "domains.googleapis.com",
        credentials: ga_credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> aio.Channel:
        """Create and return a gRPC AsyncIO channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            aio.Channel: A gRPC AsyncIO channel object.
        """

        return grpc_helpers_async.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs,
        )

    def __init__(
        self,
        *,
        host: str = "domains.googleapis.com",
        credentials: ga_credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        channel: aio.Channel = None,
        api_mtls_endpoint: str = None,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
        ssl_channel_credentials: grpc.ChannelCredentials = None,
        client_cert_source_for_mtls: Callable[[], Tuple[bytes, bytes]] = None,
        quota_project_id=None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            channel (Optional[aio.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or applicatin default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for grpc channel. It is ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure mutual TLS channel. It is
                ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}
        self._operations_client = None

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if channel:
            # Ignore credentials if a channel was passed.
            credentials = False
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None
        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
        )

        if not self._grpc_channel:
            self._grpc_channel = type(self).create_channel(
                self._host,
                credentials=self._credentials,
                credentials_file=credentials_file,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @property
    def grpc_channel(self) -> aio.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Return the channel from cache.
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsAsyncClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Sanity check: Only create a new client if we do not already have one.
        if self._operations_client is None:
            self._operations_client = operations_v1.OperationsAsyncClient(
                self.grpc_channel
            )

        # Return the client from cache.
        return self._operations_client

    @property
    def search_domains(
        self,
    ) -> Callable[
        [domains.SearchDomainsRequest], Awaitable[domains.SearchDomainsResponse]
    ]:
        r"""Return a callable for the search domains method over gRPC.

        Searches for available domain names similar to the provided
        query.

        Availability results from this method are approximate; call
        ``RetrieveRegisterParameters`` on a domain before registering to
        confirm availability.

        Returns:
            Callable[[~.SearchDomainsRequest],
                    Awaitable[~.SearchDomainsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_domains" not in self._stubs:
            self._stubs["search_domains"] = self.grpc_channel.unary_unary(
                "/google.cloud.domains.v1beta1.Domains/SearchDomains",
                request_serializer=domains.SearchDomainsRequest.serialize,
                response_deserializer=domains.SearchDomainsResponse.deserialize,
            )
        return self._stubs["search_domains"]

    @property
    def retrieve_register_parameters(
        self,
    ) -> Callable[
        [domains.RetrieveRegisterParametersRequest],
        Awaitable[domains.RetrieveRegisterParametersResponse],
    ]:
        r"""Return a callable for the retrieve register parameters method over gRPC.

        Gets parameters needed to register a new domain name, including
        price and up-to-date availability. Use the returned values to
        call ``RegisterDomain``.

        Returns:
            Callable[[~.RetrieveRegisterParametersRequest],
                    Awaitable[~.RetrieveRegisterParametersResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "retrieve_register_parameters" not in self._stubs:
            self._stubs["retrieve_register_parameters"] = self.grpc_channel.unary_unary(
                "/google.cloud.domains.v1beta1.Domains/RetrieveRegisterParameters",
                request_serializer=domains.RetrieveRegisterParametersRequest.serialize,
                response_deserializer=domains.RetrieveRegisterParametersResponse.deserialize,
            )
        return self._stubs["retrieve_register_parameters"]

    @property
    def register_domain(
        self,
    ) -> Callable[[domains.RegisterDomainRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the register domain method over gRPC.

        Registers a new domain name and creates a corresponding
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

        Returns:
            Callable[[~.RegisterDomainRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "register_domain" not in self._stubs:
            self._stubs["register_domain"] = self.grpc_channel.unary_unary(
                "/google.cloud.domains.v1beta1.Domains/RegisterDomain",
                request_serializer=domains.RegisterDomainRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["register_domain"]

    @property
    def list_registrations(
        self,
    ) -> Callable[
        [domains.ListRegistrationsRequest], Awaitable[domains.ListRegistrationsResponse]
    ]:
        r"""Return a callable for the list registrations method over gRPC.

        Lists the ``Registration`` resources in a project.

        Returns:
            Callable[[~.ListRegistrationsRequest],
                    Awaitable[~.ListRegistrationsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_registrations" not in self._stubs:
            self._stubs["list_registrations"] = self.grpc_channel.unary_unary(
                "/google.cloud.domains.v1beta1.Domains/ListRegistrations",
                request_serializer=domains.ListRegistrationsRequest.serialize,
                response_deserializer=domains.ListRegistrationsResponse.deserialize,
            )
        return self._stubs["list_registrations"]

    @property
    def get_registration(
        self,
    ) -> Callable[[domains.GetRegistrationRequest], Awaitable[domains.Registration]]:
        r"""Return a callable for the get registration method over gRPC.

        Gets the details of a ``Registration`` resource.

        Returns:
            Callable[[~.GetRegistrationRequest],
                    Awaitable[~.Registration]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_registration" not in self._stubs:
            self._stubs["get_registration"] = self.grpc_channel.unary_unary(
                "/google.cloud.domains.v1beta1.Domains/GetRegistration",
                request_serializer=domains.GetRegistrationRequest.serialize,
                response_deserializer=domains.Registration.deserialize,
            )
        return self._stubs["get_registration"]

    @property
    def update_registration(
        self,
    ) -> Callable[
        [domains.UpdateRegistrationRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update registration method over gRPC.

        Updates select fields of a ``Registration`` resource, notably
        ``labels``. To update other fields, use the appropriate custom
        update method:

        -  To update management settings, see
           ``ConfigureManagementSettings``
        -  To update DNS configuration, see ``ConfigureDnsSettings``
        -  To update contact information, see
           ``ConfigureContactSettings``

        Returns:
            Callable[[~.UpdateRegistrationRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_registration" not in self._stubs:
            self._stubs["update_registration"] = self.grpc_channel.unary_unary(
                "/google.cloud.domains.v1beta1.Domains/UpdateRegistration",
                request_serializer=domains.UpdateRegistrationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_registration"]

    @property
    def configure_management_settings(
        self,
    ) -> Callable[
        [domains.ConfigureManagementSettingsRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the configure management settings method over gRPC.

        Updates a ``Registration``'s management settings.

        Returns:
            Callable[[~.ConfigureManagementSettingsRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "configure_management_settings" not in self._stubs:
            self._stubs[
                "configure_management_settings"
            ] = self.grpc_channel.unary_unary(
                "/google.cloud.domains.v1beta1.Domains/ConfigureManagementSettings",
                request_serializer=domains.ConfigureManagementSettingsRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["configure_management_settings"]

    @property
    def configure_dns_settings(
        self,
    ) -> Callable[
        [domains.ConfigureDnsSettingsRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the configure dns settings method over gRPC.

        Updates a ``Registration``'s DNS settings.

        Returns:
            Callable[[~.ConfigureDnsSettingsRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "configure_dns_settings" not in self._stubs:
            self._stubs["configure_dns_settings"] = self.grpc_channel.unary_unary(
                "/google.cloud.domains.v1beta1.Domains/ConfigureDnsSettings",
                request_serializer=domains.ConfigureDnsSettingsRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["configure_dns_settings"]

    @property
    def configure_contact_settings(
        self,
    ) -> Callable[
        [domains.ConfigureContactSettingsRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the configure contact settings method over gRPC.

        Updates a ``Registration``'s contact settings. Some changes
        require confirmation by the domain's registrant contact .

        Returns:
            Callable[[~.ConfigureContactSettingsRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "configure_contact_settings" not in self._stubs:
            self._stubs["configure_contact_settings"] = self.grpc_channel.unary_unary(
                "/google.cloud.domains.v1beta1.Domains/ConfigureContactSettings",
                request_serializer=domains.ConfigureContactSettingsRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["configure_contact_settings"]

    @property
    def export_registration(
        self,
    ) -> Callable[
        [domains.ExportRegistrationRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the export registration method over gRPC.

        Exports a ``Registration`` that you no longer want to use with
        Cloud Domains. You can continue to use the domain in `Google
        Domains <https://domains.google/>`__ until it expires.

        If the export is successful:

        -  The resource's ``state`` becomes ``EXPORTED``, meaning that
           it is no longer managed by Cloud Domains
        -  Because individual users can own domains in Google Domains,
           the calling user becomes the domain's sole owner. Permissions
           for the domain are subsequently managed in Google Domains.
        -  Without further action, the domain does not renew
           automatically. The new owner can set up billing in Google
           Domains to renew the domain if needed.

        Returns:
            Callable[[~.ExportRegistrationRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "export_registration" not in self._stubs:
            self._stubs["export_registration"] = self.grpc_channel.unary_unary(
                "/google.cloud.domains.v1beta1.Domains/ExportRegistration",
                request_serializer=domains.ExportRegistrationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["export_registration"]

    @property
    def delete_registration(
        self,
    ) -> Callable[
        [domains.DeleteRegistrationRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete registration method over gRPC.

        Deletes a ``Registration`` resource.

        This method only works on resources in one of the following
        states:

        -  ``state`` is ``EXPORTED`` with ``expire_time`` in the past
        -  ``state`` is ``REGISTRATION_FAILED``

        Returns:
            Callable[[~.DeleteRegistrationRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_registration" not in self._stubs:
            self._stubs["delete_registration"] = self.grpc_channel.unary_unary(
                "/google.cloud.domains.v1beta1.Domains/DeleteRegistration",
                request_serializer=domains.DeleteRegistrationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_registration"]

    @property
    def retrieve_authorization_code(
        self,
    ) -> Callable[
        [domains.RetrieveAuthorizationCodeRequest], Awaitable[domains.AuthorizationCode]
    ]:
        r"""Return a callable for the retrieve authorization code method over gRPC.

        Gets the authorization code of the ``Registration`` for the
        purpose of transferring the domain to another registrar.

        You can call this method only after 60 days have elapsed since
        the initial domain registration.

        Returns:
            Callable[[~.RetrieveAuthorizationCodeRequest],
                    Awaitable[~.AuthorizationCode]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "retrieve_authorization_code" not in self._stubs:
            self._stubs["retrieve_authorization_code"] = self.grpc_channel.unary_unary(
                "/google.cloud.domains.v1beta1.Domains/RetrieveAuthorizationCode",
                request_serializer=domains.RetrieveAuthorizationCodeRequest.serialize,
                response_deserializer=domains.AuthorizationCode.deserialize,
            )
        return self._stubs["retrieve_authorization_code"]

    @property
    def reset_authorization_code(
        self,
    ) -> Callable[
        [domains.ResetAuthorizationCodeRequest], Awaitable[domains.AuthorizationCode]
    ]:
        r"""Return a callable for the reset authorization code method over gRPC.

        Resets the authorization code of the ``Registration`` to a new
        random string.

        You can call this method only after 60 days have elapsed since
        the initial domain registration.

        Returns:
            Callable[[~.ResetAuthorizationCodeRequest],
                    Awaitable[~.AuthorizationCode]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "reset_authorization_code" not in self._stubs:
            self._stubs["reset_authorization_code"] = self.grpc_channel.unary_unary(
                "/google.cloud.domains.v1beta1.Domains/ResetAuthorizationCode",
                request_serializer=domains.ResetAuthorizationCodeRequest.serialize,
                response_deserializer=domains.AuthorizationCode.deserialize,
            )
        return self._stubs["reset_authorization_code"]


__all__ = ("DomainsGrpcAsyncIOTransport",)
