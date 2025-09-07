from django.shortcuts import render

def course_list_view(request):
    return render(request, 'beforeReg/course.html')