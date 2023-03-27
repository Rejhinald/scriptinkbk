import json
from django.http import JsonResponse
from paypalrestsdk import AccessToken, configure

# Set up the PayPal API client
configure({
    "mode": "sandbox", # set to "live" for production mode
    "client_id": "AfaDIaxkUIVCOSL4vVELXUyWdygoJ9-DXKOKREzAfFaU_eUCQUm5ZMC8zWzHLjyEwPlNOGG8QPVOsNM4",
    "client_secret": "EIWP_v_JLzT4aqURapVMAmWQHs2gc_yRZtcmiunJC50Cki5O7lmQgi2IHA6q56rwAaqOCaUatkokRGZo"
})

# View to generate a new access token
def get_access_token(request):
    access_token = AccessToken().get()
    return JsonResponse({"access_token": access_token})
