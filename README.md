# Healthcare_System
A Django-based Healthcare Management System with PostgreSQL, optimized queries, Celery-powered file uploads, and comprehensive API documentation for easy setup and use.

# Project Overview
# Healthcare Project

This project is a healthcare management system built with Django. It allows users to manage patients, doctors, and appointments and supports large file uploads with Celery for background task processing.

Key Features:
- Patient, Doctor, and Appointment management
- Large file uploads handled with Celery
- Optimized database queries with select_related and prefetch_related
- Redis caching for performance

# Project Setup

System Requirements
List the prerequisites for running the project.
- Python 3.10 or later
- PostgreSQL
- Redis server
- Celery

# Installation

1. Clone the repository:
   git clone https://github.com/ishnavi1/Healthcare_System.git
   cd healthcare-project
2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install the dependencies:
   pip install -r requirements.txt

4. Set up the database:
   Install PostgreSQL and create a database (e.g., healthcare_db).
   Update settings.py with your database credentials.
5. Apply migrations:
   python manage.py makemigrations
   python manage.py migrate
6. Start the Redis server:
   redis-server
7. Run the development server:
   python manage.py runserver
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'healthcare_db',
        'USER': 'h_user',
        'PASSWORD': '123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'healthcare',
    'rest_framework',
    'django_celery_results',
]

# Running Background Tasks with Celery
1. Start the Celery worker:
   celery -A healthcare_project worker --loglevel=info
   Start the Celery beat scheduler (if periodic tasks are required):
   celery -A healthcare_project beat --loglevel=info
2. Verify that tasks are processed:
3. Use the Celery worker logs to confirm task execution.
4. Example:
  Task healthcare.tasks.process_file_task completed.

# File Uploads with Celery
- Large files are uploaded via the `POST /upload-file/` endpoint.
- Celery processes the file asynchronously to prevent blocking the server.
To test the feature:
1. Start the Django server, Redis server, and Celery worker.
2. Upload a file using Postman:
   
   curl -X POST -F "file=@path/to/test_data.csv" http://127.0.0.1:8000/upload-file/

# Troubleshooting

1. Redis Connection Error:
   - Ensure the Redis server is running: `redis-server`.
   - Verify the Redis configuration in `settings.py`.

2. File Upload Not Processed:
   - Ensure the Celery worker is running: `celery -A healthcare_project worker`.

3. Database Issues:
   - Check database connectivity and credentials in `settings.py`.

# Additional Notes

- Ensure your `.env` file is correctly configured for sensitive settings like `DATABASE_URL`, `REDIS_URL`, and `SECRET_KEY`.
- Use `DEBUG=False` in production to enhance security.

# Using Postman Collection

# API Documentation

1. Import the Postman collection:
   - Download the `Healthcare System.postman_collection.json` file from the repository.
   - Open Postman and import the file.

2. API Endpoints:
   - `POST /api/upload-file/`: Upload a file for processing.
   - `GET /api/patients/`: Retrieve all patients.
   - `POST /api/doctors/`: Add a new doctor.
   - `GET /api/appointments/`: Retrieve all appointments.

# Redis Caching Setup
Step 1: Configure Redis in settings.py
In your Django project's settings.py file, configure Redis for caching. Add the following configuration to the file:

1. settings.py

Caching Configuration
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',  # Redis URL (127.0.0.1 is default)
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
    }
}

CACHE_TTL = 60 * 15  # Cache data for 15 minutes

This configures Django to use Redis as the cache backend, where data will be cached in Redis for 15 minutes.

2. Implement Caching in Views
In your app's views.py, use caching for frequently queried data, like patient information or doctor lists. Below is an example for caching patient data:

- views.py

- from django.core.cache import cache
- from .models import Patient

def get_patient_data(request, patient_id):
    cache_key = f"patient_{patient_id}"
    patient_data = cache.get(cache_key)

    if not patient_data:
        patient_data = Patient.objects.get(id=patient_id)
        cache.set(cache_key, patient_data, timeout=60*15)  # Cache for 15 minutes

    return render(request, 'patient_detail.html', {'patient': patient_data})
In this example:

We check if the patient data is already cached using cache.get().
If the data is not cached, it is fetched from the database and stored in the cache for 15 minutes with cache.set().
Usage
Run the Django Development Server: Start your Django server to begin using Redis caching.

- python manage.py runserver
Access the App:

Visit http://127.0.0.1:8000/ to start interacting with the healthcare system.
Caching is applied to frequently queried data such as patient and doctor details.
Testing Redis Cache
You can test Redis caching by checking if the data is being cached correctly. Use the Django shell to verify cache functionality.

Enter Django Shell:

python manage.py shell
Test Cache: Try setting and getting a value in the cache to confirm that Redis is working correctly.

1. from django.core.cache import cache

2. Set a cache key-value pair
cache.set('test_key', 'test_value', timeout=60)

3. Get the cached value
print(cache.get('test_key'))  # Output: 'value'