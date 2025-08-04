from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

app_name = "accounts"
urlpatterns = [
    path("register/", views.UserRegister.as_view(), name="register"),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
]

router = routers.SimpleRouter()
router.register("user", views.UserViewset)
urlpatterns += router.urls
