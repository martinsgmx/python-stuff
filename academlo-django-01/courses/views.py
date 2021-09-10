from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from courses.models import Course


class CoursesView(View):
    http_methods_names: list = ['GET']

    @staticmethod
    def get(request) -> render or HttpResponse:
        try:
            return render(request, 'courses/index.html', {'courses': Course.objects.all()})
        except ObjectDoesNotExist:
            return HttpResponse('Something is wrong!')


class CourseView(View):
    http_methods_names: list = ['GET']

    @staticmethod
    def get(request, pk) -> render or HttpResponse:
        try:
            return render(request, 'courses/detailed.html', {'course': Course.objects.get(pk=pk)})
        except ObjectDoesNotExist:
            return HttpResponse('Something is wrong!')
