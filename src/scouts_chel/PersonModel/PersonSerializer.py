from rest_framework import serializers
from ..models import Gender, Person


class PersonSerializer(serializers.Serializer):
    id = serializers.HyperlinkedRelatedField(view_name='person-detail', read_only=True)
    name = serializers.CharField(max_length=30)
    surname = serializers.CharField(max_length=30)
    patronymic = serializers.CharField(max_length=30)
    birthday = serializers.DateField()
    gender = serializers.ChoiceField(choices=Gender.choices, default=Gender.FEMALE)

    def create(self, validated_data):
        return Person.objects.create(**validated_data)
