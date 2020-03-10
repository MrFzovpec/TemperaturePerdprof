from django.contrib import admin
from django.urls import path
from main.views import index, first, second_task, third_task, forth_task, avarage
from main.web_requests import get_areas_list, get_houses_list, get_apartment_list
urlpatterns = [
    path('admin/', admin.site.urls),
    #tasks
    path('', index),
    path('first-task/', first),
    path('first-graphics/', second_task),
    path('second-graphics/', third_task),
    path('third-graphics/', forth_task),
    path('avarage-graphics/', avarage),
    #web requests
    path('get_areas_list/', get_areas_list),
    path('get_houses_list/', get_houses_list),
    path('get_apartment_list/', get_apartment_list),

]
