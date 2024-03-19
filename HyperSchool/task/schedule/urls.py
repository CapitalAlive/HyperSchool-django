from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect

urlpatterns = [
    path("", lambda request: redirect("main"), name="index"),
    path("schedule/main/", views.main, name="main"),
    path("schedule/course_details/<pk>", views.course_details, name="courses_url"),
    path("schedule/teacher_details/<pk>", views.teacher_details, name="teacher_url"),
    path("schedule/add_course/", views.add_course, name="add_course_url"),
    path("signup/", views.sign_up, name="signup_url"),
    path("login/", LoginView.as_view(template_name="schedule/login.html",
                                     redirect_authenticated_user=True,
                                     next_page="main"),
         name="login_url"),
    path("logout/", LogoutView.as_view(next_page="login_url"), name="logout_url")

]