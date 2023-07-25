from django.urls import path
from .apis import ProfileApi, RegisterApi
from .views import RegisterView, ProfileView, UpdatePermissions

app_name = "users"
urlpatterns = [
    path('register/', RegisterApi.as_view(),name="register"),
    path('profile/', ProfileApi.as_view(),name="profile"),
    path("register-user/", RegisterView.as_view(), name="register_user"),
    path("profiles/", ProfileView.as_view(), name="profile"),
    path("update-permission/", UpdatePermissions.as_view(), name="update")

]
