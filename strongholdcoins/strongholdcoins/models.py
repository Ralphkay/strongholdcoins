from django.db import models
from django.conf import settings


from django.db import models
from django.conf import settings

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.utils.crypto import get_random_string
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver



class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')
    first_name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(blank=True,null=True)
    profile_picture = models.ImageField(upload_to="profile_pictures/", blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    address = models.TextField(max_length=255, blank=True, null=True)
    identity_card = models.FileField(upload_to="identity_folder/", blank=True, null=True)
    phone = models.CharField(max_length=10, null=True,blank=True)

    def __str__(self):
        return self.user.username


    def _full_name(self):
        return self.first_name+" "+self.surname

    full_name = property(_full_name)


class Order(models.Model):

    BUY = 'B'
    SELL = 'S'
    INVEST = 'S'
    action = (
        ("B", "Buy"),
        ("S", "Sell"),
        ("I", "Invest"),
    )
    # PENDING = "P"
    AWAITING = "AW"
    APPROVED = "AP"
    WITHHELD = "W"
    status = (
        (AWAITING,"Awaiting Payment"),
        (APPROVED, "Approved"),
        (WITHHELD, "With Held"),
      
    )

    B = "Bitcoin"
    E = "Ethereum"
    L = "Litecoin"
    currencies = (
        (B, "Bitcoin"),
        (E, "Ethereum"),
        (L, "Litecoin"),
    )
    order_id = models.CharField(unique=True, max_length=10, blank=True, null=False,)
    wallet_address = models.CharField(blank=False, null=False, max_length=255)
    order_amount = models.DecimalField(decimal_places=2, max_digits=99999, blank=False, null=False)
    user = models.ForeignKey(User, related_name="user_order")

    order_status = models.CharField(choices=status, max_length=2, default=AWAITING, blank=False, null=False)
    crypto_currency = models.CharField(choices=currencies, default=B, blank=True, max_length=12)
    amount_of_coins = models.DecimalField(decimal_places=2, max_digits=99999, blank=False, null=False,default=0.00)
    commission_fee = models.DecimalField(decimal_places=2, max_digits=99999, blank=False, null=False,default=0.00)

    action = models.CharField(max_length=1, choices=action, default=BUY, blank=False)

    DEFAULT_PM = ''
    MOBILE_MONEY = "AMM"
    BANK_ACCOUNT_TRANSFER = "BAT"
    pm = (
        # (DEFAULT_PM,"Select Method"),
        (MOBILE_MONEY,"Mobile Money"),
        (BANK_ACCOUNT_TRANSFER,"Bank Account Transfer"),
    )
    
    MTN = "MTN"
    VODAFONE = "VODAFONE"
    AIRTEL = "AIRTEL"
    TIGO = "TIGO"
    mmv = (

        (MTN, "MTN"),
        (VODAFONE, "VODAFONE"),
        (AIRTEL, "AIRTEL"),
        (TIGO, "TIGO"),
    )

    payment_method = models.CharField(choices=pm, blank=False, null=False, max_length=4)

    
    GT = "GT Bank"
    ZB = "Zenith Bank"
    SB = "Stanbic Bank"
    EC = "EcoBank"
    UB = "UniBank"
    CB = "Cal Bank"

    banks = (
        (GT, "GT BANK"),
        (ZB, "ZENITH BANK"),
        (SB, "STANBIC BANK"),
        (EC, "ECOBANK"),
        (UB, "UNIBANK"),
        (CB, "CAL BANK"),
    )

    mobile_money_vendor = models.CharField(choices=mmv, blank=True, null=True, max_length=20)
    mobile_money_number = models.CharField(max_length=10, blank=True, null=True)

    bank = models.CharField(choices=banks, max_length=50, blank=True, null=True)
    bank_account_name = models.CharField(max_length=155, blank=True, null=True)
    bank_account_number = models.CharField(blank=True, null=True, max_length=16)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.order_id)
 


class Event(models.Model):
	name = models.CharField(max_length=200)


class Rate(models.Model):

    BUY = 'B'
    SELL = 'S'
    INVEST = 'S'
    action = (
        ("B", "Buy"),
        ("S", "Sell"),
        ("I", "Invest"),
    )

    B = "BITCOIN"
    E = "ETHIRIUM"
    L = "LITHIUM"
    currency = (
        (B, "BITCOIN"),
        (E, "ETHIRIUM"),
        (L, "LITHIUM"),
        )

    # dollar_per_btc = models.DecimalField(decimal_places=2,max_digits=99999,blank=False, null=True)
    # btc_amount = models.DecimalField(decimal_places=2,max_digits=99999,blank=False, null=True)
    tax_fee = models.DecimalField(decimal_places=2,max_digits=100,blank=False, null=True)
    transaction_fee = models.DecimalField(decimal_places=2,max_digits=100,blank=False, null=True)
    action = models.CharField(max_length=1,choices=action,default=BUY,blank=True)
    # cryptocurrency = models.CharField(choices=currency,default=B,blank=True,max_length=12)

    def __str__(self):
        return self.action
