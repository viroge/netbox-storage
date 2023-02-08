from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

storagepool_buttons = [
    PluginMenuButton(
        link='plugins:netbox_storage:storagepool_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    ),
    # PluginMenuButton(
    #     link='plugins:netbox_storage:storagepool_import',
    #     title='Import',
    #     icon_class='mdi mdi-upload',
    #     color=ButtonColorChoices.CYAN
    # )
]

lun_buttons = [
    PluginMenuButton(
        link='plugins:netbox_storage:lun_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

datastore_buttons = [
    PluginMenuButton(
        link='plugins:netbox_storage:datastore_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

storagesession_buttons = [
    PluginMenuButton(
        link='plugins:netbox_storage:storagesession_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

vmdk_button = [
    PluginMenuButton(
        link='plugins:netbox_storage:vmdk_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_storage:storagepool_list',
        link_text='Storage Pools',
        buttons=storagepool_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_storage:lun_list',
        link_text='LUNs',
        buttons=lun_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_storage:datastore_list',
        link_text='Datastores',
        buttons=datastore_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_storage:storagesession_list',
        link_text='Storage Sessions',
        buttons=storagesession_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_storage:vmdk_list',
        link_text='VMDKs',
        buttons=vmdk_button
    ),
)
