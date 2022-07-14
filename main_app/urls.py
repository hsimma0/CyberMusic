
from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('accounts/', include('django.contrib.auth.urls')),
  
  # ROUTES FOR MUSIC INDEX
  path('music/', views.music_index, name='index'),
  path('music/index.html', views.music_index, name='index'),
  path('music/<int:music_id>/', views.music_details, name='details'),

  #NEW ROUTE TO CREATE MUSIC
  path('music/create/', views.MusicCreate.as_view(), name='music_create'),

  #NEW ROUTE TO UPDATE AND DELETE MUSIC
  path('music/<int:pk>/update/', views.MusicUpdate.as_view(), name='music_update'),
  path('music/<int:pk>/delete/', views.MusicDelete.as_view(), name='music_delete'),

  #NEW USER ROUTE
  path('accounts/signup/', views.signup, name='signup'), 
]


