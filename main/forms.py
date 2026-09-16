from django.forms import (
    ModelForm,
    TextInput,
    Textarea,
    URLInput,
    Select,
    DateInput,
    NumberInput,
)

from main.models import Education, Volunteer


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