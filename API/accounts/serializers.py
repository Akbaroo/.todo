from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

UserModel = get_user_model()


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(UserModel.objects.all())],
    )
    password = serializers.CharField(required=True)
    password1 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = UserModel
        fields = ['id', 'username', 
                  'email', 'last_name', 'first_name',
                  'password', 'password1'
]
        extra_kwargs = {
            'last_name':{'required':False},
            'first_name':{'required':False},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password1']:
            raise serializers.ValidationError({
                'password': "password did not match."
            })
        
        if len(attrs['password']) < 8:
            raise serializers.ValidationError({
                'password': 'This password is too short. It must contain at least'
                    })
        
        if attrs['password'].isdigit():
            raise serializers.ValidationError({
                'password': "Your password can’t be entirely numeric."
            })
        
        return super().validate(attrs)
    
    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data.get('first_name', ''),
            last_name = validated_data.get('last_name', ''),
            password=validated_data['password']
        )
        return user