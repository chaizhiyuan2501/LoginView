from django.shortcuts import render,redirect
from django.views.generic.edit import (
    CreateView,FormView
    )
from django.views.generic.base import (
    TemplateView,View
    )
from .forms import RegistForm,UserLoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class RegistUserView(CreateView):
    template_name = "regist.html"
    form_class = RegistForm

# class UserLoginView(FormView):
#     template_name = "user_login.html"
#     form_class = UserLoginForm
    
#     def post(self, request, *args, **kwargs):
#         email = request.POST["email"]
#         password = request.POST["password"]
#         user = authenticate(email=email, password=password)
#         next_url = request.POST["next"]
#         if user is not None and user.is_active:
#             login(request,user)
#         if next_url:
#             return redirect(next_url)
#         return redirect("accounts:home")

# 再定義
class UserLoginView(LoginView):
    template_name = "user_login.html"
    authentication_form = UserLoginForm
    
    def form_valid(self, form):
        remember = form.cleaned_data["remember"]
        # ログイン状態保持するボタンをチェックされたら､2週間保持する
        if remember:
            self.request.session.set_expiry(1200000)
        return super().form_valid(form)

    
# class UserLogoutView(View):

#     def get(self, request, *args, **kwargs):
#         logout(request)
#         return redirect("accounts:user_login")

# 再定義
class UserLogoutView(LogoutView):
    pass


# @method_decorator(login_required,name = "dispatch")
class UserView(LoginRequiredMixin,TemplateView):
    template_name = "user.html"

    # @method_decorator(login_required)   #ログインした前提で実行
    #GETリクエストの際にGET処理､POSTの際にPOST処理
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

