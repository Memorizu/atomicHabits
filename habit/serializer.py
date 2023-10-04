import os

from rest_framework import serializers

from habit.models import Habit
from habit.validators import RelatedOrRewardValidator, TimeToCompleteValidator, IsPleasantRelatedValidator, \
    IsPleasantValidator


class HabitSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    related_habit = serializers.PrimaryKeyRelatedField(queryset=Habit.objects.all(), validators=[IsPleasantRelatedValidator()], required=False)
    time_to_complete = serializers.DateTimeField(validators=[TimeToCompleteValidator()])

    class Meta:
        model = Habit
        fields = (
            'owner',
            'place',
            'lead_time',
            'action',
            'is_pleasant',
            'related_habit',
            'frequency',
            'reward',
            'time_to_complete',
            'is_public',
        )
        validators = [RelatedOrRewardValidator(), IsPleasantValidator()]

    def create(self, validated_data):
        return Habit.objects.create(**validated_data)
