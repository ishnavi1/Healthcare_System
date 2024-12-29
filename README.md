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

markdown
Copy code
- Python 3.10 or later
- PostgreSQL
- Redis server
- Celery

# Installation

1. Clone the repository:
   git clone https://github.com/username/healthcare-project.git
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
2. Upload a file using Postman or cURL:
   
   curl -X POST -F "file=@path/to/file.csv" http://127.0.0.1:8000/upload-file/

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
   - Download the `postman_collection.json` file from the repository.
   - Open Postman and import the file.

2. API Endpoints:
   - `POST /api/upload-file/`: Upload a file for processing.
   - `GET /api/patients/`: Retrieve all patients.
   - `POST /api/doctors/`: Add a new doctor.
   - `GET /api/appointments/`: Retrieve all appointments.
