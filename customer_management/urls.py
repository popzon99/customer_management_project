from django.urls import path
from .views import UserRegisterView, UserLoginView, UserLogoutView, MakerDashboardView, CheckerDashboardView, UploadCustomerView, EditCustomerView, UpdateStatusView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('maker_dashboard/', MakerDashboardView.as_view(), name='maker_dashboard'),
    path('checker_dashboard/', CheckerDashboardView.as_view(), name='checker_dashboard'),
    path('upload/', UploadCustomerView.as_view(), name='upload_customer'),
    path('edit/<str:pk>/', EditCustomerView.as_view(), name='edit_customer'),
    path('update_status/<str:customer_id>/', UpdateStatusView.as_view(), name='update_status'),
]
