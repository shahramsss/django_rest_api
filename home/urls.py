from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    # path("home/", views.home, name="home"),
    path("home/", views.Home.as_view(), name="home"),
    path("persons/", views.PersonView.as_view(), name="persons"),
    path("question/", views.QuestionView.as_view()),
    path("questions/", views.QuestionListView.as_view()),
    path("question/create/", views.QuestionCreateView.as_view()),
    path("question/update/<int:pk>/", views.QuestionUpdateView.as_view()),
    path("question/delete/<int:pk>/", views.QuestionDeleteView.as_view()),
]
