from django.urls import path
from . import views 


urlpatterns = [
   path('genres/', views.GenreCreateListView.as_view(), name='genres_create-list'),
   path('genres/<int:pk>', views.GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'), 
]