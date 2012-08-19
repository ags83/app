# Create your views here.

from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django import forms
from django.forms.models import model_to_dict
from django.template import RequestContext
from forms import CreateForm, EditForm, SearchForm
from django.db.models import Q
from django.contrib import messages

import math
import time

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from models import *
from items.models import Item
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def create(request, id=None):
    if id:
        item = get_object_or_404(Item,pk=id)
        print 'here '
        if item.user != request.user:
            raise HttpResponseForbidden()
    else:
        item = Item()

    if request.method == 'POST':
        if id:
            form = CreateForm(request.POST,request.FILES, instance=item) 
        else:
            form = CreateForm(request.POST,request.FILES)
        
        if form.is_valid():
            cd = form.cleaned_data
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return HttpResponseRedirect('/items/' + str(item.id) +'/')
			#item = form.save(commit=False)
            #temp_item.user = request.user
            #if len(request.FILES) == 1:
			#	temp_item.image=request.FILES['image']
                #item = Item(name=cd['name'], desc=cd['desc'], user=request.user, image=request.FILES['image'], category=cd['category'], lat=cd['lat'], long=cd['long'])
            #else:
            #    item = Item(name=cd['name'], desc=cd['desc'], user=request.user, category=cd['category'],  lat=cd['lat'], long=cd['long'])
            
            #if id is None:
            #    temp_item.save()
            #    messages.success(request, 'Item Created.')
            #    return HttpResponseRedirect('/items/' + str(temp_item.id) +'/')
            #else:
            #   
            #    f.user = request.user
            #    f.save()
            #    messages.success(request, 'Item Updated.')
            #    return HttpResponseRedirect('/items/' + str(item.id) +'/')
    else:
        form = CreateForm(instance=item)
	
    return render_to_response('item/add.html', {'form':form, 'item':item}, context_instance=RequestContext(request))
	
@login_required
def edit(request, item_id):
	if item_id:
		item = get_object_or_404(Item,pk=item_id)
	else:
		item = Item(user=request.user)
	
	if request.method == 'POST':
		form = EditForm(request.POST, request.FILES,instance=item)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/items/' + str(item.id) +'/')
	else:
		form = EditForm(instance=item)
	return render_to_response('item/edit.html', {'form':form}, context_instance=RequestContext(request))
	

def search(request):
    item_list = []
    queries_without_page = ''
    if 'category' in request.GET:
        queries_without_page = request.GET.copy()
        if queries_without_page.has_key('page'):
            del queries_without_page['page']
		
        form = SearchForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            temp_item_list = Item.objects.all()
			

            lat1 = cd['lat']
            long1 = cd['long']
            

            searcharea = cd['searcharea']
			
            if cd['category']:
                temp_item_list = temp_item_list.filter(category=cd['category'])
            lat1rad = math.radians(lat1)
            lat1cos = math.cos(lat1rad)
            long1rad = math.radians(long1)
            lat1sin = math.sin( lat1rad )
            unit = 6371
            #start_time = time.clock()
            for item in temp_item_list:
                lat2 = item.lat
                lat2rad = math.radians(lat2)
                long2 = item.long
                distance = float(unit) * math.acos( lat1cos * math.cos( lat2rad ) * math.cos( math.radians( long2 ) - long1rad ) + lat1sin * math.sin(lat2rad))
                if distance < searcharea:
                    item_list.append(item)
           # print time.clock() - start_time, "seconds"
           # print len(item_list)
                #item_list = item_list.filter(Q(name__icontains=cd['search']) | Q(desc__icontains=cd['search']))
    else:
        form = SearchForm()
		

    paginator = Paginator(item_list, 20)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
		
    return render_to_response('item/search.html', {'form':form,'items':items, 'request_method':request.method, 'queries':queries_without_page}, context_instance=RequestContext(request))
	
def view(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
		return render_to_response('errors/notexist.html')
    
    return render_to_response('item/view.html', {'item':item}, context_instance=RequestContext(request))

def latest (request):
    try:
        item_list = Item.objects.order_by('-created')[:100]
    except Item.DoesNotExist:
        return render_to_response('errors/notexist.html')	
    paginator = Paginator(item_list, 10)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    return render_to_response('item/list.html', {'items':items, 'heading':'Recently listed items'}, context_instance=RequestContext(request))
	
	
def myitems (request):
    try:
        item_list = Item.objects.filter(user=request.user)
    except Item.DoesNotExist:
        return render_to_response('errors/notexist.html')
    paginator = Paginator(item_list, 10)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    return render_to_response('item/list.html', {'items':items, 'heading':'Your Items'}, context_instance=RequestContext(request))

def delete(request, item_id):
    if request.method == 'POST':
        try:
            item = Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            return render_to_response('errors/notexist.html')
        item.delete()
        messages.success(request, 'Item Deleted.')
        return HttpResponseRedirect('/items/search/')
    else:
        return render_to_response('errors/notexist.html', context_instance=RequestContext(request))	



    
		
	
		
	
		
	
    
	
