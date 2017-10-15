from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

import account.views
from django.contrib import admin
from .views import SignupView
from . import views


urlpatterns = [

    url(r'^dashboard/user/(?P<user_pk>\d+)/order/(?P<order_pk>\d+)/edit',views.editOrder,name="editOrder"),
    url(r'^dashboard/order/(?P<order_pk>\d+)/delete',views.deleteOrder,name="deleteOrder"),
    url(r'^dashboard/user/profile/$',views.profile_view,name="userprofile"),
    # url(r'^dashboard/user/account/(?P<user_pk>\d+)',views.account_view,name="useraccount"),
    url(r'^dashboard/$',views.dashboard,name="dashboard"),

    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),


    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/signup/$",SignupView.as_view(),name="account_signup"),
    url(r"^account/", include("account.urls")),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
