import requests

pixela_endpoint = "https://pixe.la/v1/users"

# Parameters to create a Account in Pixela using POST request.
user_params = {
    "token" : "OUR_OWN_TOKEN",
    "username" : "USER_NAME",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

response = requests.post(url=pixela_endpoint,json=user_params)

print(response.text)
