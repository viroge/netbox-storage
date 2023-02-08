from netbox.filtersets import NetBoxModelFilterSet
from .models import LUN, StorageSession, Datastore


# class StorageLUNFilterSet(NetBoxModelFilterSet):

#     class Meta:
#         model = StorageLUN
#         fields = ('id', 'storage_pool', 'name',)

#     def search(self, queryset, name, value):
#         return queryset.filter(description__icontains=value)


# class StorageSessionFilterSet(NetBoxModelFilterSet):

#     class Meta:
#         model = StorageSession
#         fields = (
#             'id', 'name', 'cluster', 'storage_lun_groups',
#         )

#     def search(self, queryset, name, value):
#         return queryset.filter(description__icontains=value)


# class StorageLUNGroupFilterSet(NetBoxModelFilterSet):

#     class Meta:
#         model = StorageLUNGroup
#         fields = (
#             'id', 'storage_pool_allocation', 'name', 'vm',
#         )

#     def search(self, queryset, name, value):
#         return queryset.filter(description__icontains=value)
