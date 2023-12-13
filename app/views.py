from django.shortcuts import render
from .models import Phones
from django.http import HttpResponseRedirect, HttpResponseNotFound



# получение данных
def index(request):
    phone = Phones.objects.all()
    return render(request, 'index.html', context={'phone': phone})


# Сохранение данных
def create(request):
    if request.method == 'POST':
        phone = Phones()
        phone.name = request.POST.get('name')
        phone.info = request.POST.get('info')
        phone.price = request.POST.get('price')
        phone.author = request.POST.get('author')
        phone.save()
    return HttpResponseRedirect('/')


# Изменение
def edit(request, id):
    try:
        phone = Phones.objects.get(id=id)

        if request.method == 'POST':
            phone.name = request.POST.get('name')
            phone.info = request.POST.get('info')
            phone.price = request.POST.get('price')
            phone.author = request.POST.get('author')
            phone.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'edit.html', {'phone': phone})
    except Phones.DoesNotExist:
        return HttpResponseNotFound('<h2>Phone not found</h2>')

def delete(request, id):
    try:
        phone = Phones.objects.get(id=id)
        phone.delete()
        return HttpResponseRedirect('/')
    except Phones.DoesNotExist:
        return HttpResponseNotFound('<h2>Phone not found</h2>')
