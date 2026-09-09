from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Lavida Yuthiana Faizah",
        "npm": "2506605941",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Hello! I'm a CS student who is passionate about technology. "
            "Interested in exploring new technologies and developing innovative solutions."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Lavida Yuthiana Faizah",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)
