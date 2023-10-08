from datetime import datetime, timedelta, time

from habit.models import Habit


def calculate_next_send_time(frequency, lead_time):
    """
    Calculates the next send time based on the given frequency and lead time.

    Args:
    - frequency: The frequency of the habit, represented by Habit.Frequency enum values.
    - lead_time: The lead time for the habit, indicating the time of day when the habit notification is sent.

    Returns:
    A datetime object representing the next scheduled time for habit notification.

    Raises:
    ValueError: If an unsupported frequency value is provided.
    """
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
