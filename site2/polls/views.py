from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from .models import Post, Page

def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[::-1]
    latest_page_list = Page.objects.order_by('-ppub_date')[::-1]
    return render(request, 'polls/index.html', {'latest_post_list': latest_post_list, 'latest_page_list': latest_page_list})

def detail(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	latest_page_list = Page.objects.order_by('-ppub_date')[::-1]
	return render(request, 'polls/detail.html', {'post': post, 'latest_page_list': latest_page_list})

def pdetail(request, page_id):
	page = get_object_or_404(Page, pk=page_id)
	latest_page_list = Page.objects.order_by('-ppub_date')[::-1]
	return render(request, 'polls/pdetail.html', {'page': page, 'latest_page_list': latest_page_list})