from django.urls import path, include
from account.views import LoginView, UserListView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('', include('account.urls')),
    path('refresh/', TokenRefreshView.as_view()),
    path('', UserListView.as_view()),
    path('register_phone/', RegisterPhoneView.as_view())
]