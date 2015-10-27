from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.contrib.auth.models import User, Permission, AnonymousUser
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from sdk import geetest
from models import *
from forms import *


# view for register/sign-up page
def register(request):
	if request.method == 'POST':
		form = registerFrom(request.POST)
		if form.is_valid():
			#receive date from form and create user, in fact, a roll back process should be performed here.
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			name = form.cleaned_data['name']
			sig = form.cleaned_data['sig']
			u = User.objects.create_user(username, email, password)
			
			#grant the new user with regular permissions
			add_blog_permission = Permission.objects.get(codename='add_blog')
			change_blog_permission = Permission.objects.get(codename='change_blog')
			delete_blog_permission = Permission.objects.get(codename='delete_blog')
			add_comment_permission = Permission.objects.get(codename='add_comment')
			add_message_permission = Permission.objects.get(codename='add_message')
			delete_message_permission = Permission.objects.get(codename='delete_message')
			u.user_permissions.add(add_blog_permission, change_blog_permission, delete_blog_permission, add_comment_permission, add_message_permission, delete_message_permission)
			
			Author.objects.create(user=u, name=name, sig=sig)
			return HttpResponseRedirect(reverse('login', args=()))
	form = registerFrom()
	return render(request, 'register.html', {'form': form})

#view for login page
def login_view(request):
	if request.method == 'POST':
		form = loginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			u = authenticate(username=username, password=password)
			#look up the user and check the password in database, then if authenticated, login the user.
			if u != None:
				if u.is_active:
					login(request, u)
					uid = u.author.id
					return HttpResponseRedirect(reverse('author', args=(uid,)))
	form = loginForm()
	return render(request, 'login_view.html', {'form': form})

#view for author page, a list of blogs and author information of the user.
#author logged in visiting page of himself or others, and author not logged in visiting author page were rendered to different 
#html template respectively.
def author(request, author_id):
	if request.user.is_authenticated():
		user_au = request.user
		author_au = user_au.author
		blogs_au = author_au.blog_set.all().order_by('-pub_date')
		#if request.session.get('_auth_user_id') == author_id:
		if request.user.username == Author.objects.get(pk=author_id).user.username:
			return render(request, 'author_ld_sf.html', {'user_au': user_au, 'author_au': author_au, 'blogs_au': blogs_au})
		else:
			author = Author.objects.get(pk=author_id)
			user = author.user
			blogs = author.blog_set.all().order_by('-pub_date')
			return render(request, 'author_ld_ot.html', {'author':author, 'user':user, 'blogs':blogs, 'author_au': author_au})
	else:
		author = Author.objects.get(pk=author_id)
		user = author.user
		blogs = author.blog_set.all().order_by('-pub_date')
		return render(request, 'author_tr.html', {'author':author, 'user':user, 'blogs':blogs})

#view for adding a blog
def input(request):
	if request.user.is_authenticated():
		author = request.user.author
		if request.method == 'POST':
			form = inputForm(request.POST)
			if form.is_valid():
				title = form.cleaned_data['title']
				sub_title = form.cleaned_data['sub_title']
				content = form.cleaned_data['content']
				Blog.objects.create(author=author, title=title, sub_title=sub_title, content=content)
				return HttpResponseRedirect(reverse('author', args=(author.id, )))
		form = inputForm()
		author_au = request.user.author
		return render(request, 'input.html', {'form': form, 'author_au': author_au})
	else:
		return HttpResponseRedirect(reverse('login', args=()))

#view for home page, render for logged in user and not logged in user respectively.
def index(request):
	if request.user.is_authenticated():
		blog_list = Blog.objects.all().order_by('-pub_date')[:10]
		author_au = request.user.author
		authors = Author.objects.all().order_by('-up_num')[:10]
		return render(request, 'index_ld.html', {'blog_list': blog_list, 'author_au': author_au, 'authors': authors})
	else:
		return render(request, 'welc.html')

#view for blog page
def blog(request, blog_id):
	blog = Blog.objects.get(pk=blog_id)
	author = blog.author
	comments = blog.comment_set.all()
	if request.user.is_authenticated():
		author_au = request.user.author
		blogs = author.blog_set.exclude(pk=blog_id).order_by('-pub_date')[:5]
		#tring to using ajax
		if request.is_ajax():
			data = {"html": render_to_string("messages/_message_list.html",{
				"messages": request.user.messages.all()
				}, context_instance=RequestContext(request))}
			return HttpResponse(json.dumps(data), mimetype="application/json")



		if author == author_au:
			return render(request, 'blog_ld_sf.html', {'blog':blog, 'author':author, 'author_au':author_au, 'comments':comments})
		else:
			return render(request, 'blog_ld_ot.html', {'blog':blog, 'author':author, 'author_au':author_au, 'comments':comments, 'blogs':blogs})
	else:
		return render(request, 'blog_tr.html', {'blog':blog, 'author':author, 'comments':comments})

#to logout, no view and template, always redirected to index page.
def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('index', args=()))

#view for modify blog, not implemented yet.
def modify_blog(request, blog_id):
	blog = Blog.objects.get(pk=blog_id)
	u = request.user
	blog_au_user_username = Blog.objects.get(pk=blog_id).author.user.username
	if u.is_authenticated():
		if u.username == blog_au_user_username:
			if request.method == 'POST':
				form = inputForm
				pass

#about me page
def about(request):
	return render(request, 'about.html')

#not implemented
def comment(request):
	return HttpResponse('OK')

#check the permission to delete blog and if true then delete.
def delete_blog(request, blog_id):
	blog = Blog.objects.get(pk=blog_id)
	u = request.user
	blog_au_user_username = Blog.objects.get(pk=blog_id).author.user.username
	if u.is_authenticated():
		if u.username == blog_au_user_username:
			blog.delete()
			author_au = u.author
			return HttpResponseRedirect(reverse('author', args=(author_au.id,)))
