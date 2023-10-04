from django.urls import reverse
from rest_framework import status

from habit.models import Habit
from habit.tests.base import BaseTestCase


class HabitTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.not_pleasant_data = {
            'owner': 1,
            'place': 'home',
            'lead_time': '2023-10-03T23:56:48',
            'action': 'test',
            'is_pleasant': False,
            'frequency': 'daily',
            'reward': 'reward',
            'time_to_complete': '2023-10-03T00:01:48',
            'is_public': False,
        }
        self.validation_error_data = {
            'owner': 1,
            'place': 'home',
            'lead_time': '2023-10-03T23:56:48',
            'action': 'test',
            'is_pleasant': False,
            'frequency': 'daily',
            'related_habit': 1,
            'reward': 'reward',
            'time_to_complete': '2023-10-03T00:01:48',
            'is_public': False,
        }

    def test_create(self):
        habit_create = reverse('habit:habit-list')
        response = self.client.post(habit_create, self.not_pleasant_data, format='json', **self.headers)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['place'], self.not_pleasant_data['place'])

    def test_create_negative(self):
        habit_create = reverse('habit:habit-list')
        response = self.client.post(habit_create, self.validation_error_data, format='json', **self.headers)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('related_habit', response.json())

    def test_retrieve(self):
        habit = Habit.objects.create(
            owner=self.user,
            place='home',
            lead_time='2023-10-03T23:56:48',
            action='test',
            is_pleasant=False,
            frequency='daily',
            reward='reward',
            time_to_complete='2023-10-03T00:01:48',
            is_public=False,
        )
        habit_retrieve = reverse('habit:habit-detail', kwargs={'pk': habit.pk})
        response = self.client.get(habit_retrieve)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update(self):
        habit = Habit.objects.create(
            owner=self.user,
            place='home',
            lead_time='2023-10-03T23:56:48',
            action='test',
            is_pleasant=False,
            frequency='daily',
            reward='reward',
            time_to_complete='2023-10-03T00:01:48',
            is_public=False,
        )
        new_place = {'place': 'bridge'}
        habit_update = reverse('habit:habit-detail', kwargs={'pk': habit.pk})

        response = self.client.patch(habit_update, new_place, format='json', **self.headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['place'], 'bridge')

    def test_delete(self):
        habit = Habit.objects.create(
            owner=self.user,
            place='home',
            lead_time='2023-10-03T23:56:48',
            action='test',
            is_pleasant=False,
            frequency='daily',
            reward='reward',
            time_to_complete='2023-10-03T00:01:48',
            is_public=False,
        )
        habit_delete = reverse('habit:habit-detail', kwargs={'pk': habit.pk})
        response = self.client.delete(habit_delete)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
