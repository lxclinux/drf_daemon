from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path("students/", views.Student2View.as_view()),
    re_path("students/(?P<pk>\d)/", views.Student1View.as_view()),
]
