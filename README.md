# Django Application with Docker and DRF

This is a Django project with token-based authentication.

## Running the Application

1. Build the Docker image: `docker build -t my-django-app .`
2. Run the Docker container: `docker run -p 8000:8000 my-django-app`

## Accessing the API Endpoints

1. Obtain a token: Send a POST request to `http://localhost:8000/api-token-auth/` with your username and password.

2. Access protected endpoints: Include the token in the `Authorization` header of your requests.

## Testing the API

1. Obtain a token:

   - Request: `POST http://localhost:8000/api-token-auth/`
   - Body: `{"username": "<your-username>", "password": "<your-password>"}`
   - Response: `{"token": "<your-token>"}`
  
Example:
  
![Screenshot 2024-02-07 at 1 26 33 PM](https://github.com/izzatkarimov/django_task/assets/108251704/879b5098-2d05-42a1-be17-064bd41f8479)

2. Access a protected endpoint:

   - Request: `GET http://localhost:8000/api/tasks/`
   - Headers: `{"Authorization": "Token <your-token>"}`
   - Response: `{"data": "Protected data"}`

Example:

![Screenshot 2024-02-07 at 1 47 10 PM](https://github.com/izzatkarimov/django_task/assets/108251704/8d336726-f987-4fb5-8a2d-abb2722a86d0)

<br>
  
![Screenshot 2024-02-07 at 1 26 36 PM](https://github.com/izzatkarimov/django_task/assets/108251704/849d9130-01f8-4465-b91b-48cdc4b33876)
