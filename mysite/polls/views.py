# _*_ coding: utf-8 _*_
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django import forms
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime, timedelta
from django.contrib.auth.hashers import make_password
from django.template.loader import get_template
from django.contrib.auth.models import Group

from polls.models import *
from polls.forms import *

from account.models import *

#from polls.gym import *


def main_page(request):
    output = '''
      <html>
        <head><title>%s</title></head>
        <body>
          <h3>%s</h3>
          <p>%s</p>
        </body>
      </html>
    ''' % ('Strona startowa','Witamy :)','Wszystko działa')
    return HttpResponse(output)

'''
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = RequestContext(request, {
		'latest_question_list': latest_question_list,
	})
	#output = ', '.join([p.question_text for p in latest_question_list])
	return HttpResponse(template.render(context))

def detail(request, question_id):
	#try:
	#	question = Question.objects.get(pk=question_id)
	#except Question.DoesNotExist:
	#	raise Http404("Question does not exist")
	# To z góry prawie całe w jednej linijce	
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
    	return render(request, 'polls/results.html', {'question': question})
'''
'''
class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'
	
	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

def vote(request, question_id):
	p = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question': p,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
'''
def login_user(request):
	if request.method == 'POST':
		if request.POST.get("log_in"):
			if request.user.is_authenticated():
				logout(request)
			user = authenticate(username=request.POST['login_input'], password=request.POST['pass_input'])
			if user is not None:
		   		if user.is_active:
					login(request, user)
					return HttpResponseRedirect(reverse('user_acc'))
		    		else:
					return render(request, 'polls/login.html', {
						'error_message': "Brak użytkownika w bazie (nie aktywny)",
					})
			else:
				return render(request, 'polls/login.html', {
					'error_message': "Sprawdź login i hasło",
				})
		elif request.POST.get("log_out"):
			if request.user.is_authenticated():
				logout(request)
				return render(request, 'polls/index.html')
			else:
				return render(request, 'polls/index.html')
		elif request.POST.get("reg"):
			return HttpResponseRedirect(reverse('register'))
		else:
			return render(request, 'polls/login.html')
	else:
		return render(request, 'polls/index.html')
	'''	
	try:
		question = User.objects.get(login=request.POST['login'], haslo=request.POST['pass'])
	except User.DoesNotExist:
		return render(request, 'polls/login.html', {
			'question': p,
			'error_message': "Brak użytkownika w bazie",
		})
	else:
		return HttpResponseRedirect(reverse('polls:user_acc', args=(question.login)))
	'''

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
			if(request.POST['password'] == request.POST['repeat_password']):
				new_user = form.save(commit=False)
				new_user.username=new_user.email
				new_user.password = make_password(request.POST['password'])
				g = Group.objects.get(name='clients') 
				new_user.backend='django.contrib.auth.backends.ModelBackend'
				new_user.save();
				new_user.groups.add(g)
				new_user.save();
				if request.user.is_authenticated():
					logout(request)
					login(request, new_user)
					return HttpResponseRedirect(reverse('user_acc'))
				else:
					login(request, new_user)
					return HttpResponseRedirect(reverse('user_acc'))
				
    else:
        form = RegisterForm()
    return render(request, "polls/register.html", {
        'form': form,
    })
	
def registerface(request, email):
	u = CustomUser.objects.filter(email=email)
	if u:
		r = list(u[:1])
		r[0].backend='django.contrib.auth.backends.ModelBackend'
		r[0].save()
		login(request, r[0])
		return HttpResponseRedirect(reverse('user_acc'))
	else:
		return HttpResponseRedirect(reverse('register'))


def user_acc(request):
	username = None
	if request.user.is_authenticated():
		username = request.user.username
		vouchers = ClientsVoucher.objects.filter(client = request.user).order_by('date_end');
    		return render(request, 'polls/user_acc.html', {'user': request.user, 'vouchers': vouchers})
	else:
		return HttpResponseRedirect(reverse('login_user'))

def update_profile(request):
    args = {}

    if request.method == 'POST':
        form = UpdateProfile(request.POST, instance=request.user)
        if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('update_profile'))
    else:
        form = UpdateProfile(instance=request.user)

    args['form'] = form
    return render(request, 'polls/update_profile.html', args)

def change_password(request):
    args = {}

    if request.method == 'POST':
        form = ChangePassword(request.POST)
        if form.is_valid():
			if CustomUser.objects.filter(username=request.user.username).filter(password=make_password(form.cleaned_data['old_password'])).count():
				if form.cleaned_data['new_password'] == form.cleaned_data['repeat_new_password']:
					u = CustomUser.objects.get(username=request.user.username)
					u.set_password(make_password(form.cleaned_data['new_password']))
					u.save()
					return HttpResponseRedirect(reverse('change_password'))
				else:
					args['error'] = 'Podano różne hasła'
			else:
				args['error'] = 'Podano złe stare hasło'
    else:
        form = ChangePassword()

    args['form'] = form
    return render(request, 'polls/change_password.html', args)
	
def user_vouchers(request):
	username = None
	if request.user.is_authenticated():
		username = request.user.username
		vouchers = ClientsVoucher.objects.filter(client = request.user).order_by('date_end');
    		return render(request, 'polls/user_vouchers.html', {'user': request.user, 'vouchers': vouchers})
	else:
		return HttpResponseRedirect(reverse('login_user'))

def index(request):
    template = get_template("polls/index.html")
    variables=RequestContext(request)    
    output = template.render(variables)
    return HttpResponse(output)


