from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from .forms import BlogForm
from django.views.generic import DetailView
from .models import CustomUser, BlogCategory, Blog

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request):
    #return HttpResponse("<h1> hello world </h1>")
    if request.user.status == 'patient':
        all_blogs = {}
        for category in BlogCategory.objects.all():
            blogs = Blog.objects.filter(category = category, is_draft=False)
            if blogs:
                all_blogs[category] = blogs
        print(all_blogs)        
        return render(request, 'dashboard.html', {'blogs' : all_blogs})
    return render(request, 'dashboard.html')
def user_logout(request):
    logout(request)
    return redirect('login')


def is_doctor(user):
    return user.is_authenticated and user.status == 'doctor'

@login_required
@user_passes_test(is_doctor)
def create_blog(request):
    if not is_doctor(request.user):
        return HttpResponseForbidden("Forbidden: You do not have permission to access this page.")

    if request.method == 'POST':
        form = BlogForm(request.POST )
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('dashboard')
    else:
        form = BlogForm()

    return render(request, 'create_blog.html', {'form': form})



class BlogDetail(DetailView):
    model = Blog
    template_name = 'blog_detail.html'  # Define your template path
    context_object_name = 'blog'  # Define the variable name in the template