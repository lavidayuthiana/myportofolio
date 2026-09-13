from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Education, Volunteer


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "On-Going")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Completed")
        self.assertNotContains(response, "On-Going")

class EducationTest(TestCase):
    def setUp(self):
        self.education = Education.objects.create(
            institution_name="Fakultas Ilmu Komputer UI",
            degree="S1 Sistem Informasi",
            score_label="ipk",
            score_value="3.37",
        )

    def test_education_url_is_accessible_and_uses_correct_template(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")

    def test_education_data_appears_on_page(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertContains(response, self.education.institution_name)
        self.assertContains(response, self.education.degree)

    def test_empty_education_page(self):
        Education.objects.all().delete()
        response = self.client.get(reverse("main:show_education"))

        self.assertContains(response, "Belum ada education yang ditambahkan.")

class VolunteerTest(TestCase):
    def setUp(self):
        self.volunteer = Volunteer.objects.create(
            organization_name="Open House Fasilkom UI",
            degree="Mentor",
            description="Membimbing dan mengajar mentee tentang Fasilkom UI.",
        )

    def test_volunteer_url_is_accessible_and_uses_correct_template(self):
        response = self.client.get(reverse("main:show_volunteer"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "volunteer.html")

    def test_volunteer_data_appears_on_page(self):
        response = self.client.get(reverse("main:show_volunteer"))

        self.assertContains(response, self.volunteer.organization_name)
        self.assertContains(response, self.volunteer.degree)

    def test_empty_volunteer_page(self):
        Volunteer.objects.all().delete()
        response = self.client.get(reverse("main:show_volunteer"))

        self.assertContains(response, "Belum ada kegiatan volunteer yang ditambahkan.")