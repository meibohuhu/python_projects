from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from writer.models import Article
from account.models import CustomUser
from . paypal import *
from django.http import HttpResponse

from . forms import UpdateUserForm
from . models import Subscription

# Create your views here.
@login_required(login_url='my-login')
def client_dashboard(request):
    try:
        subDetails = Subscription.objects.get(user=request.user)
        context = {'SubPlan': subDetails.subscription_plan}
        return render(request, 'client/client-dashboard.html', context)
    except:
        context = {'SubPlan': "None"}
        return render(request, 'client/client-dashboard.html', context)

@login_required(login_url='my-login')
def browse_articles(request):
    try:
        subDetails = Subscription.objects.get(user=request.user, is_active=True)
    except:
        return render(request, 'client/subscription-locked.html')                 ### if no subscriptions for this user, direct to subscription-lock HTML page

    current_subscription_plan = subDetails.subscription_plan
    if current_subscription_plan == 'Standard':
        articles = Article.objects.all().filter(is_premium=False)
    elif current_subscription_plan == 'Premium':
        articles = Article.objects.all()

    context = {'AllClientArticles':articles}
    return render(request, 'client/browse-articles.html', context)


@login_required(login_url='my-login')
def subscription_locked(request):

    return render(request, 'client/subscription-locked.html')


@login_required(login_url='my-login')
def subscription_plans(request):

    if not Subscription.objects.filter(user=request.user).exists():     ## if no subscription exists go to plan page
        return render(request, 'client/subscription-plans.html')
    else:
        return redirect('client-dashboard')     ### avoid user directly put /client/subscription-plans in browser, we do the backend check


@login_required(login_url='my-login')
def account_management(request):
    form = UpdateUserForm(instance=request.user)   ## populate form associate with existing form, if leave it empty, will blank
    account_management_general(request);

    try:
        # form = UpdateUserForm(instance=request.user)
        #
        # if request.method == 'POST':
        #     form = UpdateUserForm(request.POST, instance=request.user)
        #     if form.is_valid():
        #         form.save()
        #         return redirect('client-dashboard')

        # Check if the user has a subscription object
        subDetails = Subscription.objects.get(user=request.user)
        subscription_id = subDetails.paypal_subscription_id

        context = {'SubscriptionID': subscription_id, 'UpdateUserForm': form}
        return render(request, 'client/account-management.html', context)

    except:
        # Pass through data to our template
        context = {'UpdateUserForm': form}
        return render(request, 'client/account-management.html', context)


def account_management_general(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)  ## update form
        if form.is_valid():
            form.save()
            return redirect('client-dashboard')


### when will this URL be invoked to create the subscripton and save into our DB
### once we have received approval from PayPal for the transaction was made in Paypal side
## we need PayPal ID
@login_required(login_url='my-login')
def create_subscription(request, subID, plan):

    custom_user = CustomUser.objects.get(email=request.user)

    if not Subscription.objects.filter(user=request.user).exists():      ## handle unique constraint errors to avoid other users using same URL or user reload same page
        firstName = custom_user.first_name
        lastName = custom_user.last_name
        fullName = firstName + " " + lastName

        selected_sub_plan = plan

        if selected_sub_plan == "Standard":
            sub_cost = "4.99"

        elif selected_sub_plan == "Premium":
            sub_cost = "9.99"

        subscription = Subscription.objects.create(
            subscriber_name=fullName,
            subscription_plan=selected_sub_plan,
            subscription_cost=sub_cost,
            paypal_subscription_id=subID,
            is_active=True,
            user=request.user)

        context = {'SubscriptionPlan': selected_sub_plan}    ## show plan in subscription successful page
        return render(request, 'client/create-subscription.html', context)
    else:
        return redirect('client-dashboard')


@login_required(login_url='my-login')
def delete_subscription(request, subID):
    try:
        ## delete from Paypal
        access_token = get_access_token()
        cancel_subscription_paypal(access_token, subID)

        ## delete from Django
        subscription = Subscription.objects.get(user=request.user, paypal_subscription_id=subID)
        subscription.delete()

        return render(request, 'client/delete-subscription.html')       ## render delete-subscription.html without context
    except:
        return redirect('client-dashboard')

@login_required(login_url='my-login')
def update_subscription(request, subID):
    access_token = get_access_token()
    # approve_link = Hateoas link from PayPal

    approve_link = update_subscription_paypal(access_token, subID)
    if approve_link:
        return redirect(approve_link)
    else:
        return HttpResponse("Unable to obtain the approval link")


@login_required(login_url='my-login')
def delete_account(request):
    if request.method == 'POST':
        deleteUser = CustomUser.objects.get(email=request.user)
        deleteUser.delete()
        return redirect("")
    return render(request, 'client/delete-account.html')     ### only when click delete button from account-management.html, if really click delete from delete-account.html, then will post request




