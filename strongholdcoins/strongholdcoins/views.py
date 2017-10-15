import account.views
from account.decorators import login_required
from .forms import SignupForm, OrderForm, ProfileForm
from .models import UserProfile, Order, Rate
from django.core.mail import send_mail, mail_admins

from django.http import JsonResponse

from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from django.utils.crypto import get_random_string
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.core.urlresolvers import reverse
from django.utils import timezone
from django import template
from PIL import Image

# from coinbase.wallet.client import Client


LOGIN_URL = '/account/login/'
DOLLAR_RATE = 4.47


class SignupView(account.views.SignupView):
    form_class = SignupForm

    identifier_field = 'email'

    def generate_username(self, form):
        # do something to generate a unique username (required by the
        # Django User model, unfortunately)
        username = get_random_string(6, 'abcdefghijklmnopqrstuvwxyz0123456789')
        return username

    def update_profile(self, form):
        UserProfile.objects.create(
            user=self.created_user,

        )

    def after_signup(self, form):
        self.update_profile(form)
        super(SignupView, self).after_signup(form)


class LoginView(account.views.LoginView):
    form_class = account.forms.LoginEmailForm


# Dashboard
@login_required(login_url=LOGIN_URL)
def dashboard(request):
    if request.user.is_authenticated:
        user_account = get_object_or_404(User, pk=request.user.id)
        userprofile = UserProfile.objects.get(id=request.user.profile.id)
        btc = Rate.objects.get(action__startswith="B")
        # btc_current_amount = btc.dollar_per_btc
        # total_fee = float(btc.dollar_per_btc * ((100 + (btc.tax_fee + btc.transaction_fee)) / 100))
        transaction_fee = (((btc.tax_fee + btc.transaction_fee)) / 100)
        gh_transaction_fee = (float(transaction_fee) * float(DOLLAR_RATE))
        timenow = timezone.now()
        new_order = Order.objects.filter(user__id=request.user.id, order_status__exact="AW").order_by("-created_on")[:1]
        history_data = Order.objects.filter(user__id=request.user.id, created_on__lte=timezone.now()).order_by(
            "created_on")
        saving_order = OrderForm()

        if request.method == "POST":
            saving_order = OrderForm(request.POST)
            if saving_order.is_valid():
                saving_order = saving_order.save(commit=False)
                saving_order.order_id = "SHC" + get_random_string(7, '0123456789')
                saving_order.order_amount = float(saving_order.order_amount) - float(gh_transaction_fee)
                saving_order.user = request.user

                if saving_order.payment_method == "AMM":
                    saving_order.bank = "N/A"
                    saving_order.bank_account_name = "N/A"
                    saving_order.bank_account_number = "N/A"
                elif saving_order.payment_method == "BAT":
                    saving_order.mobile_money_vendor = "N/A"
                    saving_order.mobile_money_number = "N/A"
                else:
                    saving_order.bank = "N/A"
                    saving_order.bank_account_name = "N/A"
                    saving_order.bank_account_number = "N/A"

                saving_order.save()

                messages.add_message(request, messages.SUCCESS,
                                     "Your order with REFERENCE ID {} was added successfully!".format(
                                         saving_order.order_id))

                mail_admins(
                    'STRONGHOLDCOINS: ORDER REQUESTED',
                    '{} has placed an order with ID: {}, please check at '
                    'https://strongholdcoins.com/admin/strongholdcoins/order/ check to review'.format(
                        request.user.username, saving_order.order_id),
                    fail_silently=False
                )

                order = OrderForm()
                return HttpResponseRedirect('/dashboard', {'form': order})
            else:
                messages.error(request, 'There was an error, try again later: {}'.format(saving_order.errors))

    return render(request, "strongholdcoins/dashboard_views/dashboard.html",
                  {'user_account': user_account, 'timenow': timenow, 'form': saving_order, 'new_order': new_order,
                   'history': history_data, 'userprofile': userprofile, 'btcrate': btc,
                   'transaction_fee': transaction_fee})


# Dashboard Edit
def editOrder(request, user_pk, order_pk):
    if request.user.is_authenticated:
        new_order = Order.objects.filter(user__id=request.user.id, order_status__exact="AW").order_by("-created_on")[:1]
        history_data = Order.objects.filter(user__id=request.user.id, created_on__lte=timezone.now()).order_by("created_on")
        userprofile = UserProfile.objects.filter(user__id=request.user.id)
        btc = Rate.objects.get(action__startswith="B")
        transaction_fee = ((100 + (btc.tax_fee + btc.transaction_fee)) / 100)
        order_to_edit = get_object_or_404(Order, pk=order_pk)
        orderform = OrderForm(instance=order_to_edit)

        pth = "/dashboard/user/{}/order/{}/edit".format(user_pk, order_to_edit.id)

        if request.method == "POST":
            orderform = OrderForm(request.POST, instance=order_to_edit)
            if orderform.is_valid():
                orderform.save()

                messages.add_message(request, messages.SUCCESS,
                                     "Your order with REFERENCE ID {} was updated successfully!".format(order_to_edit.order_id))
                mail_admins(
                    'STRONGHOLDCOINS: ORDER EDITED',
                    '{} edited an order with ID: {}, please check at '
                    'https://strongholdcoins.com/admin/strongholdcoins/order/ check to review'.format(
                        request.user.username, order_to_edit.order_id),fail_silently=False)
            else:
                messages.error(request, 'There was an error, try again later')

    return render(request, 'strongholdcoins/dashboard_views/dashboard.html',
                  {'form': orderform, 'new_order': new_order, 'history': history_data, 'pth': pth,
                   'userprofile': userprofile, 'order_to_edit': order_to_edit, 'btcrate': btc,
                   'transaction_fee': transaction_fee})



def deleteOrder(request, order_pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            order_to_delete = get_object_or_404(Order, pk=order_pk).delete()
            messages.add_message(request, messages.SUCCESS,"Your order with was deleted successfully!")
        return HttpResponseRedirect(reverse('dashboard'))


def profile_view(request):
    if request.user.is_authenticated:
            user_id = request.user.id
            userprofile = get_object_or_404(UserProfile,id=request.user.profile.id)
            profile_form = ProfileForm(instance=userprofile)
            if request.method == "POST":
                profile_form = ProfileForm(data=request.POST, files=request.FILES, instance=userprofile)
                if profile_form.is_valid:
                    profile_form.save()
                    return HttpResponseRedirect('/dashboard/user/profile', {'profile_form': profile_form, 'userprofile': userprofile})
            return render(request, "strongholdcoins/dashboard_views/profile.html",{'profile_form': profile_form, 'userprofile': userprofile})
    else:
        return HttpResponseNotFound('<h1>Bad Bot! Page not found</h1>')

# def account_view(request, user_pk):
#     userprofile = UserProfile.objects.filter(user__id=request.user.id)
#     user_id = request.user.id
#     if user_id == int(user_pk):
#         user_account = get_object_or_404(User, pk=user_pk)
#         account_form = UserAccountForm(instance=user_account)
#         if request.method == "POST":
#             account_form = UserAccountForm(request.POST, instance=user_account)
#             if account_form.is_valid:
#                 account_form.save()
#         return render(request, "strongholdcoins/dashboard_views/account.html",
#                       {'account_form': account_form, 'user_account': user_account, 'user_profile': user_profile})
#     else:
#         return HttpResponseNotFound('<h1>Bad Bot! Page not found</h1>')
