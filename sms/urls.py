from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from sms import views as sms_views
from sms import test_csv
from django.contrib.auth import views as auth_views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView, send

urlpatterns = [
    path('', views.home, name = 'sms-home'),
    path('about/', views.about, name = 'sms-about'),
    # path('simple/', views.sendsms, name = 'sms-simple'),
    path('blog/', views.blog, name = 'sms-blog'),
    path('profile/', sms_views.profile, name = 'profile'),
    path('login/', auth_views.LoginView.as_view(template_name= 'sms/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name= 'sms/logout.html'), name='logout'),

    path('register/', sms_views.register, name = 'register'),
    path('sen/', sms_views.SendSmsView, name = 'send'),
    path('send/', sms_views.send, name = 'send'),
    path('book/', sms_views.createbook, name = 'book'),
    path('upload/csv/', test_csv.upload_csv, name = 'upload_csv'),
    path('upload/', sms_views.upload, name = 'upload'),


    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),

    path('simple/', sms_views.SendSmsView.as_view(), name='sms-simple'),
    path('smsreport/', sms_views.SmsReportView.as_view(), name='sms-simple'),


    path('password-reset/', auth_views.PasswordResetView.as_view(template_name= 'sms/password_reset.html'), name='password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name= 'sms/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name= 'sms/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name= 'sms/password_reset_complete.html'), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
