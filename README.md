# Django Application with Docker and DRF

This is a Django project with token-based authentication.

## Accessing the API Endpoints

1. Obtain a token: Send a POST request to `http://localhost:8000/api-token-auth/` with your username and password.
2. Access protected endpoints: Include the token in the `Authorization` header of your requests.

## Testing the API

1. Obtain a token:

   - Request: `POST http://localhost:8000/api-token-auth/`
   - Body: `{"username": "<your-username>", "password": "<your-password>"}`
   - Response: `{"token": "<your-token>"}`

2. Access a protected endpoint:

   - Request: `GET http://localhost:8000/api/tasks/`
   - Headers: `{"Authorization": "Token <your-token>"}`
   - Response: `{"data": "Protected data"}`
