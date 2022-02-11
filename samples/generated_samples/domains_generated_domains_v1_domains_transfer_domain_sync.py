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
# Generated code. DO NOT EDIT!
#
# Snippet for TransferDomain
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-domains


# [START domains_generated_domains_v1_Domains_TransferDomain_sync]
from google.cloud import domains_v1


def sample_transfer_domain():
    # Create a client
    client = domains_v1.DomainsClient()

    # Initialize request argument(s)
    registration = domains_v1.Registration()
    registration.domain_name = "domain_name_value"
    registration.contact_settings.privacy = "REDACTED_CONTACT_DATA"
    registration.contact_settings.registrant_contact.email = "email_value"
    registration.contact_settings.registrant_contact.phone_number = "phone_number_value"
    registration.contact_settings.admin_contact.email = "email_value"
    registration.contact_settings.admin_contact.phone_number = "phone_number_value"
    registration.contact_settings.technical_contact.email = "email_value"
    registration.contact_settings.technical_contact.phone_number = "phone_number_value"

    request = domains_v1.TransferDomainRequest(
        parent="parent_value",
        registration=registration,
    )

    # Make the request
    operation = client.transfer_domain(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

# [END domains_generated_domains_v1_Domains_TransferDomain_sync]