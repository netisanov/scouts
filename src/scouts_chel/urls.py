from django.urls import path
from . import views
from .PersonModel import PersonView

urlpatterns = [
    path('', views.ApiRoot.as_view()),
    path('persons/',
         PersonView.PersonList.as_view(),
         name='person-list'),
    path('persons/<int:pk>',
         PersonView.PersonDetail.as_view(),
         name='person-detail'),
]