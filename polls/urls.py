from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_UserProfile, name='start'),
    path('quest_1', views.questionnaire_part1, name='quest_1'),
    path('vid_1', views.vid_part1, name='vid_1'),
    path('infographic', views.infographic, name='infographic'),
    path('quest_3', views.questionnaire_part3, name='quest_3'),
    path('quest_4', views.questionnaire_part4, name='quest_4'),
    path('vid_2', views.vid_part2, name='vid_2'),
    path('vid_3', views.vid_part3, name='vid_3'),
    path('quest_5', views.questionnaire_part5, name='quest_5'),

]
