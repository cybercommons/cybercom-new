from django.shortcuts import render
from .models import catalogModel

from .permission import createCatalogPermission, CatalogPermission

from data_store.views import MongoDataStore, DataStore, DataStoreDetail
from api import config

class Catalog(MongoDataStore):
    permission_classes = (createCatalogPermission,)
    connect_uri = config.CATALOG_URI
    model = catalogModel
    view_reverse='catalog'
    exclude = config.CATALOG_EXCLUDE
    include = config.CATALOG_INCLUDE
    name = "Catalog"

class CatalogData(DataStore): 
    permission_classes = (CatalogPermission,)
    model = catalogModel
    connect_uri = config.CATALOG_URI

class CatalogDataDetail(DataStoreDetail):
    permission_classes = (CatalogPermission,)
    model = catalogModel
    connect_uri = config.CATALOG_URI
