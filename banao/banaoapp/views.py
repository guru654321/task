from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User, Doctor, Patient

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        profile_picture = request.FILES.get('profile_picture')
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        address_line1 = request.POST['address_line1']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']
        user_type = request.POST['user_type']

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already taken")
            return redirect('signup')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.profile_picture = profile_picture
        user.address_line1 = address_line1
        user.city = city
        user.state = state
        user.pincode = pincode
        user.user_type = user_type
        user.save()

        if user_type == '1':  # Doctor
            Doctor.objects.create(user=user)
        elif user_type == '2':  # Patient
            Patient.objects.create(user=user)

        return redirect('login')

    return render(request, 'banaoapp/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.user_type == '1':  # Doctor
                return redirect('doctor_dashboard')
            elif user.user_type == '2':  # Patient
                return redirect('patient_dashboard')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'banaoapp/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def doctor_dashboard(request):
    if not request.user.is_authenticated or request.user.user_type != '1':
        return redirect('login')
    return render(request, 'banaoapp/doctor_dashboard.html')

def patient_dashboard(request):
    if not request.user.is_authenticated or request.user.user_type != '2':
        return redirect('login')
    return render(request, 'banaoapp/patient_dashboard.html')

def home(request):
    return render(request, 'banaoapp/home.html')
