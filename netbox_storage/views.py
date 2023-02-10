from netbox.views import generic
from . import filtersets, forms, models, tables


#
# StoragePool views
#

class StoragePoolView(generic.ObjectView):
    queryset = models.StoragePool.objects.all()

    def get_extra_context(self, request, instance):
        table = tables.LUNTable(instance.luns.all())
        table.configure(request)

        return {
            'luns_table': table,
        }


class StoragePoolListView(generic.ObjectListView):
    queryset = models.StoragePool.objects.all()
    table = tables.StoragePoolTable
    filterset = filtersets.StoragePoolFilterSet
    filterset_form = forms.StoragePoolFilterForm


class StoragePoolEditView(generic.ObjectEditView):
    queryset = models.StoragePool.objects.all()
    form = forms.StoragePoolForm


class StoragePoolDeleteView(generic.ObjectDeleteView):
    queryset = models.StoragePool.objects.all()


class StoragePoolBulkDeleteView(generic.BulkDeleteView):
    queryset = models.StoragePool.objects.all()
    table = tables.StoragePoolTable
    filterset = filtersets.StoragePoolFilterSet


# class StoragePoolImportView(generic.BulkImportView):
#     queryset = models.StoragePool.objects.all()
#     model_form = forms.StoragePoolCSVForm
#     table = tables.StoragePoolTable


#
# LUN views
#

class LUNView(generic.ObjectView):
    queryset = models.LUN.objects.all()


class LUNListView(generic.ObjectListView):
    queryset = models.LUN.objects.all()
    table = tables.LUNTable
    filterset = filtersets.LUNFilterSet
    filterset_form = forms.LUNFilterForm


class LUNEditView(generic.ObjectEditView):
    queryset = models.LUN.objects.all()
    form = forms.LUNForm


class LUNDeleteView(generic.ObjectDeleteView):
    queryset = models.LUN.objects.all()


class LUNBulkDeleteView(generic.BulkDeleteView):
    queryset = models.LUN.objects.all()
    table = tables.LUNTable
    filterset = filtersets.LUNFilterSet


#
# StorageLUNGroup views
#

class DatastoreView(generic.ObjectView):
    queryset = models.Datastore.objects.all()

    def get_extra_context(self, request, instance):
        luns_table = tables.LUNTable(instance.lun.all())
        luns_table.configure(request)

        sessions_table = tables.StorageSessionTable(instance.storage_sessions.all())
        sessions_table.configure(request)

        return {
            'luns_table': luns_table,
            'sessions_table': sessions_table,
        }


class DatastoreListView(generic.ObjectListView):
    queryset = models.Datastore.objects.all()
    table = tables.DatastoreTable
    filterset = filtersets.DatastoreFilterSet
    filterset_form = forms.DatastoreFilterForm


class DatastoreEditView(generic.ObjectEditView):
    queryset = models.Datastore.objects.all()
    form = forms.DatastoreForm


class DatastoreDeleteView(generic.ObjectDeleteView):
    queryset = models.Datastore.objects.all()


class DatastoreBulkDeleteView(generic.BulkDeleteView):
    queryset = models.Datastore.objects.all()
    table = tables.DatastoreTable
    filterset = filtersets.DatastoreFilterSet


#
# StorageSession views
#

class StorageSessionView(generic.ObjectView):
    queryset = models.StorageSession.objects.all()


class StorageSessionListView(generic.ObjectListView):
    queryset = models.StorageSession.objects.all()
    table = tables.StorageSessionTable
    filterset = filtersets.StorageSessionFilterSet
    filterset_form = forms.StorageSessionFilterForm


class StorageSessionEditView(generic.ObjectEditView):
    queryset = models.StorageSession.objects.all()
    form = forms.StorageSessionForm


class StorageSessionDeleteView(generic.ObjectDeleteView):
    queryset = models.StorageSession.objects.all()


class StorageSessionBulkDeleteView(generic.BulkDeleteView):
    queryset = models.StorageSession.objects.all()
    table = tables.StorageSessionTable
    filterset = filtersets.StorageSessionFilterSet


#
# VMDK views
#

class VMDKView(generic.ObjectView):
    queryset = models.VMDK.objects.all()


class VMDKListView(generic.ObjectListView):
    queryset = models.VMDK.objects.all()
    table = tables.VMDKTable
    filterset = filtersets.VMDKFilterSet
    filterset_form = forms.VMDKFilterForm


class VMDKEditView(generic.ObjectEditView):
    queryset = models.VMDK.objects.all()
    form = forms.VMDKForm


class VMDKDeleteView(generic.ObjectDeleteView):
    queryset = models.VMDK.objects.all()


class VMDKBulkDeleteView(generic.BulkDeleteView):
    queryset = models.VMDK.objects.all()
    filterset = filtersets.VMDKFilterSet
    table = tables.VMDKTable
