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

storageluns_buttons = [
    PluginMenuButton(
        link='plugins:netbox_storage:storagelun_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

storagelungroups_buttons = [
    PluginMenuButton(
        link='plugins:netbox_storage:storagelungroup_add',
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

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_storage:storagepool_list',
        link_text='Storage Pools',
        buttons=storagepool_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_storage:storagelun_list',
        link_text='Storage LUNs',
        buttons=storageluns_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_storage:storagelungroup_list',
        link_text='Storage LUN Groups',
        buttons=storagelungroups_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_storage:storagesession_list',
        link_text='Storage Sessions',
        buttons=storagesession_buttons
    ),
)
