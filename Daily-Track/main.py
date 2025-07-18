from http.client import responses

import requests

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
# response = requests.post(url=pixela_endpoint,json=user_params)



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

# response = requests.post(
#     url=graph_endpoint,
#     json=graph_config,
#     headers=headers
# )

# Step3 Add a pixel into the Graph.

post_pixel_end_point = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPHID}"

pixel_config = {
    "date" : "20250718",
    "quantity" : "10.5"
}

response = requests.post(
    url=post_pixel_end_point,
    json=pixel_config,
    headers=headers
)
print(response.text)