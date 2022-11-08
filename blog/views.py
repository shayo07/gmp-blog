from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'index.html')


def log_user(request):
    if request.method== 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin')
        else:
            messages.info(request, 'incorrect username or password')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('index')


def firmwares(request, pk_test):
    try:
        obj = Device.objects.get(name=pk_test)
        obj1 = obj.firmwares_set.all()
        obj2 = obj.firm_comment_set.all()
        if request.method== 'POST':
            form = CommentForm(request.POST, instance=obj2)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
         form=CommentForm()
        all=Device.objects.all()
        context= {'obj1':obj1, 'obj':obj, 'obj2':obj2, 'form':form, 'all':all}        
    except:        
        return render(request, 'firmwares.html')
    return render(request, 'firmwares.html', context)

def view_andr(request):
    try:
        all= Device.objects.all()
        obj1=Frp_bypass.objects.all()
        if request.method== 'POST':
            form = CommentFrForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form=CommentFrForm()
        comments=Frp_Comment.objects.all()
        context={'all':all, 'obj1':obj1, 'form':form, 'comments':comments}  
    except:
        return render(request, 'frp_bypass.html')
    return render(request, 'frp_bypass.html', context)


def cracked_tools(request, pk_test):
    try:
        obj = Device.objects.get(name=pk_test)
        obj1 = obj.cracked_tools_set.all()
        obj2 = obj.crack_comment_set.all()
        if request.method== 'POST':
            form = CommentCrForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
         form=CommentCrForm()
        all=Device.objects.all()
        context= {'obj1':obj1, 'obj':obj, 'obj2':obj2, 'form':form, 'all':all}        
    except:
        return render(request, 'cracked_tools.html')
    return render(request, 'cracked_tools.html', context)


def video_torent(request, pk_test):
    try:
        o = VideoTorent.objects.get(category=pk_test)
        obj = VideoTorent.objects.filter(category=pk_test)
        print(obj)
        obj2 = Torent_Comment.objects.all()
        if request.method== 'POST':
            form = CommentTrForm(request.POST)
            if form.is_valid():
                form.save()  
                return redirect('index')
        else: 
            form=CommentTrForm()
        all=VideoTorent.objects.all() 
        context= { 'obj':obj, 'obj2':obj2, 'form':form, 'all':all, 'o':o} 
    except:
        print('here')
        return render(request, 'video_torrents.html')
    return render(request, 'video_torrents.html', context)

@login_required(login_url='login')
def admin_view(request):
    obj=Device.objects.all()
    obj1 =Frp_bypass.objects.all()
    obj2=Firmwares.objects.all()
    obj3=Cracked_tools.objects.all()
    obj4=VideoTorent.objects.all()
    context={'obj':obj, 'obj1':obj1, 'obj2':obj2, 'obj3':obj3, 'obj4':obj4 }
    return render(request, 'admin.html', context)


@login_required(login_url='login')
def add_device(request):
    if request.method== 'POST':
        form = DeviceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
      form=DeviceForm()
    context={'form':form}
    return render(request, 'add_device.html', context)

@login_required(login_url='login')
def edit_device(request, pk_test):
    obj =Device.objects.get(name=pk_test)
    if request.method== 'POST':
        form = DeviceForm(request.POST, request.FILES, instance=obj )
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
      form=DeviceForm(instance=obj)
    context={'form':form}
    return render(request, 'add_device.html', context)


@login_required(login_url='login')
def remove_device(request, pk_test):
    obj=Device.objects.get(name=pk_test)
    obj.delete()
    return redirect('admin')



@login_required(login_url='login')
def add_frp(request):
    if request.method== 'POST':
        form = FrpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
      form=FrpForm()
    context={'form':form}
    return render(request, 'add_frp.html', context)

@login_required(login_url='login')
def edit_frp(request, pk_test):
    obj =Frp_bypass.objects.get(id=pk_test)
    if request.method== 'POST':
        form = FrpForm(request.POST, request.FILES, instance=obj )
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
      form=FrpForm(instance=obj)
    context={'form':form}
    return render(request, 'add_frp.html', context)

@login_required(login_url='login')
def remove_frp(request, pk_test):
    obj=Frp_bypass.objects.get(id=pk_test)
    obj.delete()
    return redirect('admin')




@login_required(login_url='login')
def add_firm(request):
    if request.method== 'POST':
        form = FirmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
      form=FirmForm()
    context={'form':form}
    return render(request, 'add_firm.html', context)

@login_required(login_url='login')
def edit_firm(request, pk_test):
    obj =Firmwares.objects.get(id=pk_test)
    if request.method== 'POST':
        form = FirmForm(request.POST, request.FILES, instance=obj )
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
      form=FirmForm(instance=obj)
    context={'form':form}
    return render(request, 'add_frp.html', context)

@login_required(login_url='login')
def remove_firm(request, pk_test):
    obj=Firmwares.objects.get(id=pk_test)
    obj.delete()
    return redirect('admin')



@login_required(login_url='login')
def add_crack(request):
    if request.method== 'POST':
        form = CrackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
      form=CrackForm()
    context={'form':form}
    return render(request, 'crack.html', context)

@login_required(login_url='login')
def edit_crack(request, pk_test):
    obj =Cracked_tools.objects.get(id=pk_test)
    if request.method== 'POST':
        form = CrackForm(request.POST, request.FILES, instance=obj )
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
      form=CrackForm(instance=obj)
    context={'form':form}
    return render(request, 'add_frp.html', context)


@login_required(login_url='login')
def remove_crack(request, pk_test):
    obj=Cracked_tools.objects.get(id=pk_test)
    obj.delete()
    return redirect('admin')



@login_required(login_url='login')
def add_torrent(request):
    if request.method== 'POST':
        form = TForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
      form=TForm()
    context={'form':form}
    return render(request, 'add_torrent.html', context)

@login_required(login_url='login')
def edit_torrent(request, pk_test):
    obj =VideoTorent.objects.get(video_name=pk_test)
    if request.method== 'POST':
        form = TForm(request.POST, request.FILES, instance=obj )
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
      form=TForm(instance=obj)
    context={'form':form}
    return render(request, 'add_torrent.html', context)

@login_required(login_url='login')
def remove_torrent(request, pk_test):
    obj=VideoTorent.objects.get(video_name=pk_test)
    obj.delete()
    return redirect('admin')


