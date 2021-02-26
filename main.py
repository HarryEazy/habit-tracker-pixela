import requests
from datetime import datetime as dt

USERNAME = ""
TOKEN = ""
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

# ------------------------ HEADER ------------------------ #
headers = {
    "X-USER-TOKEN": TOKEN
}

# ------------------------ CREATE NEW USER ------------------------ #
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# ------------------------ CREATE NEW GRAPH ------------------------ #
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph config
graph_config = {
    "id": "graph1",
    "name": "Python Code Daily Graph",
    "unit": "Udemy lessons",
    "type": "float",
    "color": "momiji"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# html link to see graph
# https://pixe.la/v1/users/username/graphs/graphname
# https://pixe.la/v1/users/harryez/graphs/graph1.html

# ------------------------ CREATE NEW PIXEL ------------------------ #
# get today's date
today = dt.now()
# use strftime to format today's date in correct format for api
date = today.strftime("%Y%m%d")

pixel_data = {
    "date": date,
    "quantity": "1.0",
}
# end point
add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
response = requests.post(url=add_pixel_endpoint, json=pixel_data, headers=headers)
print(response.text)

# ------------------------ UPDATE PIXEL ------------------------ #
# update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
#
# updated_data = {
#     "quantity": "2.0",
# }
#
# response = requests.put(url=update_pixel_endpoint, json=updated_data, headers=headers)
# print(response.text)

# ------------------------ DELETE PIXEL ------------------------ #
# delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
#
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)
