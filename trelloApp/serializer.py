from rest_framework import serializers
from .models import UserModel,BoardModel,ListModel,TaskModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardModel
        fields = '__all__'

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListModel
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = '__all__'