from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from trshy.settings import API_KEY

from locator.models import Trashcan


def index_view(request):
    return render(request, "index.html", {})


def profile_view(request):
    if not request.user.is_authenticated:
        return redirect("/")
    return render(request, "profile.html", {})


def map_view(request):
    if not request.user.is_authenticated:
        return redirect("/")
    trashcans = Trashcan.objects.all()
    return render(request, "map.html", {"trashcans": trashcans, "api": API_KEY})


def trashcan_view(request, object_id=None):
    if not request.user.is_authenticated:
        return redirect("/")
    instance = get_object_or_404(Trashcan, id=id)
    return render(request, "map.html", {"trashcan": instance})