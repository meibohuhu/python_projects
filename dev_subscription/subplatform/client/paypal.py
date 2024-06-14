
import requests
import json

from . models import Subscription


## can be directly invoked without creating class or instance of class
def get_access_token():    ## get oauth2 token

    data = {'grant_type': 'client_credentials'}
    headers = {'Accept': 'application/json', 'Accept-Language': 'en_US'}
    client_id = 'ARw8PL3Z-DFzLlBrBblLRVFSwZnWvZ96D55bulltEZaeCsLD509kgplz2EyjDcTvv_XuJZCMvFYk5O8h'
    secret_id = 'EGyyh8gjzpO6C_fSvqbR3Ocs0dh4HYKaLJY8gcrMQv2W1_Z-l5U3eWnGxCyx-ueMMpv4MPWAVpACtlYD'

    url = 'https://api.sandbox.paypal.com/v1/oauth2/token'
    the_response = requests.post(url, auth=(client_id, secret_id), headers=headers, data=data).json()

    access_token = the_response['access_token']
    return access_token


def cancel_subscription_paypal(access_token, subID):
    bearer_token = 'Bearer ' + access_token
    headers = {
        'Content-Type': 'application/json',
        'Authorization': bearer_token,
    }
    url = 'https://api.sandbox.paypal.com/v1/billing/subscriptions/' + subID + '/cancel'
    cancel_response = requests.post(url, headers=headers)
    print(cancel_response.status_code)

### 1. access token 2. parameters for new plan 3. calling revise API
def update_subscription_paypal(access_token, subID):
    bearer_token = 'Bearer ' + access_token

    headers = {
        'Content-Type': 'application/json',
        'Authorization': bearer_token,
    }
    subDetails = Subscription.objects.get(paypal_subscription_id=subID)

    # Obtain the current subscription plan for the user/client (Standard / Premium)
    current_sub_plan = subDetails.subscription_plan

    if current_sub_plan == "Standard":
        new_sub_plan_id = 'P-6VY56365R5239804VMX5G75I' # To Premium

    elif current_sub_plan == "Premium":
        new_sub_plan_id = 'P-0SU887131E602935VMX5G3EQ' # To Standard

    url = 'https://api.sandbox.paypal.com/v1/billing/subscriptions/' + subID + '/revise'
    print(new_sub_plan_id)

    revision_data = {
        "plan_id": new_sub_plan_id
    }
    # Make a POST request to PayPal's API for updating/revising a subscription
    r = requests.post(url, headers=headers, data=json.dumps(revision_data))

    # Output the response from PayPal
    response_data = r.json()
    print(response_data)

    approve_link = None
    for link in response_data.get('links', []):
        if link.get('rel') == 'approve':
            approve_link = link['href']

    if r.status_code == 200:

        print("Request was a success")

        return approve_link

    else:

        print("Sorry, an error occured!")















