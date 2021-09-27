from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from users.models import User
from .models import (
    Report,
    Service,
    Room,
    Asset,
    WorkFlow,
    Driver,
    Visitor,
    Supplier,
    Buyer,
    Season,
    Drop,
    Product,
    Order,
    Delivery
)
from .forms import (
    ReportForm,
    ServiceForm,
    RoomForm,
    AssetForm,
    WorkFlowForm,
    VisitorForm,
    DriverForm,
    SupplierForm,
    BuyerForm,
    SeasonForm,
    DropForm,
    ProductForm,
    OrderForm,
    DeliveryForm
)


# Driver views
@login_required(login_url='login')
def create_driver(request):
    forms = DriverForm()
    if request.method == 'POST':
        forms = DriverForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('driver-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_driver.html', context)


class DriverListView(ListView):
    model = Driver
    template_name = 'store/driver_list.html'
    context_object_name = 'driver'


# Visitor views
@login_required(login_url='login')
def create_visitor(request):
    forms = VisitorForm()
    if request.method == 'POST':
        forms = VisitorForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('visitor-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_visitor.html', context)


class VisitorListView(ListView):
    model = Visitor
    template_name = 'store/visitor_list.html'
    context_object_name = 'visitor'


# WorkFlow views
@login_required(login_url='login')
def create_workflow(request):
    forms = WorkFlowForm()
    if request.method == 'POST':
        forms = WorkFlowForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('workflow-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_workflow.html', context)


class WorkFlowListView(ListView):
    model = WorkFlow
    template_name = 'store/workflow_list.html'
    context_object_name = 'workflow'


# Asset views
@login_required(login_url='login')
def create_asset(request):
    forms = AssetForm()
    if request.method == 'POST':
        forms = AssetForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('asset-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_asset.html', context)


class AssetListView(ListView):
    model = Asset
    template_name = 'store/asset_list.html'
    context_object_name = 'asset'


# Supplier views
@login_required(login_url='login')
def create_supplier(request):
    forms = SupplierForm()
    if request.method == 'POST':
        forms = SupplierForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('supplier-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_supplier.html', context)


class SupplierListView(ListView):
    model = Supplier
    template_name = 'store/supplier_list.html'
    context_object_name = 'supplier'


# Buyer views
@login_required(login_url='login')
def create_buyer(request):
    forms = BuyerForm()
    if request.method == 'POST':
        forms = BuyerForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            address = forms.cleaned_data['address']
            email = forms.cleaned_data['email']
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            retype_password = forms.cleaned_data['retype_password']
            if password == retype_password:
                user = User.objects.create_user(
                    username=username, password=password,
                    email=email, is_buyer=True
                )
                Buyer.objects.create(user=user, name=name, address=address)
                return redirect('buyer-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_buyer.html', context)


class BuyerListView(ListView):
    model = Buyer
    template_name = 'store/buyer_list.html'
    context_object_name = 'buyer'


# Season views
@login_required(login_url='login')
def create_season(request):
    forms = SeasonForm()
    if request.method == 'POST':
        forms = SeasonForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('season-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_season.html', context)


class SeasonListView(ListView):
    model = Season
    template_name = 'store/season_list.html'
    context_object_name = 'season'


# Drop views
@login_required(login_url='login')
def create_drop(request):
    forms = DropForm()
    if request.method == 'POST':
        forms = DropForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('drop-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_drop.html', context)


class DropListView(ListView):
    model = Drop
    template_name = 'store/drop_list.html'
    context_object_name = 'drop'


# Product views
@login_required(login_url='login')
def create_product(request):
    forms = ProductForm()
    if request.method == 'POST':
        forms = ProductForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('product-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_product.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'product'


# Order views
@login_required(login_url='login')
def create_order(request):
    forms = OrderForm()
    if request.method == 'POST':
        forms = OrderForm(request.POST)
        if forms.is_valid():
            supplier = forms.cleaned_data['supplier']
            product = forms.cleaned_data['product']
            design = forms.cleaned_data['design']
            color = forms.cleaned_data['color']
            buyer = forms.cleaned_data['buyer']
            season = forms.cleaned_data['season']
            drop = forms.cleaned_data['drop']
            Order.objects.create(
                supplier=supplier,
                product=product,
                design=design,
                color=color,
                buyer=buyer,
                season=season,
                drop=drop,
                status='pending'
            )
            return redirect('order-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_order.html', context)


class OrderListView(ListView):
    model = Order
    template_name = 'store/order_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = Order.objects.all().order_by('-id')
        return context


# Delivery views
@login_required(login_url='login')
def create_delivery(request):
    forms = DeliveryForm()
    if request.method == 'POST':
        forms = DeliveryForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('delivery-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_delivery.html', context)


class DeliveryListView(ListView):
    model = Delivery
    template_name = 'store/delivery_list.html'
    context_object_name = 'delivery'


# Room views
@login_required(login_url='login')
def create_room(request):
    forms = RoomForm()
    if request.method == 'POST':
        forms = RoomForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('room-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_room.html', context)


class RoomListView(ListView):
    model = Room
    template_name = 'store/room_list.html'
    context_object_name = 'room'


# Service views
@login_required(login_url='login')
def create_outservice(request):
    forms = ServiceForm()
    if request.method == 'POST':
        forms = ServiceForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('outservice-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_outservice.html', context)


class ServiceListView(ListView):
    model = Service
    template_name = 'store/outservice_list.html'
    context_object_name = 'service'

 # Report views
@login_required(login_url='login')
def create_report(request):
    forms = ReportForm()
    if request.method == 'POST':
        forms = ReportForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('report-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_report.html', context)


class ReportListView(ListView):
    model = Report
    template_name = 'store/report_list.html'
    context_object_name = 'report'
