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
    edit_education,
    edit_volunteer,
    create_experience,
    get_experience_json,
    edit_experience,
    delete_experience,
    register,
    login_user,
    logout_user,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/api/", get_experience_json, name="get_experience_json"),
    path("experience/<uuid:experience_id>/edit/", edit_experience, name="edit_experience"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),

    path("education/", show_education, name="show_education"),
    path("education/add/", create_education, name="create_education"),
    path("education/api/", get_education_json, name="get_education_json"),
    path("education/<uuid:education_id>/delete/", delete_education, name="delete_education"),
    path("education/<uuid:education_id>/edit/", edit_education, name="edit_education"),

    path("volunteer/", show_volunteer, name="show_volunteer"),
    path("volunteer/add/", create_volunteer, name="create_volunteer"),
    path("volunteer/api/", get_volunteer_json, name="get_volunteer_json"),
    path("volunteer/<uuid:volunteer_id>/delete/", delete_volunteer, name="delete_volunteer"),
    path("volunteer/<uuid:volunteer_id>/edit/", edit_volunteer, name="edit_volunteer"),
]