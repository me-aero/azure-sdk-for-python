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

from .tracked_resource import TrackedResource


class StorageAccount(TrackedResource):
    """The storage account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives
    :type location: str
    :ivar sku: Gets the SKU.
    :vartype sku: ~azure.mgmt.storage.v2018_03_01_preview.models.Sku
    :ivar kind: Gets the Kind. Possible values include: 'Storage',
     'StorageV2', 'BlobStorage'
    :vartype kind: str or ~azure.mgmt.storage.v2018_03_01_preview.models.Kind
    :param identity: The identity of the resource.
    :type identity: ~azure.mgmt.storage.v2018_03_01_preview.models.Identity
    :ivar provisioning_state: Gets the status of the storage account at the
     time the operation was called. Possible values include: 'Creating',
     'ResolvingDNS', 'Succeeded'
    :vartype provisioning_state: str or
     ~azure.mgmt.storage.v2018_03_01_preview.models.ProvisioningState
    :ivar primary_endpoints: Gets the URLs that are used to perform a
     retrieval of a public blob, queue, or table object. Note that Standard_ZRS
     and Premium_LRS accounts only return the blob endpoint.
    :vartype primary_endpoints:
     ~azure.mgmt.storage.v2018_03_01_preview.models.Endpoints
    :ivar primary_location: Gets the location of the primary data center for
     the storage account.
    :vartype primary_location: str
    :ivar status_of_primary: Gets the status indicating whether the primary
     location of the storage account is available or unavailable. Possible
     values include: 'available', 'unavailable'
    :vartype status_of_primary: str or
     ~azure.mgmt.storage.v2018_03_01_preview.models.AccountStatus
    :ivar last_geo_failover_time: Gets the timestamp of the most recent
     instance of a failover to the secondary location. Only the most recent
     timestamp is retained. This element is not returned if there has never
     been a failover instance. Only available if the accountType is
     Standard_GRS or Standard_RAGRS.
    :vartype last_geo_failover_time: datetime
    :ivar secondary_location: Gets the location of the geo-replicated
     secondary for the storage account. Only available if the accountType is
     Standard_GRS or Standard_RAGRS.
    :vartype secondary_location: str
    :ivar status_of_secondary: Gets the status indicating whether the
     secondary location of the storage account is available or unavailable.
     Only available if the SKU name is Standard_GRS or Standard_RAGRS. Possible
     values include: 'available', 'unavailable'
    :vartype status_of_secondary: str or
     ~azure.mgmt.storage.v2018_03_01_preview.models.AccountStatus
    :ivar creation_time: Gets the creation date and time of the storage
     account in UTC.
    :vartype creation_time: datetime
    :ivar custom_domain: Gets the custom domain the user assigned to this
     storage account.
    :vartype custom_domain:
     ~azure.mgmt.storage.v2018_03_01_preview.models.CustomDomain
    :ivar secondary_endpoints: Gets the URLs that are used to perform a
     retrieval of a public blob, queue, or table object from the secondary
     location of the storage account. Only available if the SKU name is
     Standard_RAGRS.
    :vartype secondary_endpoints:
     ~azure.mgmt.storage.v2018_03_01_preview.models.Endpoints
    :ivar encryption: Gets the encryption settings on the account. If
     unspecified, the account is unencrypted.
    :vartype encryption:
     ~azure.mgmt.storage.v2018_03_01_preview.models.Encryption
    :ivar access_tier: Required for storage accounts where kind = BlobStorage.
     The access tier used for billing. Possible values include: 'Hot', 'Cool'
    :vartype access_tier: str or
     ~azure.mgmt.storage.v2018_03_01_preview.models.AccessTier
    :param enable_https_traffic_only: Allows https traffic only to storage
     service if sets to true. Default value: False .
    :type enable_https_traffic_only: bool
    :ivar network_rule_set: Network rule set
    :vartype network_rule_set:
     ~azure.mgmt.storage.v2018_03_01_preview.models.NetworkRuleSet
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'sku': {'readonly': True},
        'kind': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'primary_endpoints': {'readonly': True},
        'primary_location': {'readonly': True},
        'status_of_primary': {'readonly': True},
        'last_geo_failover_time': {'readonly': True},
        'secondary_location': {'readonly': True},
        'status_of_secondary': {'readonly': True},
        'creation_time': {'readonly': True},
        'custom_domain': {'readonly': True},
        'secondary_endpoints': {'readonly': True},
        'encryption': {'readonly': True},
        'access_tier': {'readonly': True},
        'network_rule_set': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'kind': {'key': 'kind', 'type': 'Kind'},
        'identity': {'key': 'identity', 'type': 'Identity'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'ProvisioningState'},
        'primary_endpoints': {'key': 'properties.primaryEndpoints', 'type': 'Endpoints'},
        'primary_location': {'key': 'properties.primaryLocation', 'type': 'str'},
        'status_of_primary': {'key': 'properties.statusOfPrimary', 'type': 'AccountStatus'},
        'last_geo_failover_time': {'key': 'properties.lastGeoFailoverTime', 'type': 'iso-8601'},
        'secondary_location': {'key': 'properties.secondaryLocation', 'type': 'str'},
        'status_of_secondary': {'key': 'properties.statusOfSecondary', 'type': 'AccountStatus'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'custom_domain': {'key': 'properties.customDomain', 'type': 'CustomDomain'},
        'secondary_endpoints': {'key': 'properties.secondaryEndpoints', 'type': 'Endpoints'},
        'encryption': {'key': 'properties.encryption', 'type': 'Encryption'},
        'access_tier': {'key': 'properties.accessTier', 'type': 'AccessTier'},
        'enable_https_traffic_only': {'key': 'properties.supportsHttpsTrafficOnly', 'type': 'bool'},
        'network_rule_set': {'key': 'properties.networkAcls', 'type': 'NetworkRuleSet'},
    }

    def __init__(self, **kwargs):
        super(StorageAccount, self).__init__(**kwargs)
        self.sku = None
        self.kind = None
        self.identity = kwargs.get('identity', None)
        self.provisioning_state = None
        self.primary_endpoints = None
        self.primary_location = None
        self.status_of_primary = None
        self.last_geo_failover_time = None
        self.secondary_location = None
        self.status_of_secondary = None
        self.creation_time = None
        self.custom_domain = None
        self.secondary_endpoints = None
        self.encryption = None
        self.access_tier = None
        self.enable_https_traffic_only = kwargs.get('enable_https_traffic_only', False)
        self.network_rule_set = None
