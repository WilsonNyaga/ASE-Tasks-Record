from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Profile related URLs
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),

    # View tasks and task-related URLs
    path('view-tasks/', views.view_tasks, name='view_tasks'),
    path('view-tasks/search/', views.search_tasks, name='search_tasks'),
    path('add-task/', views.add_task_view, name='add_task'),
    path('edit-task/<int:task_id>/', views.edit_task_view, name='edit_task'),
    path('delete-task/<int:task_id>/',
         views.delete_task_view, name='delete_task'),

    # Blog related URLs
    path('blog/', views.blog_view, name='blog'),
    path('blog/post/<int:post_id>/', views.view_post, name='view_post'),
    path('blog/post/<int:post_id>/comment/',
         views.add_comment, name='add_comment'),
    path('blog/post/<int:post_id>/edit/', views.edit_post, name='edit_post'),

    # User authentication URLs
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),

    # Password reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='tasks/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='tasks/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='tasks/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='tasks/password_reset_complete.html'), name='password_reset_complete'),
    # Add more URLs for other views as needed

    # Add a root URL pattern
    # Define a home_view function in your views.py
    path('', views.home_view, name='home'),
]
# Include static files for development only
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
