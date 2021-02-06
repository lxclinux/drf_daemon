from django.urls import path, re_path
from . import views

urlpatterns = [
    path("students3/", views.Student3View.as_view()),
    re_path("students2/", views.Student2View.as_view()),
    re_path("students/(?P<pk>\d)/", views.Student1View.as_view()),
]
