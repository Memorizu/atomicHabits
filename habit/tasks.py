from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from bots.telegram_bot import bot
from habit.models import Habit
from habit.services import calculate_next_send_time


@shared_task
def send_notification():
    """
    Celery task to send habit notifications to users.

    This task runs periodically and checks the habits of users with associated chat IDs.
    If the lead time for a habit is overdue by more than 5 minutes, a notification message
    is sent to the user reminding them to perform the habit.

    The lead time of updated habits is adjusted, and the habit objects are bulk updated.

    """
    now_time = timezone.now() + timedelta(hours=3)

    habits_with_users = Habit.objects.filter(owner__chat_id__isnull=False).prefetch_related('owner')
    habits_to_update = []

    for habit in habits_with_users:
        next_send_time = calculate_next_send_time(habit.frequency, habit.lead_time)

        if habit.lead_time < now_time - timedelta(minutes=5):

            message = f'Через 5 минут необходимо выполнять вашу привычку! ' \
                      f'Вам необходимо выполнить: {habit.action} ' \
                      f'После этого вы сможете вознаградить себя: {habit.reward if habit.reward else habit.related_habit}'
            bot.send_message(chat_id=habit.owner.chat_id, text=message)

            habit.lead_time = next_send_time
            habit.save()
            habits_to_update.append(habit)

    Habit.objects.bulk_update(habits_to_update, ['lead_time'])
