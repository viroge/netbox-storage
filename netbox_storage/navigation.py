from extras.plugins import PluginMenuButton, PluginMenuItem, PluginMenu
from utilities.choices import ButtonColorChoices

storagepool_buttons = [
    PluginMenuButton(
        link='plugins:netbox_storage:storagepool_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    ),
    PluginMenuButton(
        link='plugins:netbox_storage:storagepool_import',
        title='Import',
        icon_class='mdi mdi-upload',
        color=ButtonColorChoices.CYAN
    )
]

lun_buttons = [
    PluginMenuButton(
        link='plugins:netbox_storage:lun_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    ),
    PluginMenuButton(
        link='plugins:netbox_storage:lun_import',
        title='Import',
        icon_class='mdi mdi-upload',
        color=ButtonColorChoices.CYAN
    )
]

datastore_buttons = [
    PluginMenuButton(
        link='plugins:netbox_storage:datastore_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    ),
    PluginMenuButton(
        link='plugins:netbox_storage:datastore_import',
        title='Import',
        icon_class='mdi mdi-upload',
        color=ButtonColorChoices.CYAN
    )
]

storagesession_buttons = [
    PluginMenuButton(
        link='plugins:netbox_storage:storagesession_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    ),
    PluginMenuButton(
        link='plugins:netbox_storage:storagesession_import',
        title='Import',
        icon_class='mdi mdi-upload',
        color=ButtonColorChoices.CYAN
    )
]

vmdk_button = [
    PluginMenuButton(
        link='plugins:netbox_storage:vmdk_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    ),
    PluginMenuButton(
        link='plugins:netbox_storage:vmdk_import',
        title='Import',
        icon_class='mdi mdi-upload',
        color=ButtonColorChoices.CYAN
    )
]

storagepool_item = (
    PluginMenuItem(
        link='plugins:netbox_storage:storagepool_list',
        link_text='Storage Pools',
        buttons=storagepool_buttons
    )
)

lun_item = (
    PluginMenuItem(
        link='plugins:netbox_storage:lun_list',
        link_text='LUNs',
        buttons=lun_buttons
    )
)

datastore_item = (
    PluginMenuItem(
        link='plugins:netbox_storage:datastore_list',
        link_text='Datastores',
        buttons=datastore_buttons
    )
)

storagesession_item = (
    PluginMenuItem(
        link='plugins:netbox_storage:storagesession_list',
        link_text='Storage Sessions',
        buttons=storagesession_buttons
    )
)

vmdk_item = (
    PluginMenuItem(
        link='plugins:netbox_storage:vmdk_list',
        link_text='VMDKs',
        buttons=vmdk_button
    )
)

menu = PluginMenu(
    label='Storage',
    groups=(
        ('Storage', (storagepool_item, lun_item)),
        ('Virtualization', (datastore_item, storagesession_item, vmdk_item))
    ),
    icon_class='mdi mdi-nas'
)
