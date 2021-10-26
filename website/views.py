from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage

from melectric_web.settings import EMAIL_HOST_USER


# Create your views here.


def leave_a_review(request): # func to render and process the review information and send it to email
	if request.method == 'POST': # If form has been sent then send the email
		message_f_name = request.POST['f_name']
		message_company = request.POST['company_position']
		message_email = request.POST['email']
		# message_phone = request.POST['picture']
		to_email = ['ovidio.cabeza@gmail.com',]
		message = message_email + ', ' + request.POST['message'] 
		message_subject = 'New review from ' + message_f_name + ', from ' + message_company
		email = EmailMessage(message_subject, message, EMAIL_HOST_USER, to_email)

		# picture = request.FILES['picture']
		email.send()

		return render(request, 'getreviews.html', {'f_name':message_f_name})
	else:
		return render(request, 'getreviews.html', {})


def home(request): #function to render the home page
	return render(request, 'home.html', {})


def about(request): #function to render the about page
	return render(request, 'about.html', {})


def contact(request): # function to send the email in contact form
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
			['ovidio.cabeza@gmail.com','Josemenendez@m-electric.net','admin@m-electric.net'], # To email
			)


		return render(request, 'contact.html', {'f_name':message_f_name})
	else:
		return render(request, 'contact.html', {})
