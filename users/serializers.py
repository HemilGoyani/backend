from requests import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from users.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class LoginSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(LoginSerializer, cls).get_token(user)

        # Add custom claims
        token['email'] = user.email
        return token

queryset= User.objects.all()
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset)]
            )

    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password',},validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password',})

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password',)
        

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            
        )

        
        user.set_password(validated_data['password'])
        user.save()
        # return Response({"status": "success", "data": user.data})
        print("register successfull")
        return user
        