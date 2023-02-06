from netbox.views import generic
from . import filtersets, forms, models, tables


#
# StoragePool views
#

class StoragePoolView(generic.ObjectView):
    queryset = models.StoragePool.objects.all()

    def get_extra_context(self, request, instance):
        table = tables.StorageLUNTable(instance.luns.all())
        table.configure(request)

        return {
            'luns_table': table,
        }


class StoragePoolListView(generic.ObjectListView):
    queryset = models.StoragePool.objects.all()
    table = tables.StoragePoolTable


class StoragePoolEditView(generic.ObjectEditView):
    queryset = models.StoragePool.objects.all()
    form = forms.StoragePoolForm


class StoragePoolDeleteView(generic.ObjectDeleteView):
    queryset = models.StoragePool.objects.all()


# class StoragePoolImportView(generic.BulkImportView):
#     queryset = models.StoragePool.objects.all()
#     model_form = forms.StoragePoolCSVForm
#     table = tables.StoragePoolTable


#
# StorageLUN views
#

class StorageLUNView(generic.ObjectView):
    queryset = models.StorageLUN.objects.all()


class StorageLUNListView(generic.ObjectListView):
    queryset = models.StorageLUN.objects.all()
    table = tables.StorageLUNTable
    # filterset = filtersets.StorageLUNFilterSet
    # filterset_form = forms.StorageLUNFilterForm


class StorageLUNEditView(generic.ObjectEditView):
    queryset = models.StorageLUN.objects.all()
    form = forms.StorageLUNForm


class StorageLUNDeleteView(generic.ObjectDeleteView):
    queryset = models.StorageLUN.objects.all()


#
# StorageLUNGroup views
#

class StorageLUNGroupView(generic.ObjectView):
    queryset = models.StorageLUNGroup.objects.all()

    def get_extra_context(self, request, instance):
        luns_table = tables.StorageLUNTable(instance.storage_lun.all())
        luns_table.configure(request)

        sessions_table = tables.StorageSessionTable(instance.storage_sessions.all())
        sessions_table.configure(request)

        return {
            'luns_table': luns_table,
            'sessions_table': sessions_table,
        }


class StorageLUNGroupListView(generic.ObjectListView):
    queryset = models.StorageLUNGroup.objects.all()
    table = tables.StorageLUNGroupTable
    # filterset = filtersets.StorageLUNGroupFilterSet
    # filterset_form = forms.StorageLUNGroupFilterForm


class StorageLUNGroupEditView(generic.ObjectEditView):
    queryset = models.StorageLUNGroup.objects.all()
    form = forms.StorageLUNGroupForm


class StorageLUNGroupDeleteView(generic.ObjectDeleteView):
    queryset = models.StorageLUNGroup.objects.all()


#
# StorageSession views
#

class StorageSessionView(generic.ObjectView):
    queryset = models.StorageSession.objects.all()


class StorageSessionListView(generic.ObjectListView):
    queryset = models.StorageSession.objects.all()
    table = tables.StorageSessionTable
    # filterset = filtersets.StorageSessionFilterSet
    # filterset_form = forms.StorageSessionFilterForm


class StorageSessionEditView(generic.ObjectEditView):
    queryset = models.StorageSession.objects.all()
    form = forms.StorageSessionForm


class StorageSessionDeleteView(generic.ObjectDeleteView):
    queryset = models.StorageSession.objects.all()
