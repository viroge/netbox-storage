import django_tables2 as tables

from netbox.tables import NetBoxTable, columns
from .models import StoragePool, StorageSession, StorageLUNGroup, StorageLUN


class StorageUtilizationColumn(columns.UtilizationColumn):
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
    utilization = StorageUtilizationColumn(
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


class StorageLUNTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    storage_pool = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = StorageLUN
        fields = (
            'pk', 'id', 'name', 'storage_pool', 'size', 'description', 'actions',
        )
        default_columns = (
            'name', 'storage_pool', 'size',
        )


class StorageLUNGroupTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    storage_lun = columns.ManyToManyColumn(
        linkify_item=True,
        verbose_name='LUNs'
    )

    class Meta(NetBoxTable.Meta):
        model = StorageLUNGroup
        fields = (
            'pk', 'id', 'name', 'storage_lun', 'description', 'actions',
        )
        default_columns = (
            'name', 'storage_lun',
        )


class StorageSessionTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    cluster = tables.Column(
        linkify=True,
    )
    storage_lun_groups = columns.ManyToManyColumn(
        linkify_item=True,
        verbose_name='LUN Groups'
    )

    class Meta(NetBoxTable.Meta):
        model = StorageSession

        fields = (
            'pk', 'id', 'name', 'cluster', 'storage_lun_groups', 'description',
        )
        default_columns = (
            'name', 'cluster', 'storage_lun_groups',
        )
