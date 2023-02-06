from django.urls import path
from . import models, views
from netbox.views.generic import ObjectChangeLogView


urlpatterns = (

    # Storage pools
    path('storagepool/', views.StoragePoolListView.as_view(), name='storagepool_list'),
    path('storagepool/add/', views.StoragePoolEditView.as_view(), name='storagepool_add'),
    # path('storagepool/import/', views.StoragePoolImportView.as_view(), name='storagepool_import'),
    path('storagepool/<int:pk>/', views.StoragePoolView.as_view(), name='storagepool'),
    path('storagepool/<int:pk>/edit/', views.StoragePoolEditView.as_view(), name='storagepool_edit'),
    path('storagepool/<int:pk>/delete/', views.StoragePoolDeleteView.as_view(), name='storagepool_delete'),
    path('storagepool/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='storagepool_changelog', kwargs={
        'model': models.StoragePool
    }),

    # Storage LUNs
    path('storagelun/', views.StorageLUNListView.as_view(), name='storagelun_list'),
    path('storagelun/add/', views.StorageLUNEditView.as_view(), name='storagelun_add'),
    path('storagelun/<int:pk>/', views.StorageLUNView.as_view(), name='storagelun'),
    path('storagelun/<int:pk>/edit/', views.StorageLUNEditView.as_view(), name='storagelun_edit'),
    path('storagelun/<int:pk>/delete/', views.StorageLUNDeleteView.as_view(), name='storagelun_delete'),
    path('storagelun/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='storagelun_changelog', kwargs={
        'model': models.StorageLUN
    }),

    # Storage LUN groups
    path('storagelungroup/', views.StorageLUNGroupListView.as_view(), name='storagelungroup_list'),
    path('storagelungroup/add/', views.StorageLUNGroupEditView.as_view(), name='storagelungroup_add'),
    path('storagelungroup/<int:pk>/', views.StorageLUNGroupView.as_view(), name='storagelungroup'),
    path('storagelungroup/<int:pk>/edit/', views.StorageLUNGroupEditView.as_view(), name='storagelungroup_edit'),
    path('storagelungroup/<int:pk>/delete/', views.StorageLUNGroupDeleteView.as_view(), name='storagelungroup_delete'),
    path('storagelungroup/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='storagelungroup_changelog', kwargs={
        'model': models.StorageLUNGroup
    }),

    # Storage sessions
    path('storagesession/', views.StorageSessionListView.as_view(), name='storagesession_list'),
    path('storagesession/add/', views.StorageSessionEditView.as_view(), name='storagesession_add'),
    path('storagesession/<int:pk>/', views.StorageSessionView.as_view(), name='storagesession'),
    path('storagesession/<int:pk>/edit/', views.StorageSessionEditView.as_view(), name='storagesession_edit'),
    path('storagesession/<int:pk>/delete/', views.StorageSessionDeleteView.as_view(), name='storagesession_delete'),
    path('storagesession/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='storagesession_changelog', kwargs={
        'model': models.StorageSession
    }),
)
