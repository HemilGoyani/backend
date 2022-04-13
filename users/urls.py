from django.urls import path
from users.views import SigninView,SignupView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login/', SigninView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', SignupView.as_view(), name='auth_register'),
]