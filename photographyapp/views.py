from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import item
from .models import shop
from .forms import ModelForm
from django.contrib import messages

# shop functions

def demo(request):
    product = shop.objects.all()
    return render(request, 'home.html', {'products': product})


def detail(request, book_id):
    product1 = shop.objects.get(id=book_id)
    return render(request, 'detail.html', {'product': product1})


# item functions


def item1(request):
    product2 = item.objects.all()

    return render(request, 'home.html', {'products2': product2})


def item2(request, shop_id):
    itemproduct = item.objects.get(id=shop_id)
    return render(request, 'item.html', {'itemproducts': itemproduct})


# add product function

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        img = request.FILES['img']
        location = request.POST.get('location')
        price = request.POST.get('price')
        s = shop(name=name, img=img, location=location, price=price)
        s.save()
        print('product added')
        return redirect('demo')
    else:
        print("not product here")

    return render(request, 'add_product.html')


# update function

def update(request, id):
    obj = shop.objects.get(id=id)
    form = ModelForm(request.POST or None, request.FILES, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/demo')
    return render(request, 'edit.html', {'form': form, 'obj': obj})


def delete(request, id):
    if request.method == 'POST':
        obj = shop.objects.get(id=id)
        obj.delete()
        return redirect('demo')
    return render(request, 'delete.html')


