from django.urls import path
from apps.web.views import order
urlpatterns = [
    path('home_web/', order.home_web, name='home_web')
]
app_name = "web"
