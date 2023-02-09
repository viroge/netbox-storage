from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from .serializers import StoragePoolSerializer, LUNSerializer, StorageSessionSerializer, DatastoreSerializer, VMDKSerializer


class StoragePoolViewSet(NetBoxModelViewSet):
    queryset = models.StoragePool.objects.prefetch_related('device', 'tags')
    serializer_class = StoragePoolSerializer
    filterset_class = filtersets.StoragePoolFilterSet


class LUNViewSet(NetBoxModelViewSet):
    queryset = models.LUN.objects.prefetch_related(
        'storage_pool', 'tags'
    )
    serializer_class = LUNSerializer
    filterset_class = filtersets.LUNFilterSet


class DatastoreViewSet(NetBoxModelViewSet):
    queryset = models.Datastore.objects.prefetch_related(
        'lun', 'tags'
    )
    serializer_class = DatastoreSerializer
    filterset_class = filtersets.DatastoreFilterSet


class StorageSessionViewSet(NetBoxModelViewSet):
    queryset = models.StorageSession.objects.prefetch_related(
        'cluster', 'datastores', 'tags'
    )
    serializer_class = StorageSessionSerializer
    filterset_class = filtersets.StorageSessionFilterSet


class VMDKViewSet(NetBoxModelViewSet):
    queryset = models.VMDK.objects.prefetch_related(
        'datastore', 'vm', 'tags'
    )
    serializer_class = VMDKSerializer
    filterset_class = filtersets.VMDKFilterSet
