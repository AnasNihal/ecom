from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Product,category,Profile
from django.contrib.auth.models import User,auth
from .forms import ProductForm,ProfileForm
from django.contrib import messages
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from django.core.exceptions import ObjectDoesNotExist
from django.core.cache import cache



def home(request):
    db = Product.objects.all()[:6]
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
    cat=category.objects.all()
    if cache.get('data'):
        db=cache.get('data')
        print("db cache")
    else:
       db = Product.objects.all()
       cache.set('data',db)
       print("db product")
    m = request.COOKIES.get('mode','light')
    return render(request,"product.html",{"product":db,"cat":cat,"theme":m} )

def setcookies(request):
    m = request.COOKIES.get('mode','light')

    # print(m)
    if m == "light":
        m = 'dark'
    else:
        m='light'
    print(m)
    
    res = redirect('products')
    res.set_cookie('mode',m)
    return res





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

def profile(request):
    product = Product.objects.filter(us = request.user)
    return render(request,"profile.html",{"product":product})

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
        return render(request,"addproduct.html",{"fm":f})


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
            return render(request,"addproduct.html",{"fm":f})
        
        return render(request,"404.html")

def profile_image_update(request):
    if request.method == 'POST':
        
        try:
            UserProfile = request.user.profile
        except ObjectDoesNotExist   :
            UserProfile = Profile.objects.create(user=request.user)
            messages.info(request, "A profile was created for your account as it was missing.")

        form = ProfileForm (request.POST,request.FILES,instance=UserProfile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            return redirect('profile')
    else:
        return redirect('profile')

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













@api_view(['GET'])
def apiproducts(request):
    x=Product.objects.all()
    y=ProductSerializer(x,many=True)
    return Response(y.data)

@api_view(['GET'])
def apisingleproducts(request,id):
    x=Product.objects.get(id=id)
    y=ProductSerializer(x,many=False)
    return Response(y.data)

def new(request):
    return render(request,"api.html")

@api_view(['POST'])
def apiforedit(request):
    x=ProductSerializer(data=request.data)
    if x.is_valid:
        x.save()
        return Response(x.data)
    


@api_view(['POST'])
@permission_classes([AllowAny])
def apiregister(request):
    Uname = request.data.get('username')
    Pword = request.data.get('password')

    if Uname is None or Pword is None:
        return Response({'error':'Please provide Username and password '},status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(username =Uname).exists():
        return Response({'Error':"Username already taken"},status=status.HTTP_400_BAD_REQUEST)
    
    user =User.objects.create_user(username=Uname,password=Pword)
    token ,_ = Token.objects.get_or_create(user=user)

    return Response({'token':token.key,'username':user.username})

@api_view(['POST'])
@permission_classes([AllowAny])
def apilogin(request):
    Uname = request.data.get('username')
    Pword = request.data.get('password')
        
    user = auth.authenticate(username = Uname,password = Pword)

    if not user:
        return Response({'error':"Invalid Credintials"},status=status.HTTP_401_UNAUTHORIZED)
    
    token,_ = Token.objects.get_or_create(user=user)
    return Response({'token':token.key,'username':user.username})