from django.shortcuts import render

def go_index(request):
    return render(request, 'index.html', context={'user':request.user})