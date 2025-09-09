# FastAPI User API Project with JWT Authentication

This project is a secure REST API built with FastAPI, SQLAlchemy, and JWT (JSON Web Token) authentication for managing users. It provides user registration, login, and protected endpoints with token-based authentication.

This guide provides a complete walkthrough of the setup, from preparing your environment to running and testing the API endpoints using either the auto-generated documentation or Postman, with detailed explanations of JWT authentication implementation.

## 📁 Project Structure

The project is organized into five main Python files:

- **`main.py`**: The core of the application. It defines the API endpoints (also called routes), handles incoming HTTP requests, orchestrates the interaction with the database, and implements JWT authentication logic.
- **`auth.py`**: Handles all authentication-related functionality including password hashing, JWT token creation and validation, and OAuth2 password bearer scheme implementation.
- **`database.py`**: Handles the database connection. It sets up the SQLAlchemy engine and session management required to communicate with the SQLite database.
- **`models.py`**: Defines the database table schema. The User class in this file is mapped to a users table in the database, defining its columns and data types using the SQLAlchemy ORM, including hashed password storage.
- **`schemas.py`**: Defines the data structure for API requests and responses using Pydantic. This ensures that any data sent to the API is valid and correctly formatted, including JWT token schemas.

## 🛠️ Step 1: Setup Instructions

Follow these steps to get the project running on your local machine.

### 1. Prerequisite: Python

Ensure you have Python 3 installed. You can check your version by opening a terminal (or cmd/PowerShell on Windows) and running:

```bash
python --version
```

If that command doesn't work, try:

```bash
python3 --version
```

If you don't have Python installed, you can download it from [python.org](https://python.org).

### 2. Create the Project Directory

Create a folder for the project and navigate into it.

```bash
# Create a new directory
mkdir user_api_project

# Change into the new directory
cd user_api_project
```

Next, create the necessary files within this directory:

- `database.py`
- `main.py`
- `models.py`
- `schemas.py`
- `requirements.txt`

### 3. Add the Code

Copy and paste the provided code into the corresponding files you just created.

### 4. Define Project Dependencies

The project relies on several external Python libraries. List them in the `requirements.txt` file so they can be easily installed.

**requirements.txt:**
```
fastapi
uvicorn[standard]
sqlalchemy
pydantic
python-jose[cryptography]
passlib[bcrypt]
python-multipart
email-validator
```

**Library Descriptions:**

- **fastapi**: A modern, fast web framework for building APIs with built-in support for OAuth2 and JWT.
- **uvicorn**: An ASGI server that runs the FastAPI application.
- **sqlalchemy**: A SQL toolkit and Object Relational Mapper (ORM) that helps Python communicate with databases.
- **pydantic**: A library for data validation and settings management with email validation support.
- **python-jose**: A library for encoding and decoding JWT tokens with support for multiple algorithms.
- **passlib**: A comprehensive password hashing library supporting bcrypt and other secure hashing schemes.
- **python-multipart**: Required for handling form data in OAuth2 password flow.
- **email-validator**: Provides email validation for Pydantic models.

### 5. Create a Virtual Environment

It is best practice to use a virtual environment to manage project-specific dependencies. In your terminal, from the project root directory, run:

```bash
# For macOS/Linux
python3 -m venv venv

# For Windows
python -m venv venv
```

This creates a `venv` folder. To activate the environment, run:

```bash
# For macOS/Linux
source venv/bin/activate

# For Windows
.\venv\Scripts\activate
```

Your terminal prompt should now be prefixed with `(venv)`, indicating the environment is active.

### 6. Install Dependencies

With the virtual environment active, install all the required libraries:

```bash
pip install -r requirements.txt
```

The setup is now complete. ✅

## 🔐 JWT Authentication Explained

### What is JWT (JSON Web Token)?

JWT is a compact, URL-safe means of representing claims to be transferred between two parties. It's an open standard (RFC 7519) that defines a way for securely transmitting information as a JSON object. This information can be verified and trusted because it is digitally signed.

