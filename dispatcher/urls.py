from django.urls import path

from dispatcher import views

app_name = 'dispatcher'
urlpatterns = [
    path('auth/register/', views.register, name='register'),
    path('auth/obtain-token/', views.obtain_token, name='login'),
    path('auth/verify-token/<str:temp_token>/', views.verify_token, name='verify_token'),
    path('auth/refresh-token/', views.refresh_token, name='refresh_token'),
    path('welcome/', views.welcome_message, name='welcome_message'),
    path('learner/new-booking/', views.new_booking_learner, name='new_booking_learner'),
    path('mentor/new-booking/', views.new_booking_mentor, name='new_booking_mentor'),
]
