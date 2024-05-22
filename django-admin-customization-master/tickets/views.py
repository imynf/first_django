from django.shortcuts import render,redirect,get_object_or_404
from .models import Concert, Ticket
from .forms import TicketForm , ConcertForm
from django.core.paginator import Paginator

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TicketSerializer

# Create your views here.
def home(request):
    concerts = Concert.objects.all()
    
    return render(request, 'index.html',{'concerts': concerts})


def concert_list(request):
    # 获取所有演唱会对象
    all_concerts = Concert.objects.all()
    
    # 每页显示的演唱会数量
    concerts_per_page = 5
    
    # 创建 Paginator 对象
    paginator = Paginator(all_concerts, concerts_per_page)
    
    # 获取当前页码
    page_number = request.GET.get('page')
    
    # 获取当前页的演唱会对象
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'index.html', {'page_obj': page_obj})

#def purchase_ticket(request):
    #if request.method == 'POST':
        #venue_concert_name = request.POST.get('venue_concert_name')
        #[venue, concert_name] = venue_concert_name.split(':')
        #first_name = request.POST.get("first_name")
        #last_name = request.POST.get("last_name")
        #payment_method = request.POST.get("payment_method")
        #concert = get_object_or_404(Concert, venue=venue.strip(), name=concert_name.strip())
        #form = TicketForm(request.POST)
        #if form.is_valid():
            # 在保存票证时将 concert 对象传递给 form
         #   form.save(concert=concert)
          #  return redirect('ticket_purchase_success')
    #else:
    #    form = TicketForm()
    #return render(request, 'index.html', {'form': form})
#def purchase_ticket(request):
    if request.method == 'POST':
        venue_concert_name = request.POST.get('venue_concert_name')
        concert_name = venue_concert_name.split(':')[1].strip()  # 提取音乐会名称
        concert = get_object_or_404(Concert, name=concert_name)  # 使用音乐会名称获取音乐会对象
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        customer_full_name = request.POST.get('customer_full_name')
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.concert = concert  # 将获取到的音乐会对象赋值给票证的 concert 字段
            ticket.save()
            return render(request, 'ticket_purchase_success.html')
    else:
        form = TicketForm()
    return render(request, 'index.html', {'form': form})

def ticket_purchase_success(request):
    # 这里可以添加任何你想要显示的成功购票页面的逻辑或者内容
    return render(request, 'ticket_purchase_success.html')

def purchase_ticket(request):
    if request.method == 'POST':
        venue_concert_name = request.POST.get('venue_concert_name')
        concert_name = venue_concert_name.split(':')[1].strip()  # 提取音乐会名称
        concert = get_object_or_404(Concert, name=concert_name)  # 使用音乐会名称获取音乐会对象
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        
        # 将 first_name 和 last_name 组合成 customer_full_name
        customer_full_name = f"{first_name} {last_name}"
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.concert = concert  # 将获取到的音乐会对象赋值给票证的 concert 字段
            ticket.customer_full_name = customer_full_name  # 设置客户全名
            ticket.save()
            return render(request, 'ticket_purchase_success.html')
    else:
        form = TicketForm()
    return render(request, 'index.html', {'form': form})


