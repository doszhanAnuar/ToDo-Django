from rest_framework import serializers
from .models import *

class TodoSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Todo
        fields = ('id', 'name', 'discription', 'date', 'completed', 'user')