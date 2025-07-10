from django.shortcuts import render
from .models import Product,category

def home(request):
    db = Product.objects.all()[:3]
    cat=category.objects.all()
    return render(request,"home.html",{"product":db,"cat":cat} )

def products(request):
    db = Product.objects.all()
    cat=category.objects.all()
    return render(request,"product.html",{"product":db,"cat":cat} )


def viewproduct(request,p_id):
    db=Product.objects.get(id=p_id)
    return render(request,"viewproduct.html",{"product":db})

def filterproduct(request):
    catlist = request.GET.get("category")

    if catlist:
        product = Product.objects.filter(catry = catlist)
    else:
        product = Product.objects.all()

    catogories = category.objects.all()

    return render(request,"filterproduct.html",
                  {"product":product,
                   "cat":catogories,
                   "selected_catry":int(catlist) if catlist else None})