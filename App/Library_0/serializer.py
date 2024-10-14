from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class bookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'



































class patientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'