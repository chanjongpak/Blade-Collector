from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blades/', views.blades_index, name='index'),
    path('blades/<int:blade_id>/', views.blade_detail, name='detail'),
    path('blades/create/', views.BladeCreate.as_view(), name='blades_create'),
    path('blades/<int:pk>/update/', views.BladeUpdate.as_view(), name='blades_update'),
    path('blades/<int:pk>/delete/', views.BladeDelete.as_view(), name='blades_delete'),
    path('blades/<int:blade_id>/add_maintenance/', views.add_maintenance, name='add_maintenance'),
    path('accessories/', views.AccessoryList.as_view(), name='accessories_index'),
    path('accessories/create/', views.AccessoryCreate.as_view(), name='accessories_create'),
    path('accessories/<int:pk>/', views.AccessoryDetail.as_view(), name='accessories_detail'),
    path('accessories/<int:pk>/update', views.AccessoryUpdate.as_view(), name='accessories_update'),
    path('accessories/<int:pk>/delete', views.AccessoryDelete.as_view(), name='accessories_delete'),
    path('blades/<int:blade_id>/assoc_accessory/<int:accessory_id>/', views.assoc_accessory, name='assoc_accessory'),
]