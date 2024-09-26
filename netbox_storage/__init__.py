from netbox.plugins import PluginConfig

class NetBoxStorageConfig(PluginConfig):
    name = 'netbox_storage'
    verbose_name = ' NetBox Storage'
    description = 'Netbox Storage Administration Plugin'
    version = '0.7.0'
    base_url = 'storage'
    min_version = "4.0.0"
    author = 'Gabor Somogyvari'


config = NetBoxStorageConfig
