import paypalrestsdk

# Set up the PayPal REST API client
paypalrestsdk.configure({
    "mode": "sandbox",  # set to "live" for production environment
    "client_id": "AfaDIaxkUIVCOSL4vVELXUyWdygoJ9-DXKOKREzAfFaU_eUCQUm5ZMC8zWzHLjyEwPlNOGG8QPVOsNM4",
    "client_secret": "EIWP_v_JLzT4aqURapVMAmWQHs2gc_yRZtcmiunJC50Cki5O7lmQgi2IHA6q56rwAaqOCaUatkokRGZo"
})


# Test the API client by making a test call to the PayPal API
student_plan = paypalrestsdk.Plan({
    "name": "Student Plan",
    "description": "Enjoy your unlimited movies for 1 month. Php 1800 billed every 12 months. Watch all you want. Ad-free. Change or cancel your plan anytime.",
    "type": "fixed",
    "payment_definitions": [{
        "name": "Regular payment definition",
        "type": "REGULAR",
        "frequency_interval": "1",
        "frequency": "MONTH",
        "cycles": "12",
        "amount": {
            "currency": "PHP",
            "value": "150.00"
        }
    }],
    "merchant_preferences": {
        "return_url": "http://localhost:3000/success",
        "cancel_url": "http://localhost:3000/cancel",
        "auto_bill_amount": "YES",
        "initial_fail_amount_action": "CONTINUE",
        "max_fail_attempts": "1"
    }
})


basic_plan = paypalrestsdk.Plan({
    "name": "Basic Plan",
    "description": "Binge-watch for 6 months. Save up to 40% Watch all you want. Ad-free. Change or cancel your plan anytime.",
    "type": "fixed",
    "payment_definitions": [{
        "name": "Regular payment definition",
        "type": "REGULAR",
        "frequency_interval": "6",
        "frequency": "MONTH",
        "cycles": "12",
        "amount": {
            "currency": "PHP",
            "value": "600.00"
        }
    }],
    "merchant_preferences": {
        "return_url": "http://localhost:3000/success",
        "cancel_url": "http://localhost:3000/cancel",
        "auto_bill_amount": "YES",
        "initial_fail_amount_action": "CONTINUE",
        "max_fail_attempts": "1"
    }
})

premium_plan = paypalrestsdk.Plan({
    "name": "Premium Plan",
    "description": "Best Value Save up to 57% Watch all you want. Ad-free. Change or cancel your plan anytime.",
    "type": "fixed",
    "payment_definitions": [{
        "name": "Regular payment definition",
        "type": "REGULAR",
        "frequency_interval": "1",
        "frequency": "YEAR",
        "cycles": "12",
        "amount": {
            "currency": "PHP",
            "value": "1000"
        }
    }],
    "merchant_preferences": {
        "return_url": "http://localhost:3000/success",
        "cancel_url": "http://localhost:3000/cancel",
        "auto_bill_amount": "YES",
        "initial_fail_amount_action": "CONTINUE",
        "max_fail_attempts": "1"
    }
})


# Create the subscription plan
if student_plan.create() and basic_plan.create() and premium_plan.create():
    print("Subscription plan created successfully")
else:
    print("Subscription plan creation failed")