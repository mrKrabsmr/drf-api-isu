from django.urls import include, path


urlpatterns = [
    path("user/", include("api.v1.users.urls")),
    path("resume/", include("api.v1.resume.urls")),
    path("job/", include("api.v1.jobs.urls")),
    path("work/", include("api.v1.works.urls"))
]