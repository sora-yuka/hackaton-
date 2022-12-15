from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from applications.account.views import (
    RegisterApiView, 
    Change_passwordApiView, 
    ActivationApiView,
    ForgotPasswordApiView,
    ForgotPasswordCompleteApiview,
)


urlpatterns = [
    path('signup/', RegisterApiView.as_view()),
    path('signin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('activate/<uuid:activation_code>/', ActivationApiView.as_view()),
    # path('')
]
