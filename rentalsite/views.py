from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django import forms
from django.template import RequestContext
from forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.context_processors import csrf


	
def main_page(request):

    return render_to_response('index.html', context_instance=RequestContext(request))

	
def checkAvailable(request):
    username = request.GET.get("username")
    response_str = "false"
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        response_str = "true"
    return HttpResponse("%s" % response_str)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            user.save()
            return render_to_response('register/success.html', context_instance=RequestContext(request))
    else:
        form = RegisterForm()
    return render_to_response('register/register.html', {'form':form}, context_instance=RequestContext(request))

@login_required
def portal(request):
    return render_to_response('portal/index.html', context_instance=RequestContext(request))
'''
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/books/")
			
			 <p> 
                    <label for="emailsignup" class="youmail" data-icon="e" > Your email</label>
                    <input id="emailsignup" name="emailsignup" required="required" type="email" placeholder="mysupermail@mail.com"/> 
                </p>
                <p> 
                    <label for="passwordsignup" class="youpasswd" data-icon="p">Your password </label>
                    <input id="passwordsignup" name="passwordsignup" required="required" type="password" placeholder="eg. X8df!90EO"/>
                </p>
                <p> 
                    <label for="passwordsignup_confirm" class="youpasswd" data-icon="p">Please confirm your password </label>
                    <input id="passwordsignup_confirm" name="passwordsignup_confirm" required="required" type="password" placeholder="eg. X8df!90EO"/>
                </p>
    
'''