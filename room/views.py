from django.shortcuts import render
from room.models import Room, NumBed


def main_page(request):
    query_set = Room.objects.all()
    query_set_bed = NumBed.objects.all()
    context = {'rooms': query_set, 'number_bed': query_set_bed}
    return render(request, 'room/index.html', context=context)


def room(request, room_id):
    room_detail = Room.objects.get(id=room_id)
    context = {'room_detail': room_detail}
    return render(request, 'room/info-room.html', context=context)
