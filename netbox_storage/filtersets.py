from netbox.filtersets import NetBoxModelFilterSet
from .models import StoragePool, LUN, StorageSession, Datastore, VMDK


class StoragePoolFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = StoragePool
        fields = ('id', 'name', 'device')

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)


class LUNFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = LUN
        fields = ('id', 'storage_pool', 'name',)

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)


class DatastoreFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Datastore
        fields = ('id', 'lun', 'name',)

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)


class StorageSessionFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = StorageSession
        fields = (
            'id', 'name', 'cluster', 'datastores',
        )

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)


class VMDKFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = VMDK
        fields = (
            'id', 'name', 'vm', 'datastore',
        )

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)
