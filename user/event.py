from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar, SendUpdatesMode
from gcsa.recurrence import Recurrence, DAILY, SU, SA

from beautiful_date import Jan, Apr
from datetime import datetime

def create_event(doctor_email, patient_email, date, start_time):
    calendar = GoogleCalendar(credentials_path='credentials.json')

    event = Event(
        'Your Have an Appointment',
        start=datetime.combine(date, start_time),
        minutes_before_email_reminder=50,
        attendees=[doctor_email, patient_email]
    )

    calendar.add_event(event, send_updates=SendUpdatesMode.ALL)
