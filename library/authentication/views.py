# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.base import TemplateView
from django.template import loader
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.db.utils import IntegrityError
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from order.models import Order
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.password_validation import validate_password


class HomePageView(TemplateView):
    template_name = "authentication/index.html"


class RegisterPage(TemplateView):
    template_name = "authentication/register.html"


class LoginPage(TemplateView):
    # template_name = "authentication/login.html"
    # form_class = LoginForm
    def get(self, request):
        context = {'form': LoginForm()}
        return render(request, "authentication/login.html", context)
    

def user_page(request):

    if request.user and request.user.is_authenticated:
        return redirect('authentication:index')
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                return render(request, template_name="authentication/index.html")
            else:
                form.add_error(None, 'Incorrect Login or Password')
    else:
        form = LoginForm()

    return render(request, 'authentication/login.html', {'form':form})
# def user_page(request):
#     if request.user.is_authenticated:
#         # template = loader.get_template("authentication/user_page.html")
#         # return HttpResponse(template.render())
#         return render(request, template_name="authentication/index.html")
#     else:
#         email = request.POST["email"]
#         password = request.POST["pass"]
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             login(request, user)
#             # template = loader.get_template("authentication/user_page.html")
#             # return HttpResponse(template.render())
#             return render(request, template_name="authentication/index.html")

#         else:
#             return HttpResponse("Error")

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("authentication:login")
    else:
        form = RegistrationForm()

    return render(request, "authentication/register.html", {'form':form})
# def registration(request):
#     if request.method == "POST":
#         email = request.POST["email"]
#         password = request.POST["pass"]
#         role = request.POST["role"]

#         # Checking email and password for validation
#         try:
#             validate_email(email)
#         except ValidationError as error_message:
#             return render(
#                 request,
#                 template_name="authentication/register.html",
#                 context={"error_message": error_message},)

#         # Checking password for validation
#         try:
#             validate_password(password)
#         except ValidationError as error_message:
#             return render(
#                 request,
#                 template_name="authentication/register.html",
#                 context={"error_message": error_message},)

#         # if email and password valid then trying to create the new User
#         try:
#             if role == "0":
#                 user = CustomUser.objects.create_user(email=email, password=password, role=role)
#                 user.save()
#             elif role == "1":
#                 user = CustomUser.objects.create_superuser(
#                     email=email, password=password, role=role
#                 )
#                 user.save()
#         # if email not unique then return 'error_message': 'USER IS ALREADY EXIST'
#         except IntegrityError:
#             return render(
#                 request,
#                 template_name="authentication/register.html",
#                 context={
#                     "error_message": "User with that email is already exist, please Log In"
#                 },
#             )

#         # if everything is good then redirect to login page
#         return redirect("authentication:login")

#     # if request.method != 'POST', just render template
#     else:
#         return render(request, template_name="authentication/register.html")



def out(request):
    logout(request)
    return redirect('authentication:login')


def users_page(request):
    users = CustomUser.objects.order_by("id")
    return render(request, "authentication/all_users.html", {"users": users})


def user_details(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    orders = Order.objects.filter(user_id=user_id)
    return render(request, "authentication/user_details.html", {"user": user, "orders": orders})