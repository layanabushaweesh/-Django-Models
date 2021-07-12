from django.urls import path
from django.urls import include
from .views import SnackListView
from .views import DetalisView
urlpatterns = [
   path('',SnackListView.as_view() , name='snack_list'),
   path ('<int:pk>/', DetalisView.as_view(), name='snack_detalis')
]

