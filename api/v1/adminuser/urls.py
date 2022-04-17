from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='refresh_token'),
    path('token-verify/', TokenVerifyView.as_view(), name='verify_token'),
    #    path('signup_user/', views.UserPanelAPI.as_view()),
    #    path('user_signup/', views.UserSignUpPage),
    #    path('user_login/', views.UserLoginPage),
    path('signup_admin/', views.AdminPanelAPI.as_view()),
    path('admin_signup/', views.AdminSignUpPage),
    path('admin_login/', views.AdminLoginPage),
    path('user_check/', views.UserCheckAPI.as_view()),
    path('<int:pk>', views.AdminPanelRetrieveUpdateDestroyAPI.as_view()),
    # path('user/<int:pk>', views.UserPanelRetrieveUpdateDestroyAPI.as_view()),
]
