from django.contrib import admin
from django.urls import path
from magazine import views

urlpatterns = [
  path('', views.home, name="home"),
   path('update', views.update, name="update"),
    path('about', views.about, name="about"),
]
#   'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME':'harshaData',
#         'USER':'postgres',
#         'PASSWORD':'harshajr10'
#     }