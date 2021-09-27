from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from store.models import Driver,Product, Supplier, Buyer, Order,WorkFlow,Visitor,Room


@login_required(login_url='login')
def dashboard(request):
    total_room = Room.objects.count(),
    total_workflow = WorkFlow.objects.count()
    total_visitor = Visitor.objects.count()
    total_driver = Driver.objects.count()
    total_product = Product.objects.count()
    total_supplier = Supplier.objects.count()
    total_buyer = Buyer.objects.count()
    total_oder = Order.objects.count()
    orders = Order.objects.all().order_by('-id')
    workflow = WorkFlow.objects.all().order_by('-id')
    context = {
        'visitor': total_visitor,
        'workflowID': total_workflow,
        'driver':total_driver,
        'product': total_product,
        'supplier': total_supplier,
        'buyer': total_buyer,
        'order': total_oder,
        'orders': orders,
        'workflow': workflow,
    }
    return render(request, 'dashboard.html', context)
