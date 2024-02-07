# Django Application with Docker and DRF

This is a Django project with token-based authentication.

## Accessing the API Endpoints

1. Obtain a token: Send a POST request to `http://localhost:8000/api-token-auth/` with your username and password.

![Screenshot 2024-02-07 at 1 26 33 PM](https://github.com/izzatkarimov/django_task/assets/108251704/879b5098-2d05-42a1-be17-064bd41f8479)

2. Access protected endpoints: Include the token in the `Authorization` header of your requests.

![Screenshot 2024-02-07 at 1 26 36 PM](https://github.com/izzatkarimov/django_task/assets/108251704/849d9130-01f8-4465-b91b-48cdc4b33876)

## Testing the API

1. Obtain a token:

   - Request: `POST http://localhost:8000/api-token-auth/`
   - Body: `{"username": "<your-username>", "password": "<your-password>"}`
   - Response: `{"token": "<your-token>"}`

2. Access a protected endpoint:

   - Request: `GET http://localhost:8000/api/tasks/`
   - Headers: `{"Authorization": "Token <your-token>"}`
   - Response: `{"data": "Protected data"}`
