from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import Message

def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "chat/chatPage.html", context)

def chat_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            # Broadcast the message to WebSocket clients
            # (this part depends on your WebSocket implementation)
            return redirect('chat')
    else:
        form = MessageForm()

    messages = Message.objects.all().order_by('timestamp')
    return render(request, 'chat/chatPage.html', {'form': form, 'messages': messages})