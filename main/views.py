import datetime

from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from main.forms import EducationForm, VolunteerForm, ExperienceForm
from main.models import Education, Experience, Volunteer


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Lavida Yuthiana Faizah",
        "npm": "2506605941",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Hello! I'm a CS student who is passionate about technology. "
            "Interested in exploring new technologies and developing innovative solutions."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)

# ----------------------------- Auth -----------------------------

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Lavida Yuthiana Faizah",
        "form": form,
    }
    return render(request, "register.html", context)


def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Lavida Yuthiana Faizah",
        "form": form,
    }
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

# ----------------------------- Experience -----------------------------

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Lavida Yuthiana Faizah",
        "form": form,
    }
    return render(request, "experience_form.html", context)

def edit_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman berhasil diperbarui!")
        return redirect("main:show_experience")

    context = {
        "name": "Lavida Yuthiana Faizah",
        "form": form,
        "is_edit": True,
    }
    return render(request, "experience_form.html", context)

def get_experience_json(request):
    query = request.GET.get("title", "").strip()
    experience = Experience.objects.all()

    if query:
        experience = experience.filter(institution_name__icontains=query)

    experience_json = serializers.serialize("json", experience)
    return HttpResponse(experience_json, content_type="application/json")

def show_experience(request):
    json_response = get_experience_json(request)

    experience = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experience = [item.object for item in experience]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Lavida Yuthiana Faizah",
        "experience_list": experience,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")


# ----------------------------- Education -----------------------------

def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Riwayat pendidikan berhasil ditambahkan!")
        return redirect("main:show_education")

    context = {
        "name": "Lavida Yuthiana Faizah",
        "form": form,
    }
    return render(request, "education_form.html", context)

def edit_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)
    form = EducationForm(request.POST or None, instance=education)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Riwayat pendidikan berhasil diperbarui!")
        return redirect("main:show_education")

    context = {
        "name": "Lavida Yuthiana Faizah",
        "form": form,
        "is_edit": True,
    }
    return render(request, "education_form.html", context)


def get_education_json(request):
    query = request.GET.get("institution_name", "").strip()
    education = Education.objects.all()

    if query:
        education = education.filter(institution_name__icontains=query)

    education_json = serializers.serialize("json", education)
    return HttpResponse(education_json, content_type="application/json")


def show_education(request):
    json_response = get_education_json(request)

    education = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    education = [item.object for item in education]
    title_query = request.GET.get("institution_name", "").strip()

    context = {
        "name": "Lavida Yuthiana Faizah",
        "education_list": education,
        "title_query": title_query,
    }
    return render(request, "education.html", context)

def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Riwayat pendidikan berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:show_education")


# ----------------------------- Volunteer -----------------------------

def create_volunteer(request):
    form = VolunteerForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Kegiatan volunteer berhasil ditambahkan!")
        return redirect("main:show_volunteer")

    context = {
        "name": "Lavida Yuthiana Faizah",
        "form": form,
    }
    return render(request, "volunteer_form.html", context)

def edit_volunteer(request, volunteer_id):
    volunteer = get_object_or_404(Volunteer, pk=volunteer_id)
    form = VolunteerForm(request.POST or None, instance=volunteer)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Kegiatan volunteer berhasil diperbarui!")
        return redirect("main:show_volunteer")

    context = {
        "name": "Lavida Yuthiana Faizah",
        "form": form,
        "is_edit": True,
    }
    return render(request, "volunteer_form.html", context)


def get_volunteer_json(request):
    query = request.GET.get("organization_name", "").strip()
    volunteer = Volunteer.objects.all()

    if query:
        volunteer = volunteer.filter(organization_name__icontains=query)

    volunteer_json = serializers.serialize("json", volunteer)
    return HttpResponse(volunteer_json, content_type="application/json")


def show_volunteer(request):
    json_response = get_volunteer_json(request)

    volunteer = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    volunteer = [item.object for item in volunteer]
    title_query = request.GET.get("organization_name", "").strip()

    context = {
        "name": "Lavida Yuthiana Faizah",
        "volunteer_list": volunteer,
        "title_query": title_query,
    }
    return render(request, "volunteer.html", context)


def delete_volunteer(request, volunteer_id):
    volunteer = get_object_or_404(Volunteer, pk=volunteer_id)

    if request.method == "POST":
        volunteer.delete()
        messages.success(request, "Kegiatan volunteer berhasil dihapus!")
        return redirect("main:show_volunteer")

    return redirect("main:show_volunteer")