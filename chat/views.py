from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message

@login_required()
def room(request):
    messages = list(Message.objects.values().order_by('-timestamp')[:10])
    context = {
     'messages': messages
    }
    return render(request, 'chat/room.html', context)
	   