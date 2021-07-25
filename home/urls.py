from django.contrib import admin
from django.urls import path
from home import views
from .views import aboutus, acs, online_councelling, newsandnotices, bcis_syllabus, globalconnection, student, bba_syllabus, bba_bi_syllabus, bba_tt_syllabus, mba_evening_syllabus, mba_syllabus

urlpatterns = [
    path("", views.index, name='home'),
    path("aboutus", aboutus),
    path("acs", acs),
    path("globalconnection", globalconnection),
    path("student", student),

    path("bcis-syllabus", bcis_syllabus),
    path("bba-syllabus", bba_syllabus),
    path("bba-bi-syllabus", bba_bi_syllabus),
    path("bba-tt-syllabus", bba_tt_syllabus),
    path("mba-syllabus", mba_syllabus),
    path("mba-evening-syllabus", mba_evening_syllabus),
    path("oc", online_councelling),
    path("newsandnotices", newsandnotices),




]