from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from forms import TrainingNeedsAssessmentForm # type: ignore

def index_view(request):
    return render(request, 'myApp/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'myApp/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect('dashboard')
    return render(request, 'myApp/register.html')

def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'myApp/dashboard.html')
# views.py

def training_needs_assessment(request):
    if request.method == 'POST':
        form = TrainingNeedsAssessmentForm(request.POST)
        if form.is_valid():
            feedback = form.cleaned_data['feedback']
            courses = form.cleaned_data['courses']
            # Process the form data (e.g., save to the database)
            return render(request, 'myApp/assessment_success.html', {'feedback': feedback, 'courses': courses})
    else:
        form = TrainingNeedsAssessmentForm()

    return render(request, 'myApp/training_needs_assessment.html', {'form': form})
