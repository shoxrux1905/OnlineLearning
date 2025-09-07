from django.shortcuts import render

def specialization_list_view(request):
    return render(request, 'beforeReg/course.html')