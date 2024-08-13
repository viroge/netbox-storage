#from extras.plugins import PluginMenuButton, PluginMenuItem, PluginMenu
#from utilities.choices import ButtonColorChoices
from netbox.plugins import PluginMenuItem, PluginMenu, PluginMenuButton
from netbox.choices import ButtonColorChoices

storagepool_item = PluginMenuItem(
    link='plugins:netbox_storage:storagepool_list',
    link_text='Storage Pools',
    permissions=['netbox_storage.view_storagepool'],
    buttons=[
        PluginMenuButton(
            link='plugins:netbox_storage:storagepool_add',
            title='Add',
            icon_class='mdi mdi-plus-thick',
            color=ButtonColorChoices.GREEN,
            permissions=['netbox_storage.add_storagepool'],
        ),
        PluginMenuButton(
            link='plugins:netbox_storage:storagepool_import',
            title='Import',
            icon_class='mdi mdi-upload',
            color=ButtonColorChoices.CYAN,
            permissions=['netbox_storage.add_storagepool'],
        )
    ]
)

lun_item = PluginMenuItem(
    link='plugins:netbox_storage:lun_list',
    link_text='LUNs',
    permissions=['netbox_storage.view_lun'],
    buttons=[
        PluginMenuButton(
            link='plugins:netbox_storage:lun_add',
            title='Add',
            icon_class='mdi mdi-plus-thick',
            color=ButtonColorChoices.GREEN,
            permissions=['netbox_storage.add_lun'],
        ),
        PluginMenuButton(
            link='plugins:netbox_storage:lun_import',
            title='Import',
            icon_class='mdi mdi-upload',
            color=ButtonColorChoices.CYAN,
            permissions=['netbox_storage.add_lun'],
        )
    ]
)

datastore_item = PluginMenuItem(
    link='plugins:netbox_storage:datastore_list',
    link_text='Datastores',
    permissions=['netbox_storage.view_datastore'],
    buttons=[
        PluginMenuButton(
            link='plugins:netbox_storage:datastore_add',
            title='Add',
            icon_class='mdi mdi-plus-thick',
            color=ButtonColorChoices.GREEN,
            permissions=['netbox_storage.add_datastore'],
        ),
        PluginMenuButton(
            link='plugins:netbox_storage:datastore_import',
            title='Import',
            icon_class='mdi mdi-upload',
            color=ButtonColorChoices.CYAN,
            permissions=['netbox_storage.add_datastore'],
        )
    ]
)

storagesession_item = PluginMenuItem(
    link='plugins:netbox_storage:storagesession_list',
    link_text='Storage Sessions',
    permissions=['netbox_storage.view_storagesession'],
    buttons=[
        PluginMenuButton(
            link='plugins:netbox_storage:storagesession_add',
            title='Add',
            icon_class='mdi mdi-plus-thick',
            color=ButtonColorChoices.GREEN,
            permissions=['netbox_storage.add_storagesession'],
        ),
        PluginMenuButton(
            link='plugins:netbox_storage:storagesession_import',
            title='Import',
            icon_class='mdi mdi-upload',
            color=ButtonColorChoices.CYAN,
            permissions=['netbox_storage.add_storagesession'],
        )
    ]
)

vmdk_item = PluginMenuItem(
    link='plugins:netbox_storage:vmdk_list',
    link_text='VMDKs',
    permissions=['netbox_storage.view_vmdk'],
    buttons=[
        PluginMenuButton(
            link='plugins:netbox_storage:vmdk_add',
            title='Add',
            icon_class='mdi mdi-plus-thick',
            color=ButtonColorChoices.GREEN,
            permissions=['netbox_storage.add_vmdk'],
        ),
        PluginMenuButton(
            link='plugins:netbox_storage:vmdk_import',
            title='Import',
            icon_class='mdi mdi-upload',
            color=ButtonColorChoices.CYAN,
            permissions=['netbox_storage.add_vmdk'],
        )
    ]
)

menu = PluginMenu(
    label='Storage',
    groups=(
        ('Storage', (storagepool_item, lun_item)),
        ('Virtualization', (datastore_item, storagesession_item, vmdk_item))
    ),
    icon_class='mdi mdi-nas'
)
