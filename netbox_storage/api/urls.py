from netbox.api.routers import NetBoxRouter
from . import views


app_name = 'netbox_storage'

router = NetBoxRouter()
router.register('storagepool', views.StoragePoolViewSet)
router.register('lun', views.LUNViewSet)
router.register('datastore', views.DatastoreViewSet)
router.register('storagesession', views.StorageSessionViewSet)
router.register('vmdk', views.VMDKViewSet)

urlpatterns = router.urls
