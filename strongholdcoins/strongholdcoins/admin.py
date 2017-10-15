from django.contrib import admin
from .models import UserProfile,Order,Event,Rate
from django.http import  HttpResponse
import xlwt


from django.core.mail import send_mail

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Order", {"fields": ['order_id', 'wallet_address', 'order_amount', 'crypto_currency', 'amount_of_coins','commission_fee', 'action', 'payment_method', 'bank',
                              'bank_account_name', 'bank_account_number', 'mobile_money_vendor', 'mobile_money_number',
                              'user', 'order_status']},)
    ]

    readonly_fields = ("order_id",)
    list_display = (
        'order_id', 'wallet_address', 'order_amount','amount_of_coins','commission_fee', 'action','crypto_currency', 'payment_method', 'bank', 'bank_account_name',
        'bank_account_number', 'mobile_money_vendor', 'mobile_money_number', 'order_status')
    list_display_links = ("order_id", "wallet_address")
    search_fields = ("order_id", "mobile_money_number", "bank_account_number",)

    def approve_orders(modeladmin, request, queryset):
        for order in queryset:
            order.order_status = "AP"
            order.save()
            send_mail(
                'STRONGHOLDCOINS: ORDER APPROVAL',
                'Hi {}, your order with reference ID <strong>{}</strong> has been approved! Please check your wallet address {}. For more information please contact support@strongholdcoins.com.'.format(order.user.profile.first_name, order.order_id,order.wallet_address),
                'order@strongholdcoins.com',
                [order.user.email],
                fail_silently=False
            )


    def export_xls(modeladmin, request, queryset):

        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="orders.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Orders')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['order_id', 'wallet_address', 'order_amount', 'crypto_currency', 'amount_of_coins','commission_fee', 'action', 'payment_method', 'bank', 'bank_account_name', 'bank_account_number', 'mobile_money_vendor', 'mobile_money_number', 'user', 'order_status', ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        rows = Order.objects.all().values_list('order_id', 'wallet_address', 'order_amount', 'crypto_currency', 'amount_of_coins','commission_fee', 'action', 'payment_method', 'bank', 'bank_account_name', 'bank_account_number', 'mobile_money_vendor', 'mobile_money_number','user', 'order_status')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)
        return response




    actions = (approve_orders,export_xls,)


class UserProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Profile", {"fields": ['profile_picture','birth_date', 'address', 'bio']}),

    ]
    list_display = ('first_name','surname','birth_date','address',)


admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Rate)
admin.site.register(Event)