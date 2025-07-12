from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Product,category
from django.contrib.auth.models import User,auth


def home(request):
    db = Product.objects.all()[:3]
    cat=category.objects.all()
    return render(request,"home.html",{"product":db,"cat":cat} )

def register(request):
    if request.method == 'POST':
        u = request.POST['username']
        e = request.POST['email']
        p1 = request.POST['password1']
        p2 = request.POST['password2']
        if p1 == p2 :
        
            if User.objects.filter(username = u).exists():
                return render(request,"register.html",{"error":"Username Exists"})     
            elif User.objects.filter(email = e).exists():
                return render(request,"register.html",{"error":"Email is already taken"})
            else:

                User.objects.create_user(username=u,email=e,password=p1)
                return redirect('login')
        else:
            return render(request,"register.html",{"error":"Password do not match"})
    else:
        return render(request,"register.html")



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']

        value = auth.authenticate(username = username , password = password)

        if value is not None:
            auth.login(request,value)
            return redirect('home')
        else:
            return render(request,"login.html",{"error":"Invalid Password or Username"})
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('login')


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