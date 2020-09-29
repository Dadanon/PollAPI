from rest_framework import serializers
from polls.models import Question, Choice


class ChoiceSerializer(serializers.Serializer):
    choice_text = serializers.CharField(max_length=200)

    def __str__(self):
        return self.choice_text

    def create(self, validated_data):
        return Choice.objects.create(**validated_data)


class ChoiceListSerializer(ChoiceSerializer):
    id = serializers.IntegerField()
    votes = serializers.IntegerField()


class QuestionListSerializer(serializers.Serializer):
    question_text = serializers.CharField(max_length=200)
    pub_date = serializers.DateTimeField()
    was_published_recently = serializers.BooleanField(read_only=True)
    verbose_question_text = serializers.CharField(read_only=True)

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class QuestionDetailSerializer(QuestionListSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)


class VoteSerializer(serializers.Serializer):
    choice_id = serializers.IntegerField()
