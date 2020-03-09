from django.contrib import admin
from django.urls import path
from main.views import index, first, second_task
from main.web_requests import get_areas_list, get_houses_list, get_apartment_list
urlpatterns = [
    path('admin/', admin.site.urls),
    #tasks
    path('', index),
    path('first-task/', first),
    path('graphics/', second_task),
    #web requests
    path('get_areas_list/', get_areas_list),
    path('get_houses_list/', get_houses_list),
    path('get_apartment_list/', get_apartment_list),

]
