from netbox.api.routers import NetBoxRouter
from . import views


app_name = 'netbox_storage'

router = NetBoxRouter()
router.register('storagepool', views.StoragePoolViewSet)
router.register('storagelun', views.StorageLUNViewSet)
router.register('storagesession', views.StorageSessionViewSet)
router.register('storagelungroup', views.StorageLUNGroupViewSet)

urlpatterns = router.urls
