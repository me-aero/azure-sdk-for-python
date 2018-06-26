# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class OperationListResult(Model):
    """The operation list response that contains all operations for Azure
    Container Instance service.

    :param value: The list of operations.
    :type value: list[~azure.mgmt.containerinstance.models.Operation]
    :param next_link: The URI to fetch the next page of operations.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, *, value=None, next_link: str=None, **kwargs) -> None:
        super(OperationListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link