### JWT Structure

A JWT consists of three parts separated by dots (`.`):

```
xxxxx.yyyyy.zzzzz
```

1. **Header** (xxxxx): Contains metadata about the token
2. **Payload** (yyyyy): Contains the claims (user data)
3. **Signature** (zzzzz): Used to verify the token hasn't been tampered with

#### Header Example:
```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

#### Payload Example:
```json
{
  "sub": "user@example.com",
  "exp": 1640995200,
  "iat": 1640908800
}
```

### JWT in This Project

#### 1. Token Creation Process

When a user successfully logs in via `/token` endpoint:

1. **User Authentication**: Email and password are verified against the database
2. **Password Verification**: Uses bcrypt to compare the provided password with the stored hash
3. **Token Generation**: Creates a JWT with user email as the subject (`sub`)
4. **Expiration**: Token expires after 30 minutes (configurable)
5. **Signing**: Token is signed with a secret key using HS256 algorithm

#### 2. Token Validation Process

For protected endpoints:

1. **Token Extraction**: Extracts Bearer token from Authorization header
2. **Signature Verification**: Verifies the token signature using the secret key
3. **Expiration Check**: Ensures the token hasn't expired
4. **User Lookup**: Fetches user from database using email from token payload
5. **Authorization**: Grants access if all checks pass

#### 3. Security Features

- **Password Hashing**: Uses bcrypt with automatic salt generation
- **Token Expiration**: Prevents indefinite access (30-minute default)
- **Secret Key**: Uses environment variable for production security
- **Algorithm Security**: Uses HMAC SHA-256 for token signing
- **No Token Storage**: Server doesn't store tokens (stateless)

#### 4. OAuth2 Password Flow

This implementation follows OAuth2 Password Grant flow:

1. **Client** sends username (email) and password to `/token`
2. **Server** validates credentials and returns access token
3. **Client** includes token in Authorization header for protected requests
4. **Server** validates token and grants access to protected resources

### Environment Variables

For production, set these environment variables:

```bash
# Generate a secure secret key
export SECRET_KEY="your-super-secure-secret-key-here"

# Optional: Customize token expiration
export ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### JWT Security Best Practices

1. **Secret Key Management**: Use a strong, random secret key and store it securely
2. **Token Expiration**: Set reasonable expiration times (15-60 minutes)
3. **HTTPS Only**: Always use HTTPS in production to prevent token interception
4. **Token Storage**: Store tokens securely on client side (httpOnly cookies recommended)
5. **Refresh Tokens**: Implement refresh token rotation for long-lived sessions
6. **Algorithm Security**: Use strong algorithms (HS256, RS256)
7. **Token Revocation**: Implement token blacklisting for immediate revocation

## ▶️ Step 2: Running the Server

To start the API, run the following command from your project's root directory:

```bash
uvicorn main:app --reload
```

You should see output indicating the server is running on `http://127.0.0.1:8000`. Keep this terminal window open.

## 🧑‍🔬 Step 3: Interacting with the API (Browser Method)

FastAPI automatically generates interactive API documentation. This is the easiest way to test your endpoints.

Open your web browser and navigate to: **http://127.0.0.1:8000/docs**

You can use this interface to POST (add) a new user and GET (retrieve) a user by their name, as described in the previous guide.

## 🧪 Step 4: Testing with Postman (Alternative Method)

Postman is a popular application for testing APIs. It gives you more control and is a standard tool used by developers.

