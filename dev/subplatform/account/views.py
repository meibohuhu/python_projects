from django.shortcuts import render, redirect

from . forms import CreateUserForm

from django.contrib.auth.forms import AuthenticationForm

from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout

from django.contrib.sites.shortcuts import get_current_site

from . token import user_tokenizer_generate

from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str  ## transform our binary data into bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from django.core.mail import send_mail

from django.conf import settings

from . models import CustomUser

def home(request):

    return render(request, 'account/index.html')

def register(request):

    form = CreateUserForm()    ## create a variable => go ahead with value

    if request.method == "POST":    ## expect POST request, if we're getting a Post request from our HTML page, continue the process

        form = CreateUserForm(request.POST)      ## ensure all data in the createUserForm need to be sent via POST request

        if form.is_valid():

            form.save()    ## save into our database => our data that have been entered from CreateUserForm will be saved into DB

            '''
            user = form.save()

            user.is_active = False

            user.save()

            # Email verification config

            current_site = get_current_site(request)

            subject = 'Activate your account'

            message = render_to_string('account/email-verification.html', {

                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': user_tokenizer_generate.make_token(user),

            })

            user_email = user.email

            #send_mail(subject=subject, message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=[user_email])

            #return redirect('email-verification-sent')
            '''

            return redirect('my-login')    
            

    context = {'RegisterForm': form}    ## we want to ouput our form into our HTML page with key value pairs

    return render(request, 'account/register.html', context)


def my_login(request):

    form = AuthenticationForm()

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username') # Username / Email, since AuthenticationForm default function using username in Django
            password = request.POST.get('password')

            # Username / Email

            user = authenticate(request, username=username, password=password)

            ## a few check
            if user is not None and user.is_writer==True:

                login(request, user)

                return redirect('writer-dashboard')
                # return HttpResponse('Welcome writer')


            if user is not None and user.is_writer==False:

                login(request, user)

                return redirect('client-dashboard')
                # return HttpResponse('Welcome client!')


    context = {'LoginForm': form}   ## pass our form into HTML page

    return render(request, 'account/my-login.html', context)


def user_logout(request):

    logout(request)

    return redirect("my-login")



def email_verification(request, uidb64, token):

    unique_token = force_str(urlsafe_base64_decode(uidb64))

    custom_user = CustomUser.objects.get(pk=unique_token)

    if custom_user and user_tokenizer_generate.check_token(custom_user, token):

        custom_user.is_active = True
        custom_user.save()

        return redirect('email-verification-success')

    else:

        return redirect('email-verification-failed')



def email_verification_sent(request):

    return render(request, 'account/email-verification-sent.html')




def email_verification_success(request):

    return render(request, 'account/email-verification-success.html')




def email_verification_failed(request):

    return render(request, 'account/email-verification-failed.html')




