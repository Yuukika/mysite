from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm, UserProfileForm,UserInfoForm,UserForm
from .models import UserInfo, UserProfile
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password = cd['password'])

            if user:
                login(request, user)
                return HttpResponseRedirect('/article/')
            else:
                return HttpResponse('Sorry. Your username or password is not right.')
        else:
            return HttpResponse('Invalid login')
    if request.method == 'GET':
        login_form = LoginForm()
        return render(request,'account/login.html',{'form':login_form})


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid()*userprofile_form.is_valid():
            new_user = user_form.save(commit = False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = userprofile_form.save(commit = False)
            new_profile.user = new_user
            new_profile.save()
            UserInfo.objects.create(user=new_user)
            #return HttpResponse('successfully!')
            return HttpResponseRedirect(reverse("account:user_login"))
        else:
            #return HttpResponse('sorry, you can not register')
            return HttpResponseRedirect(reverse("account:user_register"))
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request,'account/register.html', {'form': user_form, 'profile_form': userprofile_form})


@login_required(login_url = 'account/login')
def userinfo(request):
    user = User.objects.get(username = request.user.username)
    userprofile = UserProfile.objects.get(user = user)
    userinfo = UserInfo.objects.get(user=user)
    return render(request,'account/user_information.html',{'user':user, 'userinfo':userinfo,'userprofile':userprofile})

@login_required(login_url = 'account/login/')
def edit_info(request):
    user = User.objects.get(username=request.user.username)
    userprofile =  UserProfile.objects.get(user=user)
    userinfo = UserInfo.objects.get(user=user)

    if request.method == 'POST':
        userform = UserForm(request.POST)
        userprofileform = UserProfileForm(request.POST)
        userinfoform = UserInfoForm(request.POST)
        if userform.is_valid() * userprofileform.is_valid()*userinfoform.is_valid():
            user_cd = userform.cleaned_data
            userprofile_cd = userprofileform.cleaned_data
            userinfo_cd = userinfoform.cleaned_data
            print(user_cd)
            print(userprofile_cd)
            print(userinfo_cd)
            user.email = user_cd['email']
            userprofile.birth = userprofile_cd['birth']
            userprofile.phone = userprofile_cd['phone']
            userinfo.school = userinfo_cd['school']
            userinfo.company = userinfo_cd['company']
            userinfo.profession = userinfo_cd['profession']
            userinfo.address = userinfo_cd['address']
            userinfo.aboutme = userinfo_cd['aboutme']
            userprofile.save()
            user.save()
            userinfo.save()
        return HttpResponseRedirect('/account/my-information/')
    else:
        userform = UserForm(instance=user)
        userprofileform = UserProfileForm(initial={'birth':userprofile.birth,'phone':userprofile.phone})
        userinfoform = UserInfoForm(initial={'school':userinfo.school,'company':userinfo.company,'profession':userinfo.profession,'address':userinfo.address,'aboutme':userinfo.aboutme})
        return render(request, 'account/edit_info.html',{'userform':userform, 'userprofileform':userprofileform, 'userinfoform':userinfoform})
@login_required(login_url='/account/login/')
def my_image(request):
    if request.method == 'POST':
        img = request.POST['img']
        userinfo =UserInfo.objects.get(user=request.user.id)
        userinfo.photo = img
        userinfo.save()
        return HttpResponse("1")
    else:
        return render(request, 'account/imagecrop.html',)
