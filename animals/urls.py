from django.urls import path
from .views import CatList, CatDetail, DogList, DogDetail, AnimalList, AnimalDetail, search


app_name = 'animals'
urlpatterns = [
    path('cats/', CatList.as_view(), name='cat_list'),
    path('cat/<str:pk>', CatDetail.as_view(), name='cat_detail'),
    path('dogs/', DogList.as_view(), name='dog_list'),
    path('dog/<str:pk>', DogDetail.as_view(), name='dog_detail'),
    path('others/', AnimalList.as_view(), name='animal_list'),
    path('animal/<str:pk>', AnimalDetail.as_view(), name='animal_detail'),
    path('search/', search)
]
