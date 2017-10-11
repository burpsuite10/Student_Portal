from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import contactForm
# Create your views here.
def contact(request):
	title = 'Contact'
	form = contactForm(request.POST or None)
	confirm_message = None
	context = {'title': title,'form': form, }
	if form.is_valid():
		name = form.cleaned_data['name']
		comment = form.cleaned_data['comment']
		subject = 'Email From MyMail'
		message = ' %s %s ' %(name,comment)
		emailfrom = form.cleaned_data['email']
		emailto = [settings.EMAIL_HOST_USER]
		send_mail(subject, message, emailfrom, emailto,fail_silently=True)
		title = 'Thanks!'
		confirm_message = "Thanks for the message. We will get right back to you."
		form = None

	context = {'title': title, 'form' : form, 'confirm_message': confirm_message,}
	
	template = 'contact.html'
	return render(request,template,context)