from django.contrib import admin
from .models import UserProfile,Order,Event,Rate


from django.core.mail import send_mail

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Order", {"fields": ['order_id', 'wallet_address', 'order_amount', 'action', 'payment_method', 'bank',
                              'bank_account_name', 'bank_account_number', 'mobile_money_vendor', 'mobile_money_number',
                              'user', 'order_status']},)
    ]

    readonly_fields = ("order_id",)
    list_display = (
        'order_id', 'wallet_address', 'order_amount', 'action', 'payment_method', 'bank', 'bank_account_name',
        'bank_account_number', 'mobile_money_vendor', 'mobile_money_number', 'order_status')
    list_display_links = ("order_id", "wallet_address")
    search_fields = ("order_id", "mobile_money_number", "bank_account_number",)

    def approve_orders(modeladmin, request, queryset):
        for order in queryset:
            order.order_status = "AP"
            order.save()
            send_mail(
                'STRONGHOLDCOINS: ORDER APPROVAL',
                'Hi {} your order <strong>{}</strong> has been approved! Please check your wallet address {}'.format(order.user.username,order.order_id,order.wallet_address),
                'order@strongholdcoins.com',
                [order.user.email],
                fail_silently=False
            )




    actions = (approve_orders,)


class UserProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Profile", {"fields": ['profile_picture','birth_date', 'address', 'bio']}),

    ]
    list_display = ('first_name','surname','birth_date','address',)


admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Rate)
admin.site.register(Event)