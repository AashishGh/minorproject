from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import UserCreateForm
from django.shortcuts import render
from django.contrib.auth import get_user_model

class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy("accounts:login")
    template_name = "signup.html"
'''

class Profile(TemplateView):
    template_name = 'profile.html'
'''
def profile(request):
    return render (request,'profile.html',{'uid':request.user.id})
class MorangView(TemplateView):
    template_name = 'morang.html'

class MorangDetailView(TemplateView):
    template_name = 'morang1details.html'
'''
class UserInfo:
    def __init__(self,request):
        return request.user.id
'''
def contact(request):
    test = get_user_model()
    userInfo = test.objects.all().filter(is_superuser=False)
    print(userInfo)
    return render(request,'contact.html',{'userinfo':userInfo})

    

    
