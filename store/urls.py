from django.urls import path

from .views import (
    create_report,
    create_outservice,
    create_room,
    create_asset,
    create_workflow,
    create_visitor,
    create_driver,
    create_supplier,
    create_buyer,
    create_season,
    create_drop,
    create_product,
    create_order,
    create_delivery,
    ReportListView,
    AssetListView,
    ServiceListView,
    DriverListView,
    WorkFlowListView,
    VisitorListView,
    SupplierListView,
    BuyerListView,
    SeasonListView,
    DropListView,
    ProductListView,
    OrderListView,
    RoomListView,
    DeliveryListView,
)

urlpatterns = [
    path( 'create-report/', create_report, name='create-report' ),
    path('create-driver/', create_driver, name='create-driver'),
    path('create-outservice/', create_outservice, name='create-outservice'),
    path('create-room/', create_room, name='create-room'),
    path('create-workflow/', create_workflow, name='create-workflow'),
    path('create-visitor/', create_visitor, name='create-visitor'),
    path('create-asset/', create_asset, name='create-asset'),
    path('create-supplier/', create_supplier, name='create-supplier'),
    path('create-buyer/', create_buyer, name='create-buyer'),
    path('create-season/', create_season, name='create-season'),
    path('create-drop/', create_drop, name='create-drop'),
    path('create-product/', create_product, name='create-product'),
    path('create-order/', create_order, name='create-order'),
    path('create-delivery/', create_delivery, name='create-delivery'),

    path('supplier-list/', SupplierListView.as_view(), name='supplier-list'),
    path( 'report-list/', ReportListView.as_view(), name='report-list' ),
    path('outservice-list/', ServiceListView.as_view(), name='outservice-list'),
    path('asset-list/', AssetListView.as_view(), name='asset-list'),
    path('workflow-list/', WorkFlowListView.as_view(), name='workflow-list'),
    path('driver-list/', DriverListView.as_view(), name='driver-list'),
    path('visitor-list/', VisitorListView.as_view(), name='visitor-list'),
    path('buyer-list/', BuyerListView.as_view(), name='buyer-list'),
    path('season-list/', SeasonListView.as_view(), name='season-list'),
    path('drop-list/', DropListView.as_view(), name='drop-list'),
    path('product-list/', ProductListView.as_view(), name='product-list'),
    path('order-list/', OrderListView.as_view(), name='order-list'),
    path('room-list/', RoomListView.as_view(), name='room-list'),
    path('delivery-list/', DeliveryListView.as_view(), name='delivery-list'),
]