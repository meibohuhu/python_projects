from django.urls import path

from . import views

urlpatterns = [

  path('client-dashboard', views.client_dashboard, name="client-dashboard"),
  path('browse-articles', views.browse_articles, name="browse-articles"),
  path('subscription-plans', views.subscription_plans, name="subscription-plans"),
  path('account-management-2', views.account_management, name="account-management-2"),    ## differiant with writer/account-management
  path('subscription-plans', views.subscription_plans, name="subscription-plans"),
#### after subscription creation, Subscription URL's for PayPal callback
  path('create-subscription/<subID>/<plan>', views.create_subscription, name="create-subscription"),
## subscription delete from Paypal and Django sides, also redirect to delete-subscription.html
  path('delete-subscription/<subID>', views.delete_subscription, name="delete-subscription"),

## subscription update from Paypal and Djangp side
  path('update-subscription/<subID>', views.update_subscription, name="update-subscription"),
  path('delete-account-2', views.delete_account, name="delete-account-2"),    ## from account-management.html

]

