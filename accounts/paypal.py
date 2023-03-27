import requests
import schedule
import time

client_id = "AfaDIaxkUIVCOSL4vVELXUyWdygoJ9-DXKOKREzAfFaU_eUCQUm5ZMC8zWzHLjyEwPlNOGG8QPVOsNM4"
client_secret = "EIWP_v_JLzT4aqURapVMAmWQHs2gc_yRZtcmiunJC50Cki5O7lmQgi2IHA6q56rwAaqOCaUatkokRGZo"

# Set up the API request\
url = "https://api.sandbox.paypal.com/v1/oauth2/token"
headers = {"Accept": "application/json", "Accept-Language": "en_US"}
data = {"grant_type": "client_credentials", "expires_in": 2592000}
auth = (client_id, client_secret)

# Send the request and parse the response JSON
def get_access_token():
    response = requests.post(url, headers=headers, data=data, auth=auth)
    if response.status_code != 200:
        print("API request failed with status code:", response.status_code)
    else:
        try:
            access_token = response.json()["access_token"]
            print("Access token:", access_token)
        except KeyError:
            print("Response JSON is missing the 'access_token' key:", response.content)


# Schedule the job to run every hour
schedule.every(1).minutes.do(get_access_token)

# Keep the script running indefinitely
while True:
    schedule.run_pending()
    time.sleep(1)