First, download and install Postman from their [website](https://www.postman.com/downloads/).

### Add a New User (POST /addUser)

1. Open Postman and create a new request by clicking the + button.
2. Set the HTTP method to **POST**.
3. Enter the request URL: `http://127.0.0.1:8000/addUser`.
4. Go to the "Body" tab below the URL bar.
5. Select the **raw** radio button and choose **JSON** from the dropdown menu.
6. In the text area, paste the details of the user you want to create:

```json
{
  "id": 0,
  "name": "Jane Smith",
  "email": "jane.smith@example.com",
  "nickname": "Jan"
}
```

7. Click the "Send" button.
8. You should see a **Status: 200 OK** and the created user's data will appear in the response body at the bottom of the screen.

### Get a User by Name (GET /user/{user_name})

1. Create another new request in Postman.
2. Set the HTTP method to **GET**.
3. Enter the request URL, replacing `{user_name}` with the actual name of the user you want to find. If the name has spaces, Postman will automatically encode them (e.g., "Jane Smith" becomes "Jane%20Smith").
   ```
   http://127.0.0.1:8000/user/Jane Smith
   ```
4. Since this is a GET request, no request body is needed.
5. Click the "Send" button.
6. If the user exists, you will see a **Status: 200 OK** and their data will be returned in the JSON response body. If not, the response body will show `null`.

You can stop the server at any time by returning to your terminal and pressing **Ctrl + C**.

## 📋 API Endpoints

### Public Endpoints (No Authentication Required)

#### 1. User Registration
- **URL**: `/signup`
- **Method**: POST
- **Description**: Creates a new user account with hashed password
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "nickname": "johndoe",
    "password": "securepassword123"
  }
  ```
- **Response**: Returns the created user object (without password)
- **Error**: `400 Bad Request` if email already exists

#### 2. User Login
- **URL**: `/token`
- **Method**: POST
- **Description**: Authenticates user and returns JWT access token
- **Request Body** (form data):
  ```
  username: john@example.com
  password: securepassword123
  ```
- **Response**:
  ```json
  {
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "token_type": "bearer"
  }
  ```
- **Error**: `401 Unauthorized` if credentials are invalid

### Protected Endpoints (JWT Authentication Required)

All protected endpoints require the `Authorization` header:
```
Authorization: Bearer <your-jwt-token>
```

#### 3. Get Current User
- **URL**: `/users/me/`
- **Method**: GET
- **Description**: Retrieves the currently authenticated user's information
- **Headers**: `Authorization: Bearer <token>`
- **Response**: Returns the current user's data (without password)
- **Error**: `401 Unauthorized` if token is invalid or expired

#### 4. Get User by ID
- **URL**: `/user/{user_id}`
- **Method**: GET
- **Description**: Retrieves a specific user by their ID
- **Path Parameters**:
  - `user_id`: The ID of the user to retrieve
- **Headers**: `Authorization: Bearer <token>`
- **Response**: Returns the user object if found
- **Error**: 
  - `401 Unauthorized` if token is invalid
  - `404 Not Found` if user doesn't exist

## 🗄️ Database Schema

The application uses SQLite with the following user table structure:

| Column | Type | Description |
|--------|------|-------------|
| id | Integer | Primary key, auto-increment |
| name | String(255) | User's full name |
| email | String(255) | User's email address (unique, indexed) |
| nickname | String(255) | User's nickname |
| hashed_password | String(255) | Bcrypt hashed password |

### Password Security

- **Hashing Algorithm**: bcrypt with automatic salt generation
- **Salt Rounds**: Default bcrypt configuration (typically 12 rounds)
- **Storage**: Only hashed passwords are stored, never plain text
- **Verification**: Uses `passlib` library for secure password comparison

## 🚀 Features

### Core Framework
- **FastAPI Framework**: Modern, fast web framework for building APIs with built-in OAuth2 support
- **SQLAlchemy ORM**: Object-relational mapping for database operations
- **Pydantic Validation**: Automatic request/response validation with email validation
- **SQLite Database**: Lightweight, file-based database with user management

### Authentication & Security
- **JWT Authentication**: Secure token-based authentication using JSON Web Tokens
- **Password Hashing**: bcrypt-based password hashing with automatic salt generation
- **OAuth2 Password Flow**: Standard OAuth2 implementation for secure authentication
- **Token Expiration**: Configurable token expiration (30 minutes default)
- **Stateless Authentication**: No server-side session storage required

### API Features
- **Auto-generated Documentation**: Interactive API docs at `/docs` with authentication support
- **Dependency Injection**: Clean separation of concerns with FastAPI's dependency system
- **Protected Endpoints**: JWT-protected routes with automatic token validation
- **Error Handling**: Comprehensive error handling with appropriate HTTP status codes
- **CORS Support**: Cross-origin resource sharing support for web applications

## 🔧 Development

### Running in Development Mode

```bash
uvicorn main:app --reload
```

The `--reload` flag enables auto-reloading when you make changes to the code.

### Database

The SQLite database file (`users.db`) will be automatically created when you first run the application.

## 🧪 Testing the API with JWT Authentication

### Using FastAPI's Interactive Documentation

1. **Navigate to**: `http://127.0.0.1:8000/docs`
2. **Register a User**: Use the `/signup` endpoint to create a new user
3. **Get Access Token**: Use the `/token` endpoint to authenticate and get a JWT token
4. **Authorize**: Click the "Authorize" button and enter your token
5. **Test Protected Endpoints**: Use `/users/me/` and `/user/{user_id}` endpoints

