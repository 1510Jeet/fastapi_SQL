# FastAPI User API Project

This project is a simple REST API built with FastAPI and SQLAlchemy for managing a list of users. It allows you to add new users to a database and retrieve their information.

This guide provides a complete walkthrough of the setup, from preparing your environment to running and testing the API endpoints using either the auto-generated documentation or Postman.

## 📁 Project Structure

The project is organized into four main Python files:

- **`main.py`**: The core of the application. It defines the API endpoints (also called routes), handles incoming HTTP requests, and orchestrates the interaction with the database.
- **`database.py`**: Handles the database connection. It sets up the SQLAlchemy engine and session management required to communicate with the SQLite database.
- **`models.py`**: Defines the database table schema. The User class in this file is mapped to a users table in the database, defining its columns and data types using the SQLAlchemy ORM.
- **`schemas.py`**: Defines the data structure for API requests and responses using Pydantic. This ensures that any data sent to the API is valid and correctly formatted.

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
```

**Library Descriptions:**

- **fastapi**: A modern, fast web framework for building APIs.
- **uvicorn**: An ASGI server that runs the FastAPI application.
- **sqlalchemy**: A SQL toolkit and Object Relational Mapper (ORM) that helps Python communicate with databases.
- **pydantic**: A library for data validation and settings management.

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

### 1. Home Endpoint
- **URL**: `/`
- **Method**: GET
- **Description**: Returns a simple "Hello World" message
- **Response**: `{"message": "Hello World"}`

### 2. Add User
- **URL**: `/addUser`
- **Method**: POST
- **Description**: Creates a new user in the database
- **Request Body**:
  ```json
  {
    "id": 0,
    "name": "string",
    "email": "string",
    "nickname": "string"
  }
  ```
- **Response**: Returns the created user object with auto-generated ID

### 3. Get User by Name
- **URL**: `/user/{user_name}`
- **Method**: GET
- **Description**: Retrieves a user by their name
- **Path Parameters**:
  - `user_name`: The name of the user to retrieve
- **Response**: Returns the user object if found, or `null` if not found

## 🗄️ Database Schema

The application uses SQLite with the following user table structure:

| Column | Type | Description |
|--------|------|-------------|
| id | Integer | Primary key, auto-increment |
| name | String | User's full name |
| email | String | User's email address |
| nickname | String | User's nickname |

## 🚀 Features

- **FastAPI Framework**: Modern, fast web framework for building APIs
- **SQLAlchemy ORM**: Object-relational mapping for database operations
- **Pydantic Validation**: Automatic request/response validation
- **SQLite Database**: Lightweight, file-based database
- **Auto-generated Documentation**: Interactive API docs at `/docs`
- **Dependency Injection**: Clean separation of concerns

## 🔧 Development

### Running in Development Mode

```bash
uvicorn main:app --reload
```

The `--reload` flag enables auto-reloading when you make changes to the code.

### Database

The SQLite database file (`users.db`) will be automatically created when you first run the application.

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📞 Support

If you have any questions or need help with this project, please open an issue in the repository.
