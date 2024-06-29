from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_protect

from ...forms import AccountForm, UserCreationForm
from ...models import Account
from ...permissions import IsAdmin


@method_decorator(csrf_protect, name="dispatch")
class CustomLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("login")


@method_decorator(csrf_protect, name="dispatch")
class Redirect(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if IsAdmin():
                return redirect("user_create")
            else:
                ...
        else:
            return redirect("login")


class UserCreateView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "admin/registration_form.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user_create")
        return render(request, "admin/registration_form.html", {"form": form})


class AccountListView(View):
    def get(self, request):
        accounts = Account.objects.all()
        return render(request, "admin/account_list.html", {"accounts": accounts})

    def post(self, request):
        account_id = request.POST.get("account_id")
        account = get_object_or_404(Account, id=account_id)
        account.active = not account.active
        account.save()
        return redirect("accounts_list")


class AccountCreateView(View):
    def get(self, request):
        form = AccountForm()
        return render(request, "admin/account_form.html", {"form": form})

    def post(self, request):
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts_list")
        return render(request, "admin/account_form.html", {"form": form})
