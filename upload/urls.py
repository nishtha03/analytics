from django.urls import path
from django.conf.urls import include, url
from upload import views, crm
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# from helpdesk import views

urlpatterns = [
    # path for views.py
    path('', views.Home.as_view(), name='home'),
    path('upload/', views.upload, name='upload'),
    path('question/', views.question, name='question'),

    path('file/', views.file_reader, name='file'),
    path('Answer1/', views.Answer1, name='Answer1'),
    path('Answer2/', views.Answer2, name='Answer2'),
    path('Answer3/', views.Answer3, name='Answer3'),
    path('Answer6/', views.Answer6, name='Answer6'),
    path('Answer8/', views.Answer8, name='Answer8'),
    # path('Answer1/', views.dynamic, name='home1'),
    url(r'^pdf/$', views.GeneratePdf.as_view(), name='pdf'),

    # path for crm.py
    path('crm/', crm.crm, name='crm'),
    path('crm1/', crm.crm1, name='crm1'),
    path('crm2/', crm.crm2, name='crm2'),
    path('crm3/', crm.crm3, name='crm3'),
    path('crm6/', crm.crm6, name='crm6'),
    path('crm8/', crm.crm8, name='crm8'),
]
urlpatterns += staticfiles_urlpatterns()
