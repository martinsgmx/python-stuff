from django.urls import path
from students.views import StudentsView, StudentView


app_name = 'students'
urlpatterns = [
    path('', StudentsView.as_view(), name='all'),
    path('<pk>/', StudentView.as_view(), name='detailed')
]