### Using Postman

#### Step 1: Register a New User

1. **Method**: POST
2. **URL**: `http://127.0.0.1:8000/signup`
3. **Headers**: `Content-Type: application/json`
4. **Body** (raw JSON):
   ```json
   {
     "name": "John Doe",
     "email": "john@example.com",
     "nickname": "johndoe",
     "password": "securepassword123"
   }
   ```

#### Step 2: Login and Get JWT Token

1. **Method**: POST
2. **URL**: `http://127.0.0.1:8000/token`
3. **Headers**: `Content-Type: application/x-www-form-urlencoded`
4. **Body** (form-data):
   ```
   username: john@example.com
   password: securepassword123
   ```
5. **Response**: Copy the `access_token` from the response

#### Step 3: Test Protected Endpoints

1. **Method**: GET
2. **URL**: `http://127.0.0.1:8000/users/me/`
3. **Headers**: 
   ```
   Authorization: Bearer <your-access-token>
   ```

### Using cURL

#### Register User
```bash
curl -X POST "http://127.0.0.1:8000/signup" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Jane Smith",
    "email": "jane@example.com",
    "nickname": "janesmith",
    "password": "mypassword123"
  }'
```

#### Login and Get Token
```bash
curl -X POST "http://127.0.0.1:8000/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=jane@example.com&password=mypassword123"
```

#### Access Protected Endpoint
```bash
curl -X GET "http://127.0.0.1:8000/users/me/" \
  -H "Authorization: Bearer <your-access-token>"
```

## 🔒 Security Considerations

### Production Deployment

1. **Environment Variables**: Set secure environment variables
   ```bash
   export SECRET_KEY="your-super-secure-secret-key-here"
   export ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

2. **HTTPS**: Always use HTTPS in production to protect JWT tokens

3. **Database Security**: Use a production database (PostgreSQL, MySQL) instead of SQLite

4. **Token Storage**: Implement secure token storage on client side

### Common Security Issues

- **Weak Secret Keys**: Use cryptographically secure random keys
- **Token Exposure**: Never log or expose JWT tokens in client-side code
- **Long-lived Tokens**: Implement refresh token rotation for better security
- **Token Validation**: Always validate token signature and expiration
- **Password Policies**: Implement strong password requirements

## 📚 Additional Resources

- [JWT.io](https://jwt.io/) - JWT token decoder and debugger
- [FastAPI Security Documentation](https://fastapi.tiangolo.com/tutorial/security/)
- [OAuth2 Specification](https://tools.ietf.org/html/rfc6749)
- [JWT Specification (RFC 7519)](https://tools.ietf.org/html/rfc7519)
- [bcrypt Documentation](https://pypi.org/project/bcrypt/)

