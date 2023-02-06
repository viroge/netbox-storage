from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from .serializers import StoragePoolSerializer, StorageLUNSerializer, StorageSessionSerializer, StorageLUNGroupSerializer


class StoragePoolViewSet(NetBoxModelViewSet):
    queryset = models.StoragePool.objects.prefetch_related('device', 'tags')
    serializer_class = StoragePoolSerializer


class StorageLUNViewSet(NetBoxModelViewSet):
    queryset = models.StorageLUN.objects.prefetch_related(
        'storage_pool', 'tags'
    )
    serializer_class = StorageLUNSerializer


class StorageLUNGroupViewSet(NetBoxModelViewSet):
    queryset = models.StorageLUNGroup.objects.prefetch_related(
        'storage_lun', 'tags'
    )
    serializer_class = StorageLUNGroupSerializer


class StorageSessionViewSet(NetBoxModelViewSet):
    queryset = models.StorageSession.objects.prefetch_related(
        'cluster', 'storage_lun_groups', 'tags'
    )
    serializer_class = StorageSessionSerializer
