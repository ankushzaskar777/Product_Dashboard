from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.

@login_required
def show(request):
    obj = Product.objects.all()
    context ={'prod':obj}
    return render(request,'product/show.html',context)




@login_required
def add(request):
    if request.method == 'POST':
        pid = request.POST.get("pid")
        pname = request.POST.get("pname")
        price = request.POST.get("price")
        description = request.POST.get("description")
        category = request.POST.get("category")
        pimage = request.FILES.get("pimage")

        obj = Product(
            pid=pid,
            pname=pname,
            category=category,
            price=price,
            pimage=pimage,
            description=description
        )
        obj.save()
        
        return redirect("show")
    return render(request, 'product/add.html')


def home(request):
    return render(request, 'product/home.html')




def delete(request,pid):
    obj = Product.objects.get(pid=pid)
    obj.delete()
    return redirect("show")    



def edit(request, pid):
    obj = Product.objects.get(pid=pid)  # Old Data
    context = {'obj': obj}

    if request.method == "POST":
        pname       = request.POST.get('pname')
        price       = request.POST.get("price")
        description = request.POST.get("description")
        category    = request.POST.get("category")
        pimage      = request.FILES.get("pimage")  #  Correct FILES

        obj.pname = pname
        obj.price = price
        obj.description = description
        obj.category = category

        #  Only update image if user uploads new one
        if pimage:
            obj.pimage = pimage  

        obj.save()
        return redirect("show")

    return render(request, 'product/edit.html', context)



def search_products(request):
    query = request.GET.get('q', '').strip()  # Get search input safely

    if query:
        results = Product.objects.filter(pname__icontains=query)
    else:
        results = []  # No blank search error

    return render(request, 'product/search_result.html', {'products': results, 'query': query})




def category(request, category_name):
    return render(request, 'product/category.html', {'category_name': category_name})

def contact(request):
    return render(request, 'product/contact.html')

def login_view(request):
    if request.method == "POST":
        print("POST data:", request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("show") # this is show page...!
        else:
            return render(request, "product/login.html", {"error": "Invalid Username or Password"})
    return render(request, "product/login.html")



def register(request):
    if request.method == "POST":
        username    = request.POST.get("username")
        email       = request.POST.get("email")
        password    = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return render(request, "product/register.html", {"error": "User is already exists"})
        if User.objects.filter(email=email).exists():
            return render(request, "product/register.html", {"error": "Email already registered"})

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect("login")

    return render(request, "product/register.html")

def logout_view(request):
    logout(request)
    return redirect('login')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"From: {name}\nEmail: {email}\n\nMessage:\n{message}"

        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,
            ['yourgmail@gmail.com'],  # Receiver email
        )
        messages.success(request, "Message Sent Successfully ✅")

    return render(request, 'product/contact.html')