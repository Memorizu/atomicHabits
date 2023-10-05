from datetime import datetime, timedelta, time

from habit.models import Habit


def calculate_next_send_time(frequency, lead_time):
    current_date = datetime.combine(lead_time.date(), time())

    if frequency == Habit.Frequency.EACH_HOUR:
        next_send_time = current_date + timedelta(hours=1)
    elif frequency == Habit.Frequency.DAILY:
        next_send_time = current_date + timedelta(days=1)
    elif frequency == Habit.Frequency.WEEKLY:
        next_send_time = current_date + timedelta(weeks=1)
    else:
        raise ValueError("Неподдерживаемая частота")
    return next_send_time
