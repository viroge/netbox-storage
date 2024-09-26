import django_tables2 as tables

from django.template.defaultfilters import filesizeformat
from netbox.tables import NetBoxTable, columns
from .models import StoragePool, StorageSession, Datastore, LUN, VMDK


class UtilizationColumn(columns.UtilizationColumn):
    template_code = """
    {% load helpers %}
    {% if record.pk %}
      {% utilization_graph value %}
    {% endif %}
    """


class StoragePoolTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    utilization = UtilizationColumn(
        accessor='get_utilization',
        orderable=False
    )
    device = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = StoragePool
        fields = (
            'pk', 'id', 'name', 'size', 'utilization', 'device', 'description',
            'actions'
        )
        default_columns = ('name', 'device', 'size', 'utilization')

    def render_size(self, value):
        return filesizeformat(value)


class LUNTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    storage_pool = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = LUN
        fields = (
            'pk', 'id', 'name', 'storage_pool', 'size', 'wwn', 'description', 'actions',
        )
        default_columns = (
            'name', 'storage_pool', 'size',
        )

    def render_size(self, value):
        return filesizeformat(value)


class DatastoreTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    lun = columns.ManyToManyColumn(
        linkify_item=True,
        verbose_name='LUNs/Shares',
    )
    utilization = UtilizationColumn(
        accessor='get_utilization',
        orderable=False
    )

    class Meta(NetBoxTable.Meta):
        model = Datastore
        fields = (
            'pk', 'id', 'name', 'lun', 'utilization', 'description', 'actions',
        )
        default_columns = (
            'name', 'lun', 'utilization',
        )


class StorageSessionTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    cluster = tables.Column(
        linkify=True,
    )
    datastores = columns.ManyToManyColumn(
        linkify_item=True,
        verbose_name='Datastores'
    )

    class Meta(NetBoxTable.Meta):
        model = StorageSession

        fields = (
            'pk', 'id', 'name', 'cluster', 'datastores', 'description',
        )
        default_columns = (
            'name', 'cluster', 'datastores',
        )


class VMDKTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    vm = tables.Column(
        linkify=True
    )
    datastore = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = VMDK

        fields = (
            'pk', 'id', 'vmdisk', 'name', 'datastore', 'size',
        )
        default_columns = (
            'vmdisk', 'datastore', 'name', 'size',
        )

    def render_size(self, value):
        return filesizeformat(value)
