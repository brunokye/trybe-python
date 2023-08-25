from django.shortcuts import render, redirect
from playlists.forms import CreateSingerForm
from playlists.forms import CreateMusicModelForm
from playlists.models import Music, Singer


def singer(request):
    form = CreateSingerForm()

    if request.method == "POST":
        form = CreateSingerForm(request.POST)

        if form.is_valid():
            Singer.objects.create(**form.cleaned_data)
            return redirect("home-page")

    context = {"form": form}

    return render(request, "singer.html", context)


def music(request):
    form = CreateMusicModelForm()

    if request.method == "POST":
        form = CreateMusicModelForm(request.POST)

        if form.is_valid():
            Music.objects.create(**form.cleaned_data)
            return redirect("home-page")

    context = {"form": form}

    return render(request, "music.html", context)


def index(request):
    context = {"musics": Music.objects.all()}
    return render(request, "home.html", context)
