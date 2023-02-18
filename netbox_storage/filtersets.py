from netbox.filtersets import NetBoxModelFilterSet
import django_filters
from virtualization.models import VirtualMachine
from .models import StoragePool, LUN, StorageSession, Datastore, VMDK


class StoragePoolFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = StoragePool
        fields = ('id', 'name', 'device')

    def search(self, queryset, name, value):
        return queryset.filter(name__icontains=value)


class LUNFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = LUN
        fields = ('id', 'storage_pool', 'name', 'wwn',)

    def search(self, queryset, name, value):
        return queryset.filter(name__icontains=value)


class DatastoreFilterSet(NetBoxModelFilterSet):
    reachable_by_vm = django_filters.ModelMultipleChoiceFilter(
        field_name='storage_sessions__cluster__virtual_machines',
        queryset=VirtualMachine.objects.all(),
        label='Reachable by these Virtual Machines'
    )

    class Meta:
        model = Datastore
        fields = ('id', 'lun', 'name', 'reachable_by_vm',)

    def search(self, queryset, name, value):
        return queryset.filter(name__icontains=value)


class StorageSessionFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = StorageSession
        fields = (
            'id', 'name', 'cluster', 'datastores',
        )

    def search(self, queryset, name, value):
        return queryset.filter(name__icontains=value)


class VMDKFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = VMDK
        fields = (
            'id', 'name', 'vm', 'datastore',
        )

    def search(self, queryset, name, value):
        return queryset.filter(name__icontains=value)
