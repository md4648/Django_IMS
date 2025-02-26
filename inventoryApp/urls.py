
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.Home,name=''),
    path('add_item',views.addItems,name='add_item'),
    path('update-item/<int:pk>',views.updateItem, name='update-item'),
    path('delete_item/<int:pk> ',views.delete_item, name='delete_item'),
    path('stock_detail/<int:pk> ',views.stock_detail, name='stock_detail'),
    path('receive_item/<int:pk>',views.receive_item,name='receive_item'),
    path('issue_item/<int:pk>',views.issue_item,name='issue_item'),
    path('reorder_item/<int:pk>',views.reorder_item,name='reorder_item'),
    path('accounts/', include('registration.backends.default.urls')),
]
