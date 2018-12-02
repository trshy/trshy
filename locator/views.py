from django.shortcuts import render
from django.http import Http404



def index_view(request):
    return render(request, "index.html", {})


def profile_view(request):
    if not request.user.is_authenticated:
        raise Http404
    return render(request, "profile.html", {})