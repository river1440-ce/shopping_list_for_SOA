from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('items/', views.ItemListView.as_view(), name='items'),
    path('item/<int:pk>', views.ItemDetailView.as_view(), name='item-detail'),
    path('myitems/', views.ItemByUserListView.as_view(), name='my-shopping-list'),   
]

#for the function of CRUD items
urlpatterns += [
    path('item/create/', views.ItemCreateDIY, name='item-create'),
    path('item/<int:pk>/update/', views.ItemUpdate.as_view(), name='item-update'),
    path('item/<int:pk>/delete/', views.ItemDelete.as_view(), name='item-delete'),
]

#for user register
urlpatterns += [
    path("register/", views.register_request, name="register"),
]
