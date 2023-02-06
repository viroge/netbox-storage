from rest_framework import serializers

from ..models import StoragePool, StorageLUN, StorageSession, StorageLUNGroup
from virtualization.api.serializers import NestedClusterSerializer
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer


#
# Nested serializers
#

class NestedStoragePoolSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_storage-api:storagepool-detail'
    )

    class Meta:
        model = StoragePool
        fields = ('id', 'url', 'display', 'name')


class NestedStorageLUNSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_storage-api:storagelun-detail'
    )

    class Meta:
        model = StorageLUN
        fields = ('id', 'url', 'display', 'name')


class NestedStorageSessionSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_storage-api:storagesession-detail'
    )

    class Meta:
        model = StorageSession
        fields = ('id', 'url', 'display', 'name')


class NestedStorageLUNGroupSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_storage-api:storagelungroup-detail'
    )

    class Meta:
        model = StorageLUNGroup
        fields = ('id', 'url', 'display', 'name')


#
# Regular serializers
#

class StoragePoolSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_storage-api:storagepool-detail'
    )

    class Meta:
        model = StoragePool
        fields = (
            'id', 'url', 'display', 'name', 'size', 'device', 'description',
            'tags', 'custom_fields', 'created', 'last_updated',
        )


class StorageLUNSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_storage-api:storagelun-detail'
    )
    storage_pool = NestedStoragePoolSerializer()

    class Meta:
        model = StorageLUN
        fields = (
            'id', 'url', 'display', 'name', 'size', 'storage_pool',
            'description', 'tags', 'custom_fields',
            'created', 'last_updated',
        )


class StorageSessionSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_storage-api:storagesession-detail'
    )
    cluster = NestedClusterSerializer()

    class Meta:
        model = StorageSession
        fields = (
            'id', 'url', 'display', 'name', 'cluster', 'storage_lun_groups',
            'description', 'tags', 'custom_fields', 'created', 'last_updated',
        )


class StorageLUNGroupSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_storage-api:storagelungroup-detail'
    )

    class Meta:
        model = StorageLUNGroup
        fields = (
            'id', 'url', 'display', 'name', 'storage_lun',
            'description', 'tags', 'custom_fields', 'created', 'last_updated',
        )
