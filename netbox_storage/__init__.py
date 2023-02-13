from extras.plugins import PluginConfig


class NetBoxStorageConfig(PluginConfig):
    name = 'netbox_storage'
    verbose_name = ' NetBox Storage'
    description = 'Netbox Storage Administration Plugin'
    version = '0.5'
    base_url = 'storage'


config = NetBoxStorageConfig
