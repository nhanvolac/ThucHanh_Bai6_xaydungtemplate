from django.conf.urls import url
from orders import views

app_name = "orders"

urlpatterns = [
    url(r'^create/', views.order_create, name = 'order_create'),
]