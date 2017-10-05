from django import forms
from django.forms.extras.widgets import SelectDateWidget

import account.forms

from django import forms
from django.utils.crypto import get_random_string
from django.forms import ModelForm, CharField, RadioSelect,Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Order,UserProfile
from PIL import Image

from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class SignupForm(account.forms.SignupForm):
    first_name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    birth_date = forms.DateField(widget=SelectDateWidget(years=range(1910,1991)))

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        del self.fields["username"]


class ProfileForm(ModelForm):
    # Add to a form containing a FileField and change the field names accordingly.



  class Meta:
    model = UserProfile
    fields = ('profile_picture','first_name','surname','birth_date','phone','address','identity_card')

    def clean_content(self):
        content = self.cleaned_data['content']
        content_type = content.content_type.split('/')[0]
        if content_type in settings.CONTENT_TYPES:
            if content._size > settings.MAX_UPLOAD_SIZE:
                raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (
                filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(content._size)))
        else:
            raise forms.ValidationError(_('File type is not supported'))
        return content


class OrderForm(ModelForm):
    wallet_address = CharField(required=True)
    order_amount = CharField(required=True)
    # order_id = CharField(max_length=10, initial=get_random_string(10,'0123456789'))

    DEFAULT_PM=""
    MOBILE_MONEY = "AMM"
    BANK_ACCOUNT_TRANSFER = "BAT"
    DEFAULT="Choose"

    pm = (
        (DEFAULT_PM, "Select Vendor"),
        (MOBILE_MONEY, "Mobile Money"),
        (BANK_ACCOUNT_TRANSFER, "Bank Account Transfer"),
    )
    payment_method = forms.CharField(
        max_length=3,
        widget = forms.Select(choices=(pm)),
        required=True
     )
    
    GT = "GT"
    ZB = "ZB"
    SB = "SB"
    EC = "EB"
    UB = "UB"
    CB = "CB"
    banks = (
      ("","Select Bank"),
      (GT,"GT BANK"),
      (ZB,"ZENITH BANK"),
      (SB,"STANBIC BANK"),
      (EC,"ECOBANK"),
      (UB,"UNIBANK"),
      (CB,"CAL BANK"),
    )
    bank = forms.CharField(

      max_length = 2,
      widget = forms.Select(choices=(banks)),
      required=False 

      )

    class Meta:
        model = Order
        fields = ('order_id','wallet_address','order_amount','action','payment_method','bank','bank_account_name','bank_account_number','mobile_money_vendor','mobile_money_number')



