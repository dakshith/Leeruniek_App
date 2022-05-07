from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('pupilList', views.pupilList),
    path('gradeList', views.gradeList),
    path('pupilScore', views.pupilScore),
    path('scores', views.scores)
]