from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Course, Enrollment
from .forms import ContactCourse




#from django.core.mail import send_mail, BadHeaderError
#from django.http import HttpResponse, HttpResponseRedirect
#from django.shortcuts import render, redirect







def index(request):
	course = Course.objects.all()
	template_name = 'courses/index.html'
	context = {'courses': course}
	return render(request, template_name, context)

#def details(request, pk):
#	course = get_object_or_404(Course, pk=pk)
#	context = {'courses': course}
#	template_name = 'courses/details.html'
#	return render(request, template_name, context)	


def details(request, slug):
	course = get_object_or_404(Course, slug=slug)
	context = {}
	if request.method == 'POST':
		form = ContactCourse(request.POST)
		if form.is_valid():
			context['is_valid'] = True
			form.send_mail(course)
			form = ContactCourse()
	else:
		form = ContactCourse()	
	context['form'] = form
	context['course'] = course
	template_name = 'courses/details.html'
	return render(request, template_name, context)	

@login_required
def enrollment(request, slug):
	course = get_object_or_404(Course, slug=slug)
	enrollment, created = Enrollment.objects.get_or_create( user= request.user, course=course)
	if created:
		#	enrollment.active()
		messages.success(request, 'Voçê foi inscrito no Curso com Sucesso')
	else:
		messages.info(request, 'Voçê já está inscrito no Curso')	
	return redirect('accounts:dashboard')

@login_required
def announcements(request, slug):
	course = get_object_or_404(Course, slug=slug)
	if not request.user.is_staff:
		enrollment = get_object_or_404(Enrollment, user= request.user, course=course)
		if not enrollment.is_approved():
			messages.error(request, 'A sua inscrição está pendente')	
			return redirect('acconuts:dashbord')
	template = 'courses/announcements.html'
	context = {}
	return render(request, template, context)







