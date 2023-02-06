from django.shortcuts import render
from .models import Order
from .forms import OrderForms

# Create your views here.
#Выводит весь query set
def first_page(request):
    object_list = Order.objects.all()
    form = OrderForms()
    return render(request,'./index.html', {'object_list':object_list,
                                           'form':form})

#Отправка формы и заносит её в БД
def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    element = Order(order_name = name,order_phone = phone)
    element.save()
    return render(request,'./thanks_page.html',{'name':name,
                                                'phone': phone})
