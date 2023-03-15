from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('contact/',views.contact,name="contact"),
    path('',views.index,name="home"),
    path('',views.index,name="checkout" ),
]
