
from django.contrib import admin
from django.urls import path
from .views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworldurl/',helloworldfunc),
    path('hatoya',hatoyafunc),
    path('part',partfunc),
    path('song',songfunc),
    path('show',showfunc),

]