from rest_framework import serializers

# makes password in non-readable format
from django.contrib.auth.hashers import make_password

# decorators helps us to write something to pre written codes
from rest_framework.decorators import authentication_classes, permission_classes

from .models import CustomUser

class UserSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        # validated_data is key_value pair
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            # for the first time always use set password
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)

        instance.save()
        return instance

    class Meta:
        model = CustomUser
        # extra_kwargs which are hindered from database
        extra_kwargs = {'password': {'write_only': True}}
#       is_active , is_staff , is_superuser are the variables inherited from class
        fields = ('name', 'email', 'password', 'phone', 'gender',
                  'is_active', 'is_staff', 'is_superuser')