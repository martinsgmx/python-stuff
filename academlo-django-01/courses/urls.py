from django.urls import path
from courses.views import CoursesView, CourseView

app_name = 'courses'
urlpatterns = [
    path('', CoursesView.as_view(), name='all'),
    path('<pk>/', CourseView.as_view(), name='detailed')
]
