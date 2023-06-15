from django.shortcuts import render, redirect
from myapp.models import CategoryDB, ProductDB, ContactDB
from webapp.views import contact
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def indexpage(req):
    return render(req, "indexpage.html")

def add_category(req):
    return render(req, "add_category.html")

def save_category(req):
    if req.method == "POST":
        na = req.POST.get('name')
        image = req.FILES['img']
        des = req.POST.get('des')
        obj = CategoryDB(Categoryname = na, CatImage = image, Description = des)
        obj.save()
        messages.success(req, "Category saved successfully..!")
        return redirect(add_category)

def display_contact(req):
    contact = ContactDB.objects.all()
    return render(req, "Displaycontact.html", {'data': contact})

def deletecontact(req, proid):
    data = ContactDB.objects.get(id=proid)
    data.delete()
    return redirect(display_contact)

def display_category(req):
    category = CategoryDB.objects.all()
    return render(req, "display_category.html", {'data': category})

def edit_category(req, dataid):
    data = CategoryDB.objects.get(id=dataid)
    return render(req, "edit_category.html", {'data': data})

def update_category(req, dataid):
    if req.method == "POST":
        na = req.POST.get('name')
        des = req.POST.get('des')
        try:
            img = req.FILES['img']
            fs = FileSystemStorage()
            Image =fs.save(img.name, img)
        except MultiValueDictKeyError:
            Image = CategoryDB.objects.get(id=dataid).CatImage
        CategoryDB.objects.filter(id=dataid).update(Categoryname=na, Description=des, CatImage=Image)
        return redirect(display_category)

def delete_category(req, dataid):
    category = CategoryDB.objects.filter(id=dataid)
    category.delete()
    return redirect(display_category)

def addproduct(request):
    product = CategoryDB.objects.all()
    return render(request, "addproduct.html", {'data': product})

def saveproduct(request):
    if request.method == "POST":
        cna = request.POST.get('select')
        pna = request.POST.get('pname')
        br = request.POST.get('brand')
        pr = request.POST.get('price')
        de = request.POST.get('des')
        pf = request.FILES['pfile']
        obj = ProductDB(Select=cna, Pname=pna, Brand=br, Price=pr, Des=de, ProductImage=pf)
        obj.save()
        messages.success(request, "Product saved successfully..!")
        return redirect(addproduct)

def displayproduct(request):
    product = ProductDB.objects.all()
    return render(request, "displayproduct.html", {'data': product})

def editproduct(requst, proid):
    category = CategoryDB.objects.all()
    product = ProductDB.objects.get(id=proid)
    return render(requst, "editproduct.html", {'category': category, 'product': product})

def updateproduct(request, proid):
    if request.method == "POST":
        cna = request.POST.get('select')
        pna = request.POST.get('pname')
        br = request.POST.get('brand')
        pr = request.POST.get('price')
        de = request.POST.get('des')
        try:
            pimg = request.FILES['pfile']
            fs = FileSystemStorage()
            file = fs.save(pimg.name, pimg)
        except MultiValueDictKeyError:
            file= ProductDB.objects.get(id=proid).ProductImage
        ProductDB.objects.filter(id=proid).update(Select=cna, Pname=pna, Brand=br, Price=pr, Des=de, ProductImage=file)
        return redirect(displayproduct)

def deleteproduct(req, proid):
    data = ProductDB.objects.get(id=proid)
    data.delete()
    return redirect(displayproduct)

def loginpage(req):
    return render(req, "adminlogin.html")

def Login(req):
    if req.method == "POST":
        uname = req.POST.get('username')
        pswd = req.POST.get('password')
        if User.objects.filter(username__contains=uname).exists():
            user = authenticate(username=uname, password=pswd)
            if user is not None:
                login(req, user)
                req.session['username']= uname
                req.session['password']= pswd
                messages.success(req, "Admin Login success!!")
                return redirect(indexpage)
            else:
                messages.error(req, "Username or password is unsuccess!!")
                return redirect(loginpage)
        else:
            messages.error(req, "Username or password is unsuccess!!")
            return redirect(loginpage)

def deletesession(req):
    del req.session['username']
    del req.session['password']
    return redirect(loginpage)





