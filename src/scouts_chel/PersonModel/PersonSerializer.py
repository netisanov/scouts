from rest_framework import serializers
from ..models import Gender, Person, TieChoices, PositionChoices


class PersonSerializer(serializers.Serializer):
    id = serializers.HyperlinkedRelatedField(view_name='person-detail', read_only=True)
    surname = serializers.CharField(max_length=30)
    name = serializers.CharField(max_length=30)
    patronymic = serializers.CharField(max_length=30)
    birthday = serializers.DateField()
    gender = serializers.ChoiceField(choices=Gender.choices, default=Gender.FEMALE)
    mother = serializers.HyperlinkedRelatedField(view_name='person-detail', read_only=True)
    father = serializers.HyperlinkedRelatedField(view_name='person-detail', read_only=True)
    children = serializers.HyperlinkedRelatedField(many=True,
                                                   view_name='person-detail',
                                                   read_only=True,
                                                   source='show_children')
    siblings = serializers.HyperlinkedRelatedField(many=True, view_name='person-detail', read_only=True)
    tie = serializers.ChoiceField(choices=TieChoices.choices, default=TieChoices.EMPTY)
    tie_date = serializers.DateField(required=False)
    is_staff = serializers.BooleanField(default=False)
    staff_date = serializers.DateField(required=False)
    position = serializers.ChoiceField(choices=PositionChoices.choices, default=PositionChoices.NULL)
    age = serializers.IntegerField(source='get_age', read_only=True)

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.patronymic = validated_data.get('patronymic', instance.patronymic)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.tie = validated_data.get('tie', instance.tie)
        instance.tie_date = validated_data.get('tie_date', instance.tie_date)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.staff_date = validated_data.get('staff_date', instance.staff_date)
        instance.position = validated_data.get('position', instance.position)
        instance.clean()
        instance.save()
        return instance
