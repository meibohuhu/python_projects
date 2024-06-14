from django.urls import path

from . import views

urlpatterns = [

  path('client-dashboard', views.client_dashboard, name="client-dashboard"),

  path('browse-articles', views.browse_articles, name="browse-articles"),

  path('subscription-locked', views.subscription_locked, name="subscription-locked"),

  path('subscription-plans', views.subscription_plans, name="subscription-plans"),

  path('account-management-2', views.account_management, name="account-management-2"),

  # Subscription URL's

  path('create-subscription/<subID>/<plan>', views.create_subscription, name="create-subscription"),

  path('delete-subscription/<subID>', views.delete_subscription, name="delete-subscription"),

  path('update-subscription/<subID>', views.update_subscription, name="update-subscription"),


  path('paypal-update-sub-confirmed', views.paypal_update_sub_confirmed, name="paypal-update-sub-confirmed"),

  path('django-update-sub-confirmed/<subID>', views.django_update_sub_confirmed, name="django-update-sub-confirmed"),


  # Account management (delete an account)

  path('delete-account-2', views.delete_account, name="delete-account-2"),

]