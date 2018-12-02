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


def rate_view(request):
    can_id = request.GET.get("id")
    rate_type = request.GET.get("type")
    trashcan = Trashcan.objects.all().filter(id=can_id)[0]
    if rate_type == "full":
        trashcan.full_rating += 1
    elif rate_type == "missing":
        trashcan.missing_rating += 1
    elif rate_type == "success":
        trashcan.full_rating = max(0, trashcan.full_rating - 1)
        trashcan.missing_rating = max(0, trashcan.missing_rating - 1)
    trashcan.save()
    return redirect("../map")



