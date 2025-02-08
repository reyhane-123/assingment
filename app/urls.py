from django.urls import path
from . import views

urlpatterns = [
    path('detail/<id>',views.detail)
]
