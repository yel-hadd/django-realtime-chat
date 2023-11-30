from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Room, Message


@login_required
def rooms(request):
    rooms = Room.objects.all()
    if rooms.count() == 0:
        Room.objects.create(name="General", slug="general")
        Room.objects.create(name="Random", slug="random")
        Room.objects.create(name="Games", slug="games")
        Room.objects.create(name="Movies", slug="movies")
        Room.objects.create(name="Music", slug="music")
        Room.objects.create(name="Sports", slug="sports")
        Room.objects.create(name="TV Shows", slug="tv-shows")
        Room.objects.create(name="Books", slug="books")
        Room.objects.create(name="News", slug="news")
        Room.objects.create(name="Politics", slug="politics")
        Room.objects.create(name="Science", slug="science")
        Room.objects.create(name="Technology", slug="technology")
        Room.objects.create(name="Programming", slug="programming")
        Room.objects.create(name="Art", slug="art")
    return render(request, 'room/rooms.html', {'rooms': rooms})


@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:10]
    return render(request, 'room/room.html', {'room': room, 'messages': messages})