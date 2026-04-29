from django.urls import path
from .views import home_page_view, about_page_view # << NEU

urlpatterns = [
    path("about/", about_page_view), # << NEU
    path("", home_page_view),
]