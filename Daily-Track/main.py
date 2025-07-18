import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USER_NAME = ""
TOKEN = ""
GRAPHID = "graph1"

# Step 1 ) Parameters to create a Account in Pixela using POST request.
user_params = {
    "token" : TOKEN,
    "username" : USER_NAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}
# Create your user account
response1 = requests.post(url=pixela_endpoint,json=user_params)



# Step 2) Create a graph definition.
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

# Json data to make a post request at graph_en_point.
# Create a graph definition

graph_config = {
    "id" : "graph1",
    "name" : "Cycling Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "ajisai"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

response2 = requests.post(
    url=graph_endpoint,
    json=graph_config,
    headers=headers
)

# Step3 Add a pixel into the Graph.

post_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPHID}"

# Automatically get today's date.
today = datetime.now()

pixel_config = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : input("How many kilometers did you ran today ?:")
}

response3 = requests.post(
    url=post_pixel_endpoint,
    json=pixel_config,
    headers=headers
)


# Step 4 Update the Pixel in the Graph.
update_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPHID}/{today.strftime("%Y%m%d")}"

update_data = {
    "quantity" : "10.5"
}

response4 = requests.put(
    url=update_pixel_endpoint,
    json=update_data,
    headers=headers
)

# Step 5 Delete a Pixel

delete_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPHID}/{today.strftime("%Y%m%d")}"

response5 = requests.delete(
    url=delete_pixel_endpoint,
    headers=headers
)
