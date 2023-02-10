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
    path('storagepool/delete/', views.StoragePoolBulkDeleteView.as_view(), name='storagepool_bulk_delete'),
    path('storagepool/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='storagepool_changelog', kwargs={
        'model': models.StoragePool
    }),

    # LUNs
    path('lun/', views.LUNListView.as_view(), name='lun_list'),
    path('lun/add/', views.LUNEditView.as_view(), name='lun_add'),
    path('lun/<int:pk>/', views.LUNView.as_view(), name='lun'),
    path('lun/<int:pk>/edit/', views.LUNEditView.as_view(), name='lun_edit'),
    path('lun/<int:pk>/delete/', views.LUNDeleteView.as_view(), name='lun_delete'),
    path('lun/delete/', views.LUNBulkDeleteView.as_view(), name='lun_bulk_delete'),
    path('lun/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='lun_changelog', kwargs={
        'model': models.LUN
    }),

    # Datastores
    path('datastore/', views.DatastoreListView.as_view(), name='datastore_list'),
    path('datastore/add/', views.DatastoreEditView.as_view(), name='datastore_add'),
    path('datastore/<int:pk>/', views.DatastoreView.as_view(), name='datastore'),
    path('datastore/<int:pk>/edit/', views.DatastoreEditView.as_view(), name='datastore_edit'),
    path('datastore/<int:pk>/delete/', views.DatastoreDeleteView.as_view(), name='datastore_delete'),
    path('datastore/delete/', views.DatastoreBulkDeleteView.as_view(), name='datastore_bulk_delete'),
    path('datastore/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='datastore_changelog', kwargs={
        'model': models.Datastore
    }),

    # Storage sessions
    path('storagesession/', views.StorageSessionListView.as_view(), name='storagesession_list'),
    path('storagesession/add/', views.StorageSessionEditView.as_view(), name='storagesession_add'),
    path('storagesession/<int:pk>/', views.StorageSessionView.as_view(), name='storagesession'),
    path('storagesession/<int:pk>/edit/', views.StorageSessionEditView.as_view(), name='storagesession_edit'),
    path('storagesession/<int:pk>/delete/', views.StorageSessionDeleteView.as_view(), name='storagesession_delete'),
    path('storagesession/delete/', views.StorageSessionBulkDeleteView.as_view(), name='storagesession_bulk_delete'),
    path('storagesession/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='storagesession_changelog', kwargs={
        'model': models.StorageSession
    }),

    # VMDK
    path('vmdk/', views.VMDKListView.as_view(), name='vmdk_list'),
    path('vmdk/add/', views.VMDKEditView.as_view(), name='vmdk_add'),
    path('vmdk/<int:pk>/', views.VMDKView.as_view(), name='vmdk'),
    path('vmdk/<int:pk>/edit/', views.VMDKEditView.as_view(), name='vmdk_edit'),
    path('vmdk/<int:pk>/delete/', views.VMDKDeleteView.as_view(), name='vmdk_delete'),
    path('vmdk/delete/', views.VMDKBulkDeleteView.as_view(), name='vmdk_bulk_delete'),
    path('vmdk/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='vmdk_changelog', kwargs={
        'model': models.VMDK
    }),
)
