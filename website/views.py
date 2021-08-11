from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == 'POST':
		message_f_name = request.POST['f_name']
		message_l_name = request.POST['l_name']
		message_email = request.POST['email']
		message_phone = request.POST['phone']
		message = request.POST['note']

		send_mail(
			'New message from ' + message_f_name + ' ' + message_l_name, #subject
			message, #message
			message_email, #email
			# message_phone, #phone number
			['ovidio.cabeza@gmail.com'], # To email
			)


		return render(request, 'contact.html', {'f_name':message_f_name})
	else:
		return render(request, 'contact.html', {})
