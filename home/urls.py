from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    # path("home/", views.home, name="home"),
    path("home/", views.Home.as_view(), name="home"),
    path("persons/", views.PersonView.as_view(), name="persons"),
    path("questions/", views.QuestionView.as_view()),
    path("questions/<int:pk>/", views.QuestionView.as_view()),
]
