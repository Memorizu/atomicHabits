from datetime import timedelta
from rest_framework import serializers


class RelatedOrRewardValidator:
    """
    Validator to ensure that 'related_habit' and 'reward' fields are not set together.
    Raises:
        serializers.ValidationError: If both 'related_habit' and 'reward' fields are provided.
    """
    def __call__(self, value):
        related_habit = value.get('related_habit', None)
        reward = value.get('reward', None)

        if related_habit and reward:
            raise serializers.ValidationError("You can't set related_habit and reward together")


class TimeToCompleteValidator:
    """
    Validator to ensure 'time_to_complete' is less than two minutes.
    Raises:
        serializers.ValidationError: If 'time_to_complete' is greater than or equal to two minutes.
    """
    def __call__(self, value):
        two_minutes = timedelta(minutes=2)
        time_to_complete_timedelta = timedelta(
            hours=value.hour,
            minutes=value.minute,
            seconds=value.second,
        )

        if time_to_complete_timedelta >= two_minutes:
            raise serializers.ValidationError("Time to complete must be less than two minutes.")


class IsPleasantRelatedValidator:
    """
    Validator to ensure that 'related_habit' is a pleasant habit (is_pleasant=True).
    Raises:
        serializers.ValidationError: If 'related_habit' is provided and is not pleasant (is_pleasant=False).
    """
    def __call__(self, value):
        if value and not value.is_pleasant:
            raise serializers.ValidationError("Related Habit must be pleasant")


class IsPleasantValidator:
    """
    Validator check is_pleasant field. If is_pleasant field is True - raises exception if existing related habit or reward.
    """

    def __call__(self, value):
        related_habit = value.get('related_habit', None)
        reward = value.get('reward', None)

        if value:
            if related_habit or reward:
                raise serializers.ValidationError("You cant set reward or related_habit on pleasant habit")
