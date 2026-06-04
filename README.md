# Social Media API

A Restful Social Media API built with **Django** and **Django REST Framework (DRF)**. This project provides user authentication, profile management, and post management functionalities for a social media platform.
 
---

##  Features

### Authentication
- User Registration
- User Login
- JWT Authentication

### User Management
- Create User Accounts
- View User Profiles
- Update User Information

### Post Management
- Create Posts
- View Posts
- Update Posts
- Delete Posts
- List All Posts

### API Features
- RESTful Endpoints
- JSON Responses
- Serializer Validation
- Generic Class-Based Views
- Secure Authentication

---

##  Tech Stack

- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite
- Tailwind CSS

---

##  Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/social-media-api.git
cd social-media-api
```

### Create a Virtual Environment

#### Windows

```bash
python -m venv my_env
my_env\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create a Superuser

```bash
python manage.py createsuperuser
```

### Run the Development Server

```bash
python manage.py runserver
```

Open your browser and navigate to:

```text
http://127.0.0.1:8000/
```

---

## Example API Workflow

### 1. Register a User

```http
POST /api/register/
```

### 2. Login

```http
POST /api/login/
```

### 3. Create a Post

```http
POST /api/posts/
```

```json
{
  "title": "Learning Django",
  "content": "Building my first social media API."
}
```

---

##  Testing

You can test the API using:

- Postman
- Thunder Client
- Insomnia
- Django REST Framework Browsable API

---

##  Admin Dashboard

Access the admin dashboard at:

```text
http://127.0.0.1:8000/admin/
```

Login using the superuser credentials you created.


---

##  Learning Outcomes

This project demonstrates:

- Django Project Structure
- Django REST Framework
- JWT Authentication
- CRUD Operations
- API Design
- URL Routing
- Serializers
- Generic Views
- Database Migrations
- Secure API Development

---


##  Author

Natasha Bolyn