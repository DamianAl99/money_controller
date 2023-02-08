from django.shortcuts import render, redirect, get_object_or_404
from payments.models import Add_Text_Admin

def go_index(request):
    return render(request, 'index.html', context={'request':request, 'text':get_object_or_404(Add_Text_Admin).text})