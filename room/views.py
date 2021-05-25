from django.shortcuts import render


def main_page(request):
    return render(request, 'room/index.html')


def room(request):
    return render(request, 'room/info-room.html')
