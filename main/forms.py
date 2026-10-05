from django.forms import (
    ModelForm,
    TextInput,
    Textarea,
    URLInput,
    Select,
    DateInput,
    NumberInput,
    DateTimeInput,
)

from main.models import Education, Volunteer, Experience
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "institution_name",
            "degree",
            "description",
            "logo",
            "score_label",
            "score_value",
            "started_at",
            "ended_at",
        ]

        labels = {
            "institution_name": "Nama Institusi",
            "degree": "Jenjang",
            "description": "Deskripsi (organisasi/prestasi)",
            "logo": "URL Logo",
            "score_label": "Label Nilai",
            "score_value": "Nilai",
            "started_at": "Mulai",
            "ended_at": "Selesai",
        }

        widgets = {
            "institution_name": TextInput(
                attrs={"placeholder": "Universitas Indonesia", "maxlength": 255}
            ),
            "degree": TextInput(
                attrs={"placeholder": "S1 Sistem Informasi", "maxlength": 255}
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Organisasi atau prestasi selama masa studi",
                    "rows": 3,
                }
            ),
            "logo": URLInput(
                attrs={"placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000"}
            ),
            "score_label": Select(),
            "score_value": NumberInput(attrs={"step": "0.01", "min": "0"}),
            "started_at": DateInput(attrs={"type": "date"}),
            "ended_at": DateInput(attrs={"type": "date"}),
        }
        
    def clean_institution_name(self):
        name = strip_tags(self.cleaned_data["institution_name"]).strip()
        if not name:
            raise ValidationError("Nama institusi tidak boleh hanya berisi tag HTML.")
        return name

    def clean_degree(self):
        degree = strip_tags(self.cleaned_data["degree"]).strip()
        if not degree:
            raise ValidationError("Jenjang tidak boleh hanya berisi tag HTML.")
        return degree

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()


class VolunteerForm(ModelForm):
    class Meta:
        model = Volunteer
        fields = [
            "organization_name",
            "degree",
            "description",
            "logo",
            "started_at",
            "ended_at",
        ]

        labels = {
            "organization_name": "Nama Organisasi",
            "degree": "Peran/Jabatan",
            "description": "Deskripsi Kegiatan",
            "logo": "URL Logo",
            "started_at": "Mulai",
            "ended_at": "Selesai",
        }

        widgets = {
            "organization_name": TextInput(
                attrs={"placeholder": "BEM Fasilkom UI", "maxlength": 255}
            ),
            "degree": TextInput(
                attrs={"placeholder": "Staff Divisi Acara", "maxlength": 255}
            ),
            "description": Textarea(
                attrs={"placeholder": "Ceritakan kegiatan volunteer-mu", "rows": 3}
            ),
            "logo": URLInput(
                attrs={"placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000"}
            ),
            "started_at": DateInput(attrs={"type": "date"}),
            "ended_at": DateInput(attrs={"type": "date"}),
        }

    def clean_organization_name(self):
        name = strip_tags(self.cleaned_data["organization_name"]).strip()
        if not name:
            raise ValidationError("Nama organisasi tidak boleh hanya berisi tag HTML.")
        return name

    def clean_degree(self):
        degree = strip_tags(self.cleaned_data["degree"]).strip()
        if not degree:
            raise ValidationError("Peran/jabatan tidak boleh hanya berisi tag HTML.")
        return degree

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ["title", "description", "category", "thumbnail", "started_at", "ended_at"]

        labels = {
            "title": "Judul Pengalaman",
            "description": "Deskripsi",
            "category": "Kategori",
            "thumbnail": "URL Logo/Thumbnail",
            "started_at": "Mulai",
            "ended_at": "Selesai",
        }

        widgets = {
            "title": TextInput(attrs={"placeholder": "Asisten Dosen PBP", "maxlength": 255}),
            "description": Textarea(attrs={"placeholder": "Ceritakan pengalamanmu", "rows": 3}),
            "category": Select(),
            "thumbnail": URLInput(attrs={"placeholder": "https://..."}),
            "started_at": DateTimeInput(format="%Y-%m-%dT%H:%M", attrs={"type": "datetime-local"}),
            "ended_at": DateTimeInput(format="%Y-%m-%dT%H:%M", attrs={"type": "datetime-local"}),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Judul pengalaman tidak boleh hanya berisi tag HTML.")
        return title

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()