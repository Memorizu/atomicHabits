from rest_framework import serializers

from habit.models import Habit
from habit.validators import RelatedOrRewardValidator, TimeToCompleteValidator, \
    IsPleasantRelatedValidator, IsPleasantValidator


class HabitSerializer(serializers.ModelSerializer):
    """
    Serializer for Habit objects.

    Fields:
    - owner: The user who owns the habit. Automatically set to the current authenticated user.
    - place: The location associated with the habit (string).
    - lead_time: The time of day when the habit notification is sent (datetime).
    - action: The action to be performed as part of the habit (string).
    - is_pleasant: A boolean indicating whether the habit is pleasant or not.
    - related_habit: Another habit related to the current habit (optional). Should be a valid Habit object ID.
    - frequency: The frequency of the habit, represented as an enum value.
    - reward: The reward associated with completing the habit (string).
    - time_to_complete: The date and time by which the habit should be completed (datetime).
    - is_public: A boolean indicating whether the habit is public or private.

    Validators:
    - is_pleasant: Validates whether the habit is marked as pleasant or not.
    - related_habit: Validates if the related habit is pleasant.
    - time_to_complete: Validates the completion time to be in the future.
    - related_or_reward: Validates either a related habit or a reward is provided, not both.

    Methods:
    - create(self, validated_data): Creates a new Habit instance with the provided validated data.

    Note: 'validators' option in Meta class specifies custom validation logic for the serializer.
    """
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    related_habit = serializers.PrimaryKeyRelatedField(
        queryset=Habit.objects.all(),
        validators=[IsPleasantRelatedValidator()],
        required=False)
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
