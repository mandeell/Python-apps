import requests
import datetime

USERNAME = "mandel"
TOKEN = "jwuw7hdhwu82h2hie9dud9"

headers = {
    "X-USER-TOKEN": TOKEN
}

date_time = datetime.date.today()
today = date_time.strftime("%Y%m%d")

def create_user(token: str, username: str):

    pixela_endpoint = "https://pixe.la/v1/users"

    user_params = {
        "token": token,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    response = requests.post(url=pixela_endpoint, json=user_params)
    print(response.text)

def create_graph(graph_id: str, name: str, unit: str, type_name: str, color: str,):

    graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

    graph_config = {
        "id": graph_id,
        "name": name,
        "unit": unit,
        "type": type_name,
        "color": color,
        "timezone": "Africa/Lagos",
    }
    response = requests.post(url=graph_endpoint, headers=headers, json=graph_config)
    print(response.text)

def post_a_pixel(steps: str, date):
    pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1"



    pixel_config = {
        "date": date,
        "quantity": steps,
    }
    response = requests.post(url=pixel_endpoint, headers=headers, json=pixel_config)
    print(response.text)

def update_pixel(steps: str, date):
    update_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1/{date}"

    update_pixel_config = {
        "quantity": steps,
    }

    response = requests.put(url=update_pixel_endpoint, headers=headers, json=update_pixel_config)
    print(response.text)

def delete_pixel(date: str):
    delete_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1/{date}"
    response = requests.delete(url=delete_pixel_endpoint, headers=headers)
    print(response.text)
