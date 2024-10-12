# FastAPI MVC starter for Backend

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Dependencies](#dependencies-used)
- [Installation](#installation)

## Description

The FastAPI MVC Starter Template is an open-source project providing a starting point for building backend applications using the Model-View-Controller (MVC) architectural pattern with the FastAPI framework. This template is specifically designed to help backend developers create structured, scalable, and maintainable applications. It’s ideal for those looking to kickstart FastAPI development efficiently, without needing to set everything up from scratch.

### Objective
The project aims to provide a solid, reusable foundation for building backend applications with FastAPI. It reduces the initial setup and offers clear examples of implementing the MVC pattern in FastAPI, allowing developers to focus on business logic rather than repetitive technical setup.

### Features:

1. **MVC-Based Project Structure**
<br>Separates application logic into Model, View (API endpoints), and Controller layers to enhance code readability, modularity, and maintainability.


2. **ORM (Object-Relational Mapping) Support**
<br>Includes built-in support for SQLAlchemy, integrated with MySQL database using PyMySQL as default.


3. **Authentication and Authorization**
<br>Pre-configured JWT (JSON Web Token) authentication for securing APIs, including user login, registration, and access management.


4. **Middleware Support**
<br>Comes with middleware for logging, CORS (Cross-Origin Resource Sharing) configuration, and request tracking to simplify debugging and development.


5. **Migrations Database**
<br>Supports database migration schema using alembic, this allows developers to more easily make changes to database structures and perform migrations. This feature can also synchronize the sqlalchemy ORM model.


6. **Easy Configuration**
<br>Utilizes dotenv for environment variable management, simplifying the configuration and deployment of the application across different environments.

   
## Dependencies Used

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
- **Uvicorn**: A ASGI web server implementation for Python, asynchronous support, support HTTP/1.1 and WebSockets.
- **Alembic**: A lightweight database migration tool for usage with the SQLAlchemy Database Toolkit for Python.
- **SQLAlchemy**: A Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
- **PyJWT**: A Python library which allows you to encode and decode JSON Web Tokens (JWT).

## Installation

1. Clone Repository using git
```bash
git clone https://github.com/Jrhero14/FastApi-BackendMVC
cd FastApi-BackendMVC
```

2. Copy .env file and update it with your database credentials
```bash
cp .env.example .env
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Migrate database
```bash
alembic upgrade head
```

5. Run the Application
```bash
uvicorn app.main:app --reload
```

## Tables of Database

<img width="35%" src="https://i.ibb.co.com/FnZbtBd/Screenshot-2024-10-12-222819.png">

### Contributions
Developers are welcome to contribute to this project by opening issues, submitting pull requests, or suggesting improvements. All forms of contributions are greatly appreciated.