from django.shortcuts import render

from main.models import Experience
from main.models import Education
from main.models import Volunteer


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

def show_education(request):
    context = {
        "name": "Lavida Yuthiana Faizah",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)

def show_volunteer(request):
    context = {
        "name": "Lavida Yuthiana Faizah",
        "volunteer_list": Volunteer.objects.all(),
    }
    return render(request, "volunteer.html", context)
