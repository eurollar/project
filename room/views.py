from django.shortcuts import render


def room(request):
    arr = ['123', '345', '567']
    context = {'users': arr, 'admin': 'sassr'}
    return render(request, 'room/index.html', context)
# Create your views here.
