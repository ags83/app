# Create your views here.
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django import forms
from django.forms.models import model_to_dict
from django.template import RequestContext
from forms import CreateMessage, DeleteMessage
from django.db.models import Q
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from messages.models import Message

@login_required
def create(request, id=None):
    if request.method == 'POST':
        form = CreateMessage(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user_to = User.objects.get(username=cd['user_to'])
            mail = Message(head=cd['head'], body=cd['body'], user_to=user_to, user_from=request.user)
            mail.save()
            messages.success(request, 'Message Sent.')
            return HttpResponseRedirect('/messages/main/')
    else:
        if id is not None:
            try:
                mail = Message.objects.get(id=id)
            except Message.DoesNotExist:
                return render_to_response('messages/main.html', context_instance=RequestContext(request))
            form = CreateMessage(initial={'user_to':mail.user_from.username, 'head':'RE: '+ mail.head})
        else:	
            form = CreateMessage()
    return render_to_response('messages/add.html', {'form':form}, context_instance=RequestContext(request))
	
@login_required
def main(request):
    mail_list = Message.objects.filter(user_to=request.user)
    paginator = Paginator(mail_list, 50)
    page = request.GET.get('page')
    try:
        mails = paginator.page(page)
    except PageNotAnInteger:
        mails = paginator.page(1)
    except EmptyPage:
        mails = paginator.page(paginator.num_pages)
    return render_to_response('messages/main.html', {'mails':mails}, context_instance=RequestContext(request))

	
def view(request, mail_id):
    try:
        mail = Message.objects.get(id=mail_id)
    except Message.DoesNotExist:
		return render_to_response('errors/notexist.html')
    form = DeleteMessage(initial={'message_id':mail.id})
    
    return render_to_response('messages/view.html', {'mail':mail,'form':form}, context_instance=RequestContext(request))
	
def delete(request, mail_id):
    if request.method == 'POST':
        try:
            mail = Message.objects.get(id=mail_id)
        except Message.DoesNotExist:
            return render_to_response('errors/notexist.html')
        mail.delete()
        messages.success(request, 'Message Deleted.')
        return HttpResponseRedirect('/messages/main/')
    else:
        return render_to_response('errors/notexist.html', context_instance=RequestContext(request))
	
	
    
	