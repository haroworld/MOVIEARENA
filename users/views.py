from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .forms import ChangePicsForm, ChangeSettingsForm, EditprofileForm, RegistrationForm
from . models import Profile
# Create your views here.



def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')
    

    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User does not exits')

        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is not correct')

    return render(request, 'users/login.html')


def registerPage(request):
    try:
        form = RegistrationForm(initial={'email':request.session['mail']})
    except:
        form = RegistrationForm()

    if request.user.is_authenticated:
        messages.error(request, 'You are already logged in')
        return redirect('home')

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        

        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 and password2 and password1 != password2:
            messages.error(request, 'Password does not match')
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            if 'mail' in request.session:
                del request.session['mail']
            
            user.save()
            Profile.objects.create(
                user = user,
                surname = user.last_name,
                firstname = user.first_name,
                email = user.email,
                username = user.username,
                profileType = 'Adult'
            )

            

            messages.success(request, 'Your account was created successfully')
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')
            

    context = {'form':form}
    return render(request, 'users/register.html',context)





@login_required(login_url='login')
def profilePage(request):
    user = request.user
    context = {'user':user}
    return render(request,'users/profile.html', context)


@login_required(login_url='login')
def editProfile(request):
    user = request.user
    profile = user.profile
    form = EditprofileForm(instance=user)

    if request.method == "POST":
        form=EditprofileForm(request.POST, request.FILES, instance = user)
        if form.is_valid:
            current_user = form.save(commit=False)
            profile.surname = current_user.last_name
            profile.firstname = current_user.first_name
            profile.username = current_user.username
            current_user.save()
            profile.save()
            return redirect('profile')

    context = {'form':form}
    return render(request, "users/edit_profile.html", context)


@login_required(login_url='login')
def changeEmail(request):
    user = request.user
    profile = user.profile

    if request.method == "POST":
        email = request.POST['email'].lower()
        profile.email = email
        user.email = email
        profile.save()
        user.save()
        return redirect('profile')

    return render(request, 'users/change_email.html')

@login_required(login_url='login')
def changeNum(request):
    user = request.user
    profile = user.profile

    if request.method == "POST":
        phone_number = request.POST['number']
        profile.phone_number = phone_number
        profile.save()
        return redirect('profile')

    return render(request, 'users/change_number.html')


@login_required(login_url='login')
def CheckPassword(request):
    user_id = request.user.id
    user = User.objects.get(id = user_id)
    username = request.user.username

    if request.method == "POST":
        password = request.POST['password']

        user = authenticate(request, username=username,password=password)
        if user is not None:
            return redirect('change_email')
        else:
            messages.error(request, 'Incorect password')

    return render(request, 'users/check_password.html')

@login_required(login_url='login')
def CheckPasswordForNum(request):
    user_id = request.user.id
    user = User.objects.get(id = user_id)
    username = request.user.username

    if request.method == "POST":
        password = request.POST['password']

        user = authenticate(request, username=username,password=password)
        if user is not None:
            return redirect('change_number')
        else:
            messages.error(request, 'Incorect password')

    return render(request, 'users/check_passwordnum.html')


@login_required(login_url='login')
def ChangeSettings(request):
    user = request.user
    profile = user.profile
    form = ChangeSettingsForm(instance = profile)

    if request.method == "POST":
        form = ChangeSettingsForm(request.POST, request.FILES ,instance = profile)
        if form.is_valid:
            form.save()
            return redirect('profile')
    context = {'form':form}
    return render(request, 'users/settings.html', context)


@login_required(login_url='login')
def DeleteAccount(request):
    user = request.user

    if request.method == "POST":
        logout(request)
        user.delete()
        return redirect('login')
    context = {'user':user}
    return render(request, 'users/delete_account.html', context)


@login_required(login_url='login')
def Logout(request):
    logout(request)
    return redirect('mainPage')

@login_required(login_url='login')
def changeProfilePic(request):
    user = request.user
    profile = user.profile
    form = ChangePicsForm(instance = profile)

    if request.method == "POST":
        form = ChangePicsForm(request.POST, request.FILES, instance = profile)
        if form.is_valid():
            form.save()
            return redirect('profile')


    context = {'form':form}
    return render(request, 'users/change_pics.html', context)