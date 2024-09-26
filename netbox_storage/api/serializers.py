from rest_framework import serializers

from virtualization.api.serializers import ClusterSerializer, VirtualMachineSerializer
from dcim.api.serializers import DeviceSerializer
from netbox.api.serializers import NetBoxModelSerializer
from netbox.api.fields import SerializedPKRelatedField
from ..models import StoragePool, LUN, StorageSession, Datastore, VMDK


class StoragePoolSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_storage-api:storagepool-detail'
    )
    device = DeviceSerializer(nested=True)

    class Meta:
        model = StoragePool
        fields = (
            'id', 'url', 'display', 'name', 'size', 'device', 'description',
            'tags', 'custom_fields', 'created', 'last_updated',
        )
        brief_fields = (
            'id', 'url', 'display', 'name', 'size', 'device',
        )


class LUNSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_storage-api:lun-detail'
    )
    storage_pool = StoragePoolSerializer(nested=True)

    class Meta:
        model = LUN
        fields = (
            'id', 'url', 'display', 'name', 'size', 'storage_pool', 'wwn',
            'description', 'tags', 'custom_fields',
            'created', 'last_updated',
        )
        brief_fields = (
            'id', 'url', 'display', 'name', 'size', 'storage_pool', 
        )


class DatastoreSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_storage-api:datastore-detail'
    )
    lun = SerializedPKRelatedField(
        queryset=LUN.objects.all(),
        serializer=LUNSerializer,
        many=True
    )

    class Meta:
        model = Datastore
        fields = (
            'id', 'url', 'display', 'name', 'lun',
            'description', 'tags', 'custom_fields', 'created', 'last_updated',
        )
        brief_fields = (
            'id', 'url', 'display', 'name', 'lun',
        )


class StorageSessionSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_storage-api:storagesession-detail'
    )
    cluster = ClusterSerializer(nested=True)
    datastores = SerializedPKRelatedField(
        queryset=Datastore.objects.all(),
        serializer=DatastoreSerializer,
        many=True
    )

    class Meta:
        model = StorageSession
        fields = (
            'id', 'url', 'display', 'name', 'cluster', 'datastores',
            'description', 'tags', 'custom_fields', 'created', 'last_updated',
        )
        brief_fields = (
            'id', 'url', 'display', 'name', 'cluster', 'datastores',
        )


class VMDKSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_storage-api:vmdk-detail'
    )
    datastore = DatastoreSerializer(nested=True)
    vm = VirtualMachineSerializer(nested=True)

    class Meta:
        model = VMDK
        fields = (
            'id', 'url', 'display', 'vm', 'name', 'datastore',
            'size', 'tags', 'custom_fields', 'created', 'last_updated',
        )
        brief_fields = (
            'id', 'url', 'display', 'vm', 'name', 'datastore', 'size',
        )
