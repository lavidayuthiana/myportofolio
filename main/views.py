import datetime

from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from main.forms import EducationForm, VolunteerForm, ExperienceForm
from main.models import Education, Experience, Volunteer
from django.core.exceptions import PermissionDenied

def is_editor(user):
    return user.groups.filter(name="Editor").exists()


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

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
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

@login_required(login_url="/login/")
def edit_experience(request, experience_id):
    if not (request.user.is_superuser or is_editor(request.user)):
        raise PermissionDenied
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
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.prefetch_related("starred_by").all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    data = []
    for experience in experiences:
        starred_users = experience.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(experience.id),
            "fields": {
                "title": experience.title,
                "description": experience.description,
                "category": experience.category,
                "category_display": experience.get_category_display(),
                "thumbnail": experience.thumbnail,
                "started_at": experience.started_at.isoformat() if experience.started_at else None,
                "ended_at": experience.ended_at.isoformat() if experience.ended_at else None,
                "is_ongoing": experience.is_ongoing,
                "star_count": len(starred_users),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            },
        })

    return JsonResponse(data, safe=False)

def show_experience(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Lavida Yuthiana Faizah",
        "title_query": title_query,
        "form": ExperienceForm(),
    }
    return render(request, "experience.html", context)

@require_POST
def create_experience_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan pengalaman."},
            status=403,
        )

    form = ExperienceForm(request.POST)
    if form.is_valid():
        experience = form.save()
        return JsonResponse(
            {"message": "Pengalaman berhasil ditambahkan.", "pk": str(experience.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")

    return redirect("main:show_experience")

@login_required(login_url="/login/")
def toggle_star(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")

# ----------------------------- Education -----------------------------

@login_required(login_url="/login/")
def create_education(request):
    if not request.user.is_superuser:
        raise PermissionDenied
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

@login_required(login_url="/login/")
def edit_education(request, education_id):
    if not (request.user.is_superuser or is_editor(request.user)):
        raise PermissionDenied
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

def serialize_education(education, user):
    """Mengubah objek Education menjadi dict JSON, termasuk info star untuk user saat ini."""
    starred_users = list(education.starred_by.all())
    return {
        "pk": str(education.id),
        "fields": {
            "institution_name": education.institution_name,
            "degree": education.degree,
            "description": education.description,
            "logo": education.logo,
            "score_label_display": education.get_score_label_display(),
            "score_value": str(education.score_value),
            "started_at": education.started_at.isoformat() if education.started_at else None,
            "ended_at": education.ended_at.isoformat() if education.ended_at else None,
            "is_ongoing": education.is_ongoing,
            "star_count": len(starred_users),
            "is_starred": user.is_authenticated and user in starred_users,
            "starred_by_names": ", ".join(u.username for u in starred_users),
        },
    }


def get_education_json(request):
    query = request.GET.get("institution_name", "").strip()
    educations = Education.objects.prefetch_related("starred_by").all()
    if query:
        educations = educations.filter(institution_name__icontains=query)
    data = [serialize_education(edu, request.user) for edu in educations]
    return JsonResponse(data, safe=False)


def show_education(request):
    context = {
        "name": "Lavida Yuthiana Faizah",
        "title_query": request.GET.get("institution_name", "").strip(),
        "form": EducationForm(),
    }
    return render(request, "education.html", context)

@login_required(login_url="/login/")
def delete_education(request, education_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Riwayat pendidikan berhasil dihapus!")

    return redirect("main:show_education")

@login_required(login_url="main:login")
@require_POST
def toggle_star_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)
    if education.starred_by.filter(pk=request.user.pk).exists():
        education.starred_by.remove(request.user)
    else:
        education.starred_by.add(request.user)
    return redirect("main:show_education")

@require_POST
def create_education_ajax(request):
    # Cek hak akses di server, bukan cuma menyembunyikan tombol di template
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan pendidikan."},
            status=403,
        )

    form = EducationForm(request.POST)
    if form.is_valid():
        education = form.save()
        return JsonResponse(
            {"message": "Riwayat pendidikan berhasil ditambahkan.",
             "data": serialize_education(education, request.user)},
            status=201,
        )
    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)


# ----------------------------- Volunteer -----------------------------

@login_required(login_url="/login/")
def create_volunteer(request):
    if not request.user.is_superuser:
        raise PermissionDenied
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

@login_required(login_url="/login/")
def edit_volunteer(request, volunteer_id):
    if not (request.user.is_superuser or is_editor(request.user)):
        raise PermissionDenied
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

    volunteer_json = serializers.serialize("json", volunteer, fields=["organization_name", "degree", "description", "logo", "started_at", "ended_at"])
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
        "is_editor": is_editor(request.user),
    }
    return render(request, "volunteer.html", context)


@login_required(login_url="/login/")
def delete_volunteer(request, volunteer_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    volunteer = get_object_or_404(Volunteer, pk=volunteer_id)

    if request.method == "POST":
        volunteer.delete()
        messages.success(request, "Kegiatan volunteer berhasil dihapus!")

    return redirect("main:show_volunteer")

@login_required(login_url="main:login")
@require_POST
def toggle_star_volunteer(request, volunteer_id):
    volunteer = get_object_or_404(Volunteer, pk=volunteer_id)
    if volunteer.starred_by.filter(pk=request.user.pk).exists():
        volunteer.starred_by.remove(request.user)
    else:
        volunteer.starred_by.add(request.user)
    return redirect("main:show_volunteer")