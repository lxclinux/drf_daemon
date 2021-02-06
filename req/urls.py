from django.urls import path
from . import views

urlpatterns = [
    path("students3/", views.Student3Apiview.as_view()),
    path("students1/", views.Student1View.as_view()),
    path("students2/", views.Student2Api.as_view())
]
