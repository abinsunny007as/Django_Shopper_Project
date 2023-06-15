from django.shortcuts import render, redirect
from myapp.models import CategoryDB, ProductDB, ContactDB
from webapp.models import signupDB, cartDB
from django.contrib import messages

# Create your views here.
def home(req):
    Cat = CategoryDB.objects.all()
    return render(req, "home.html", {'Cat': Cat})

def about(req):
    Cat = CategoryDB.objects.all()
    return render(req, "about.html", {'Cat': Cat})

def contact(req):
    Cat = CategoryDB.objects.all()
    return render(req, "contact.html", {'Cat': Cat})

def contactsave(req):
    if req.method == "POST":
        fn = req.POST.get('fname')
        ln = req.POST.get('lname')
        em = req.POST.get('email')
        sub = req.POST.get('subject')
        mes = req.POST.get('message')
        obj = ContactDB(Fname=fn, Lname=ln, Email=em, Subject=sub, Message=mes)
        obj.save()
        return redirect(contact)


def cart(req):
    Cat = CategoryDB.objects.all()
    return render(req, "cart.html", {'Cat': Cat})

def product(req, cat_name):
    Cat = CategoryDB.objects.all()
    pro = ProductDB.objects.filter(Select=cat_name)
    return render(req, "product.html", {'Cat': Cat, 'pro': pro})

def singleproduct(req, pro_id):
    Cat = CategoryDB.objects.all()
    pro_single = ProductDB.objects.get(id=pro_id)
    pro = ProductDB.objects.all()
    return render(req, "singleproduct.html", {'Cat': Cat, 'pro_single': pro_single, 'pro': pro})

def RegisterPage(req):
    return render(req, "signup.html")

def saveregister(req):
    if req.method == "POST":
        na = req.POST.get('uname')
        em = req.POST.get('email')
        ph = req.POST.get('mobile')
        pswd = req.POST.get('pswd')
        cpswd = req.POST.get('cpswd')
        pro = req.FILES['pimg']
        obj = signupDB(Username=na, Email=em, Phone=ph, password=pswd, Confrim_pswd=cpswd, Profile_img=pro)
        obj.save()
        messages.success(req, "Register is successfull!!")
        return redirect(RegisterPage)

def userlogin(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('pswd')
        if signupDB.objects.filter(Username=username, password=password).exists():
            request.session['Username'] = username
            request.session['password'] = password
            messages.success(request, "Userlogin is success!!")
            return redirect(home)
        else:
            messages.error(request, "Username or password is unsuccess!!")
            return redirect(RegisterPage)
    messages.error(request, "Username or password is unsuccess!!")
    return redirect(RegisterPage)

def userlogout(request):
    del request.session['Username']
    del request.session['password']
    return redirect(RegisterPage)

def cartpage(req):
    Cat = CategoryDB.objects.all()
    cart = cartDB.objects.filter(Username=req.session['Username'])
    return render(req, "cart.html", {'cart': cart, 'Cat': Cat})

def cartsave(req):
    if req.method == "POST":
        user = req.POST.get('username')
        brand = req.POST.get('brand')
        pri = req.POST.get('price')
        qua = req.POST.get('qty')
        tot = req.POST.get('tot')
        obj = cartDB(Username=user, Brand=brand, Price=pri, Quality=qua, Total=tot)
        obj.save()
        return redirect(cartpage)

def deletecart(req, cart_id):
    cart = cartDB.objects.get(id=cart_id)
    cart.delete()
    return redirect(cartpage)

def checkoutpage(req):
    Cat = CategoryDB.objects.all()
    return render(req, "checkout.html", {'Cat': Cat})

