from django.urls import path
from . import views
app_name="myapp"

urlpatterns = [
    path('index/',views.index,name="Index"),
    path('',views.home,name="Home"),
    path('child/',views.child,name="Child"),
]
