from django.urls import path

from dispatcher import views

app_name = 'dispatcher'
urlpatterns = [
    path('auth/', views.get_auth_token),
    path('welcome/', views.welcome_message, name='welcome_message'),
    path('learner/new-booking/', views.new_booking_learner, name='new_booking_learner'),
    path('mentor/new-booking/', views.new_booking_mentor, name='new_booking_mentor'),
]
