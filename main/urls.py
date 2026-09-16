from django.urls import path

from main.views import (
    show_main,
    show_experience,
    show_education,
    show_volunteer,
    create_education,
    create_volunteer,
    get_education_json,
    get_volunteer_json,
    delete_education,
    delete_volunteer,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),

    path("education/", show_education, name="show_education"),
    path("education/add/", create_education, name="create_education"),
    path("education/api/", get_education_json, name="get_education_json"),
    path("education/<uuid:education_id>/delete/", delete_education, name="delete_education"),

    path("volunteer/", show_volunteer, name="show_volunteer"),
    path("volunteer/add/", create_volunteer, name="create_volunteer"),
    path("volunteer/api/", get_volunteer_json, name="get_volunteer_json"),
    path("volunteer/<uuid:volunteer_id>/delete/", delete_volunteer, name="delete_volunteer"),
]