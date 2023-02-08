from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm, NetBoxModelCSVForm
from utilities.forms.fields import DynamicModelChoiceField, CSVModelChoiceField, DynamicModelMultipleChoiceField
from dcim.models import Device
from virtualization.models import Cluster, VirtualMachine
from .models import StoragePool, StorageSession, LUN, Datastore, VMDK


#
# Regular forms
#
class StoragePoolForm(NetBoxModelForm):
    device = DynamicModelChoiceField(
        queryset=Device.objects.all()
    )

    class Meta:
        model = StoragePool
        fields = ('name', 'size', 'device', 'description', 'tags')


class LUNForm(NetBoxModelForm):
    storage_pool = DynamicModelChoiceField(
        queryset=StoragePool.objects.all()
    )

    class Meta:
        model = LUN
        fields = ('storage_pool', 'name', 'size', 'description')


class DatastoreForm(NetBoxModelForm):
    lun = DynamicModelMultipleChoiceField(
        queryset=LUN.objects.all()
    )

    class Meta:
        model = LUN
        fields = ('lun', 'name', 'description')


class StorageSessionForm(NetBoxModelForm):
    cluster = DynamicModelChoiceField(
        queryset=Cluster.objects.all(),
    )
    datastores = DynamicModelMultipleChoiceField(
        queryset=Datastore.objects.all()
    )

    class Meta:
        model = StorageSession
        fields = (
            'name', 'cluster', 'datastores', 'description'
        )


class VMDKForm(NetBoxModelForm):
    datastore = DynamicModelChoiceField(
        queryset=Datastore.objects.all(),
    )
    vm = DynamicModelChoiceField(
        queryset=VirtualMachine.objects.all(),
    )

    class Meta:
        model = VMDK
        fields = (
            'vm', 'datastore', 'name', 'size',
        )


#
# Filter forms
#
# class StoragePoolAllocationFilterForm(NetBoxModelFilterSetForm):
#     model = StoragePoolAllocation
#     storage_pool = forms.ModelMultipleChoiceField(
#         queryset=StoragePool.objects.all(),
#         required=False
#     )
#     name = forms.CharField(
#         required=False
#     )
#     allocation_type = forms.MultipleChoiceField(
#         choices=AllocationTypes,
#         required=False
#     )


# class StorageSessionFilterForm(NetBoxModelFilterSetForm):
#     model = StorageSession
#     storage_pool_allocation = forms.ModelMultipleChoiceField(
#         queryset=StoragePoolAllocation.objects.all(),
#         required=False
#     )
#     name = forms.CharField(
#         required=False
#     )
#     session_type = forms.MultipleChoiceField(
#         choices=SessionTypes,
#         required=False
#     )
#     source = DynamicModelChoiceField(
#         queryset=IPAddress.objects.all(),
#         required=False
#     )
#     destination = DynamicModelChoiceField(
#         queryset=IPAddress.objects.all(),
#         required=False
#     )


# class StorageSpaceAllocationFilterForm(NetBoxModelFilterSetForm):
#     model = StorageSpaceAllocation
#     storage_pool_allocation = forms.ModelMultipleChoiceField(
#         queryset=StoragePoolAllocation.objects.all(),
#         required=False
#     )
#     vm = DynamicModelChoiceField(
#         queryset=VirtualMachine.objects.all(),
#         required=False
#     )
#     name = forms.CharField(
#         required=False
#     )


# #
# # CSV Forms
# #

# class StoragePoolCSVForm(NetBoxModelCSVForm):
#     device = CSVModelChoiceField(
#         queryset=Device.objects.all(),
#         to_field_name='name',
#     )

#     class Meta:
#         model = StoragePool
#         fields = ('name', 'size', 'device', 'description')
