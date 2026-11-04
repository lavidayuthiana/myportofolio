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
        self.assertContains(response, f'href="{reverse("main:show_main")}"')
        # Sejak Tugas 5 data dimuat lewat AJAX, jadi isi kartu dicek dari API
        data = self.client.get(reverse("api:experience-list")).json()
        self.assertEqual(data[0]["title"], self.experience.title)
        self.assertEqual(data[0]["description"], self.experience.description)
        self.assertEqual(data[0]["category_display"], "Part-Time")
        self.assertTrue(data[0]["is_ongoing"])

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan")
        self.assertEqual(self.client.get(reverse("api:experience-list")).json(), [])

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        data = self.client.get(reverse("api:experience-list")).json()

        self.assertFalse(self.experience.is_ongoing)
        self.assertFalse(data[0]["is_ongoing"])

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
        data = self.client.get(reverse("main:get_education_json")).json()

        self.assertEqual(data[0]["fields"]["institution_name"], self.education.institution_name)
        self.assertEqual(data[0]["fields"]["degree"], self.education.degree)

    def test_empty_education_page(self):
        Education.objects.all().delete()
        response = self.client.get(reverse("main:show_education"))

        self.assertContains(response, "Belum ada pendidikan yang ditambahkan")
        self.assertEqual(self.client.get(reverse("main:get_education_json")).json(), [])

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
        data = self.client.get(reverse("main:get_volunteer_json")).json()

        self.assertEqual(data[0]["fields"]["organization_name"], self.volunteer.organization_name)
        self.assertEqual(data[0]["fields"]["degree"], self.volunteer.degree)

    def test_empty_volunteer_page(self):
        Volunteer.objects.all().delete()
        response = self.client.get(reverse("main:show_volunteer"))

        self.assertContains(response, "Belum ada kegiatan volunteer yang ditambahkan")
        self.assertEqual(self.client.get(reverse("main:get_volunteer_json")).json(), [])