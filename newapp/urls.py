from django.urls import path
from newapp.views import *

urlpatterns = [
    path('', student_list, name='student_list'),
    path('add-student/', add_student, name='add_student'),
    path('update-student/<str:s_id>/', update_student, name='update_student'),
    path('delete-student/<str:s_id>/', delete_student, name='delete_student')
]
