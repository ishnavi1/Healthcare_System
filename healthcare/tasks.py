from celery import shared_task

@shared_task
def send_appointment_email():
    # Logic to send emails
    pass