from django.shortcuts import render
from .models import Concert
from .forms import TicketForm , ConcertForm
# Create your views here.
def home(request):
    concerts = Concert.objects.all()
    
    return render(request, 'index.html',{'concerts': concerts})