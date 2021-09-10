from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from students.models import Student


class StudentsView(View):
    http_methods_names = ['GET']

    @staticmethod
    def get(request) -> render or HttpResponse:
        try:
            return render(request, 'students/index.html', {'students': Student.objects.all()})
        except ObjectDoesNotExist:
            return HttpResponse('Something is wrong!')


class StudentView(View):
    http_methods_names = ['GET']

    @staticmethod
    def get(request, pk) -> render or HttpResponse:
        try:
            return render(request, 'students/detailed.html', {'student': Student.objects.get(pk=pk)})
        except ObjectDoesNotExist:
            return HttpResponse('Something is wrong!')
