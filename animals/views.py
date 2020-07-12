from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.template import loader
from django.http import HttpResponse
from django.db.models import Q

from abc import ABC, abstractmethod

from animals.models import Animal, Cat, Dog


class CatList(ListView):
    model = Cat
    template_name = 'cats_list.html'

    def get_queryset(self):
        cats = Cat.objects.all()
        queryset = []
        i = 0
        while i + 2 < len(cats) - 1:
            queryset.append((cats[i], cats[i + 1], cats[i + 2]))
            i += 3
        queryset.append(cats[i:])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['CatsActive'] = 'active'
        return context


class CatDetail(DetailView):

    model = Cat
    template_name = 'cat_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DogList(ListView):
    model = Dog
    template_name = 'dogs_list.html'

    def get_queryset(self):
        dogs = Dog.objects.all()
        queryset = []
        i = 0
        while i + 2 < len(dogs) - 1:
            queryset.append((dogs[i], dogs[i + 1], dogs[i + 2]))
            i += 3
        queryset.append(dogs[i:])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['DogsActive'] = 'active'
        return context


class DogDetail(DetailView):

    model = Dog
    template_name = 'dog_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AnimalList(ListView):

    model = Animal
    template_name = 'animals_list.html'

    def get_queryset(self):
        animals = Animal.objects.all()
        queryset = []
        i = 0
        while i + 2 < len(animals) - 1:
            queryset.append((animals[i], animals[i + 1], animals[i + 2]))
            i += 3
        queryset.append(animals[i:])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['OthersActive'] = 'active'
        return context


class AnimalDetail(DetailView):

    model = Animal
    template_name = 'animal_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def search(request):

    template = loader.get_template('search_results.html')

    if request.method == 'POST':
        q = request.POST.get('search').strip()
        if q:
            res = search_in_db(q)
        else:
            res = []
        data = {'search_results': res}
        return HttpResponse(template.render(data, request))


def search_in_db(q):
    res = []
    res.append(Cat.objects.filter(Q(name__icontains=q) | Q(breed__icontains=q) |
                                  Q(species__icontains=q) | Q(color__icontains=q)))
    res.append(Dog.objects.filter(Q(name__icontains=q) | Q(breed__icontains=q) |
                                  Q(species__icontains=q) | Q(size__icontains=q)))
    res.append(Animal.objects.filter(Q(name__icontains=q) | Q(breed__icontains=q) |
                                     Q(species__icontains=q)))
    return [pet for result in res for pet in result]
