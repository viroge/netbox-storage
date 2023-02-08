from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from .serializers import StoragePoolSerializer, LUNSerializer, StorageSessionSerializer, DatastoreSerializer, VMDKSerializer


class StoragePoolViewSet(NetBoxModelViewSet):
    queryset = models.StoragePool.objects.prefetch_related('device', 'tags')
    serializer_class = StoragePoolSerializer


class LUNViewSet(NetBoxModelViewSet):
    queryset = models.LUN.objects.prefetch_related(
        'storage_pool', 'tags'
    )
    serializer_class = LUNSerializer


class DatastoreViewSet(NetBoxModelViewSet):
    queryset = models.Datastore.objects.prefetch_related(
        'lun', 'tags'
    )
    serializer_class = DatastoreSerializer


class StorageSessionViewSet(NetBoxModelViewSet):
    queryset = models.StorageSession.objects.prefetch_related(
        'cluster', 'datastores', 'tags'
    )
    serializer_class = StorageSessionSerializer


class VMDKViewSet(NetBoxModelViewSet):
    queryset = models.VMDK.objects.prefetch_related(
        'datastore', 'vm', 'tags'
    )
    serializer_class = VMDKSerializer
