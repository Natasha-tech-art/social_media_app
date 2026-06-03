# Social Media App

A Django REST Framework-based social media application with user authentication, profile management, and post creation/management.

## Features

- **User Authentication**: JWT-based authentication with login and token refresh
- **User Profiles**: Create and manage user profiles with bio and profile pictures
- **User Search**: Search for users by username
- **Posts**: Create, read, update, and delete posts
- **Admin Panel**: Django admin interface for managing data

## Project Structure

```
social_media_app/
├── config/              # Django project settings
│   ├── settings.py      # Project settings
│   ├── urls.py          # Project URL routing
│   ├── wsgi.py          # WSGI configuration
│   └── asgi.py          # ASGI configuration
├── users/               # User management app
│   ├── models.py        # User model (extends AbstractUser)
│   ├── views.py         # User views (Register, Profile, Search)
│   ├── serializers.py   # User serializers
│   ├── urls.py          # User app URLs
│   └── migrations/      # Database migrations
├── posts/               # Post management app
│   ├── models.py        # Post model
│   ├── views.py         # Post views (List, Create, Detail, Update, Delete)
│   ├── serializers.py   # Post serializers
│   ├── urls.py          # Post app URLs
│   └── migrations/      # Database migrations
├── my_env/              # Python virtual environment
├── manage.py            # Django management script
├── db.sqlite3           # SQLite database
└── requirements.txt     # Python dependencies
```

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git (optional, for version control)

## Installation

1. **Clone the repository** (if using git):
   ```bash
   git clone <repository-url>
   cd social_media_app
   ```

2. **Create and activate a virtual environment**:
   ```bash
   # Windows
   python -m venv my_env
   my_env\Scripts\activate

   # macOS/Linux
   python3 -m venv my_env
   source my_env/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

## Running the Development Server

```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`

**Note**: Ensure your virtual environment is activated before running the server.

## API Endpoints

### Authentication
- `POST /api/login/` - Obtain JWT tokens
- `POST /api/refresh/` - Refresh JWT token

### Users
- `POST /api/register/` - Register a new user
- `GET /api/profiles/<id>/` - Get user profile
- `PUT /api/profiles/<id>/` - Update user profile
- `GET /api/search/users/?query=<search_term>` - Search users by username

### Posts
- `GET /api/posts/` - List all posts
- `POST /api/posts/` - Create a new post
- `GET /api/posts/<id>/` - Get post details
- `PUT /api/posts/<id>/` - Update a post
- `DELETE /api/posts/<id>/` - Delete a post

### Admin
- `GET /admin/` - Django admin interface

## Authentication

The API uses **JWT (JSON Web Token)** authentication. To authenticate:

1. **Login** to get tokens:
   ```bash
   POST /api/login/
   Body: {
     "username": "your_username",
     "password": "your_password"
   }
   ```

2. **Use the access token** in request headers:
   ```
   Authorization: Bearer <your_access_token>
   ```

3. **Refresh the access token** when it expires:
   ```bash
   POST /api/refresh/
   Body: {
     "refresh": "<your_refresh_token>"
   }
   ```

## Database Schema

### User Model
- `id` (Primary Key)
- `username` (Unique)
- `email` (Unique)
- `password` (Hashed)
- `bio` (Optional)
- `profile_picture` (Optional)

### Post Model
- `id` (Primary Key)
- `author` (Foreign Key to User)
- `title`
- `content`
- `created_at` (Timestamp)
- `updated_at` (Timestamp)

## Settings Configuration

### Key Settings in `config/settings.py`

- **DEBUG**: Set to `False` for production
- **ALLOWED_HOSTS**: Add your domain names
- **INSTALLED_APPS**: Includes Django apps and custom apps (users, posts)
- **MIDDLEWARE**: Security and session middleware configured
- **REST_FRAMEWORK**: JWT authentication enabled
- **AUTH_USER_MODEL**: Uses custom User model from users app
- **DATABASES**: SQLite configured (use PostgreSQL for production)
- **MEDIA_URL & MEDIA_ROOT**: For storing uploaded profile pictures

## Common Commands

```bash
# Run the server
python manage.py runserver

# Run system checks
python manage.py check

# Create migrations for model changes
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Create superuser for admin
python manage.py createsuperuser

# Access Django shell
python manage.py shell

# Collect static files (for production)
python manage.py collectstatic
```

## Troubleshooting

### Virtual Environment Not Activated
- **Error**: `ModuleNotFoundError: No module named 'rest_framework'`
- **Solution**: Activate the virtual environment first:
  ```bash
  # Windows
  my_env\Scripts\activate
  ```

### Database Errors
- **Error**: `sqlite3.OperationalError`
- **Solution**: Run migrations:
  ```bash
  python manage.py migrate
  ```

### Port Already in Use
- **Error**: `Address already in use (':8000')`
- **Solution**: Run on a different port:
  ```bash
  python manage.py runserver 8001
  ```

## Production Deployment

For production deployment:

1. Set `DEBUG = False` in settings.py
2. Add your domain to `ALLOWED_HOSTS`
3. Use a production WSGI server (Gunicorn, uWSGI)
4. Configure a production database (PostgreSQL recommended)
5. Set up HTTPS with SSL certificates
6. Use environment variables for sensitive settings
7. Configure static and media file serving

## Technology Stack

- **Backend**: Django 6.0.5
- **API**: Django REST Framework 3.17.1
- **Authentication**: djangorestframework-simplejwt 5.5.1
- **Database**: SQLite (development) / PostgreSQL (production)
- **Images**: Pillow 12.2.0

## License

[Add your license information here]

## Support

For issues or questions, please open an issue in the repository or contact the development team.

---

**Last Updated**: June 3, 2026
