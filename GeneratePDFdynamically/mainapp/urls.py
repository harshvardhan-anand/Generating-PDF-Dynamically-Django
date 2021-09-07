from django.urls import path
from . import views

urlpatterns = [
    path('showpdf', views.show_pdf),
    path('downloadpdf', views.download_pdf)
]