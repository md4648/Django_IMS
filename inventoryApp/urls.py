
from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home,name=''),
    path('add_item',views.addItems,name='add_item'),
    path('update-item/<int:pk>',views.updateItem, name='update-item')
]
