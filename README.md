# Healthcare_System
A Django-based Healthcare Management System with PostgreSQL, optimized queries, Celery-powered file uploads, and comprehensive API documentation for easy setup and use.

1. Project Overview
# Healthcare Project

This project is a healthcare management system built with Django. It allows users to manage patients, doctors, and appointments and supports large file uploads with Celery for background task processing.

Key Features:
- Patient, Doctor, and Appointment management
- Large file uploads handled with Celery
- Optimized database queries with select_related and prefetch_related
- Redis caching for performance

2. Project Setup
System Requirements
List the prerequisites for running the project.

markdown
Copy code
- Python 3.10 or later
- PostgreSQL
- Redis server
- Celery
Installation Instructions
Provide step-by-step instructions for setting up the project locally.

markdown
Copy code
# Installation

1. Clone the repository:
   git clone https://github.com/username/healthcare-project.git
   cd healthcare-project
Create and activate a virtual environment:


python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the dependencies:


pip install -r requirements.txt
Set up the database:

Install PostgreSQL and create a database (e.g., healthcare_db).
Update settings.py with your database credentials.
Apply migrations:


python manage.py makemigrations
python manage.py migrate
Start the Redis server:


redis-server
Run the development server:


python manage.py runserver


# 3. API Documentation

# 4. Running Background Tasks with Celery

# Running Background Tasks with Celery

1. Start the Celery worker:
   
   celery -A healthcare_project worker --loglevel=info
Start the Celery beat scheduler (if periodic tasks are required):

celery -A healthcare_project beat --loglevel=info
Verify that tasks are processed:

Use the Celery worker logs to confirm task execution.
Example:
arduino
 Task healthcare.tasks.process_file_task completed.

# 5. File Uploads with Celery

# File Uploads

- Large files are uploaded via the `POST /upload-file/` endpoint.
- Celery processes the file asynchronously to prevent blocking the server.

To test the feature:
1. Start the Django server, Redis server, and Celery worker.
2. Upload a file using Postman or cURL:
   
   curl -X POST -F "file=@path/to/file.csv" http://127.0.0.1:8000/upload-file/


# 6. Troubleshooting

# Troubleshooting

1. Redis Connection Error:
   - Ensure the Redis server is running: `redis-server`.
   - Verify the Redis configuration in `settings.py`.

2. File Upload Not Processed:
   - Ensure the Celery worker is running: `celery -A healthcare_project worker`.

3. Database Issues:
   - Check database connectivity and credentials in `settings.py`.

# 7. Additional Notes

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
{
	"info": {
		"_postman_id": "57b409fa-4e8f-46f0-adcd-c4f401b5a54e",
		"name": "Healthcare System",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "34788421"
	},
	"item": [
		{
			"name": "Obtain a Token",
			"request": {
				"auth": {
					"type": "bearer",
					"bearer": [
						{
							"key": "token",
							"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM1NDY2NzU3LCJpYXQiOjE3MzU0NjY0NTcsImp0aSI6IjkwYmY4YzQ5OTk1YjRmMDU4MDIyNmQ3NDg3NDA5MGFlIiwidXNlcl9pZCI6MX0.qhXfSP6m4oY6tw7vUw3YImZLrhTDK_43pYg7a6H4i5A",
							"type": "string"
						}
					]
				},
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"username\": \"sai\",\r\n    \"password\": \"Sanjivani@601\"\r\n}\r\n",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/api/token/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"token",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Get All Patients",
			"request": {
				"auth": {
					"type": "bearer",
					"bearer": [
						{
							"key": "token",
							"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM1NDY2NDEyLCJpYXQiOjE3MzU0NjYxMTIsImp0aSI6ImQ5Yjg5YmM5ZTNiYzRhYjk5ZWMyZDk3ZjU5YjZhMzY4IiwidXNlcl9pZCI6MX0.KGIKWvYBAzIfgMCOYaos9uYydDXO0blbd7hsmIZJiSE",
							"type": "string"
						}
					]
				},
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:8000/api/patients/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"patients",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Create a New Patient",
			"request": {
				"auth": {
					"type": "bearer",
					"bearer": [
						{
							"key": "token",
							"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM1NDY2NDEyLCJpYXQiOjE3MzU0NjYxMTIsImp0aSI6ImQ5Yjg5YmM5ZTNiYzRhYjk5ZWMyZDk3ZjU5YjZhMzY4IiwidXNlcl9pZCI6MX0.KGIKWvYBAzIfgMCOYaos9uYydDXO0blbd7hsmIZJiSE",
							"type": "string"
						}
					]
				},
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"user\": 1,\r\n    \"dob\": \"1990-01-01\",\r\n    \"contact_number\": \"1234567890\"\r\n}\r\n",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/api/patients/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"patients",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Update a Patient",
			"request": {
				"auth": {
					"type": "bearer",
					"bearer": [
						{
							"key": "token",
							"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM1NDY2NDEyLCJpYXQiOjE3MzU0NjYxMTIsImp0aSI6ImQ5Yjg5YmM5ZTNiYzRhYjk5ZWMyZDk3ZjU5YjZhMzY4IiwidXNlcl9pZCI6MX0.KGIKWvYBAzIfgMCOYaos9uYydDXO0blbd7hsmIZJiSE",
							"type": "string"
						}
					]
				},
				"method": "PUT",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"user\": 1,\r\n    \"dob\": \"1991-01-01\",\r\n    \"contact_number\": \"9876543210\"\r\n}\r\n",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/api/patients/1/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"patients",
						"1",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Delete a Patient",
			"request": {
				"auth": {
					"type": "bearer",
					"bearer": [
						{
							"key": "token",
							"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM1NDY2NzU3LCJpYXQiOjE3MzU0NjY0NTcsImp0aSI6IjkwYmY4YzQ5OTk1YjRmMDU4MDIyNmQ3NDg3NDA5MGFlIiwidXNlcl9pZCI6MX0.qhXfSP6m4oY6tw7vUw3YImZLrhTDK_43pYg7a6H4i5A",
							"type": "string"
						}
					]
				},
				"method": "DELETE",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:8000/api/patients/1/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"patients",
						"1",
						""
					]
				}
			},
			"response": []
		}
	]
}