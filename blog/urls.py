from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [ 
    path('', views.index, name='index' ),
    path('view_firmwares/<str:pk_test>/', views.firmwares, name='view_firmware'),
    path('launch/', views.view_andr, name='launch_android'),
    path('cracked_tools/<str:pk_test>/', views.cracked_tools, name='cracked_tools'),
    path('video_torrent/<str:pk_test>/', views.video_torent, name='video_torrent'),


    path('add_device/', views.add_device, name='add_device'),
    path('edit_device/<str:pk_test>/', views.edit_device, name='edit_device'),
    path('delete_device/<str:pk_test>/', views.remove_device, name='delete_device'),

    path('add_frp/', views.add_frp, name='add_frp'),
    path('edit_frp/<str:pk_test>/', views.edit_frp, name='edit_frp'),
    path('delete_frp/<str:pk_test>/', views.remove_frp, name='delete_frp'),

    path('add_firm/', views.add_firm, name='add_firm'),
    path('edit_firm/<str:pk_test>/', views.edit_firm, name='edit_firm'),
    path('delete_firm/<str:pk_test>/', views.remove_firm, name='delete_firm'),

    path('add_crack/', views.add_crack, name='add_crack'),
    path('edit_crack/<str:pk_test>/', views.edit_crack, name='edit_crack'),
    path('delete_crack/<str:pk_test>/', views.remove_crack, name='delete_crack'),


    path('add_torrent/', views.add_torrent, name='add_torrent'),
    path('edit_torrent/<str:pk_test>/', views.edit_torrent, name='edit_torrent'),
    path('delete_torrent/<str:pk_test>/', views.remove_torrent, name='delete_torrent'),

    path('admin_view/', views.admin_view, name='admin'),
    path('login/', views.log_user, name='login'),
    path('logout/', views.logout_user, name='logout'),


    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='reset_password'),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset1.html'), name='password_reset_confirm'),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )