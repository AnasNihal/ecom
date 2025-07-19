from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Product,category
from django.contrib.auth.models import User,auth
from .forms import ProductForm
from django.contrib import messages


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

def addproduct(request):
    if request.method == 'POST':
        f = ProductForm (request.POST,request.FILES)
        if f.is_valid():
            x = f.save(commit=False)
            x.us=request.user
            x.save()
            return redirect('/')
    else:
        f=ProductForm()
        return render(request,"profile.html",{"fm":f})


def editproduct(request,p_id):
    if request.method == 'POST':
        x=Product.objects.get(id=p_id)
        f = ProductForm (request.POST,request.FILES,instance=x)
        if f.is_valid():
            f.save()
            return redirect('/')
    else:
        x=Product.objects.get(id=p_id)
        
        if x.us == request.user:
            f=ProductForm(instance=x)
            return render(request,"profile.html",{"fm":f})
        
        return render(request,"404.html")


def viewcart(request):
    cart = request.session.get('cart',{})
    product_id = cart.keys()

    products = Product.objects.filter(id__in = product_id)

    cart_items = []
    total = 0

    for product in products:
        qty = cart[str(product.id)]
        subtotal = product.price * qty
        total += subtotal

        cart_items.append({
            "product":product,
            "qty":qty,
            'subtotal': product.price * qty

        })

    return render(request,"cart.html",{
        "cart_items":cart_items,
        "total":total
    })

def addcart(request,d_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=d_id) 
        cart = request.session.get('cart' , {})

        if str(d_id) in cart:
            cart[str(d_id)] += 1
        else:
            cart[str(d_id)] = 1

        request.session['cart'] = cart
        return redirect('viewcart')
    else:
        return redirect('login')



def increase_qty(request,i_id):
    cart = request.session.get('cart',{})
     
    if str(i_id):
        cart[str(i_id)] += 1
    else:
        cart[str(i_id)] = 1
 
    request.session['cart'] = cart
    return redirect('viewcart')


def decrease_qty(request, i_id):
    print("== Decrease view called ==")

    cart = request.session.get('cart', {})
    print("Cart before:", cart)

    if str(i_id) in cart:
        cart[str(i_id)] -= 1
        print(f"Item {i_id} decreased to", cart[str(i_id)])

        if cart[str(i_id)] <= 0:
            del cart[str(i_id)]
            print(f"Item {i_id} removed from cart")

    request.session['cart'] = cart
    print("Cart after:", cart)

    return redirect('viewcart')


def remove_item(request,r_id):
    cart = request.session.get('cart',{})
    product_id = str(r_id)


    if product_id in cart:
        cart.pop(product_id)
        messages.success(request,"Product Removed Success!!")
    else:
        messages.warning(request,"Product was not found")


    request.session['cart'] = cart
    return redirect('viewcart')
