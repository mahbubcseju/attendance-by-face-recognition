from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='Home'),

    path('login', views.Login.as_view(), name='Login'),
    path('logout', views.LogOut.as_view(), name='LogOut'),
    path('sign_up', views.SignUp.as_view(), name='SignUp'),
    path('sign_up/done', views.SignUpDone.as_view(), name='SignUpDone'),

    path('api/course/create', views.APICourseCreate.as_view(), name='APICourseCreate'),
    path('course/detail/<int:pk>/', views.CourseDetail.as_view(), name='CourseDetail'),
    path('course/student/invite/', views.APIStudentInvite.as_view(), name='APIStudentInvite'),
    path('api/student/invitation/update/', views.APIInvitationUpdate.as_view(), name='APIStudentInvitationUpdate'),
    path('attendance/initialize/<int:course_id>/', views.InitializeAttendance.as_view(), name='InitializeAttendance'),
    path('attendance/<int:period_id>/start/', views.ProcessAttendance.as_view(), name='ProcessAttendance'),
    path('register/image/<username>/', views.RegisterImage.as_view(), name='RegisterFaceImage'),
]
