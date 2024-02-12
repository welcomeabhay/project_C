from django.shortcuts import render
from .models import *

# for home page
def Home(request):
    cate = Category.objects.all()

    return render(request, 'index.html',{'cato':cate})

# for about page
def About(request):

    return render(request,'about.html')

# for contact page
def Contact(request):

    return render(request,'contact.html')

# for category page
def CategorY(request):
    cate = Category.objects.all()

    return render(request,'category.html',{'cato':cate})

# for sub_category
def Sub_CategorY(request,cname):
    sub_c = Sub_category.objects.filter(category__name=cname)
    # print("subid:",sub_c.name)

    return render(request,'sub_category.html',{'scato':sub_c})