from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validation_data):
        password = validation_data.pop('password', None)
        user = self.Meta.model(**validation_data)
        user.set_password(password)
        user.save()
        return user
