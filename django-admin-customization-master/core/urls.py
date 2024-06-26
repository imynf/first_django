"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tickets import views



admin.site.site_title = "TicketsPlus site admin"
admin.site.site_header = "TicketsPlus administration"
admin.site.index_title = "Site administration"
# https://github.com/django/django/blob/main/django/contrib/admin/sites.py

urlpatterns = [
    path("home/",views.home, name='home'),
    path("secretadmin/", admin.site.urls),
    path('purchase-ticket/', views.purchase_ticket, name='purchase_ticket'),
    path('purchase-success/', views.ticket_purchase_success, name='ticket_purchase_success'),
]
