from django.urls import path

from dispatcher import views


urlpatterns = [
    path('auth/', views.get_auth_token),
    path('welcome/', views.welcome_message),
    path('learner/new-booking/', views.new_booking_learner),
    path('mentor/new-booking/', views.new_booking_mentor),
]
