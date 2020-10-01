from rest_framework import serializers
from polls.models import Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('choice_text', )


class QuestionSerializer(serializers.ModelSerializer):
    was_published_recently = serializers.BooleanField(read_only=True)

    class Meta:
        model = Question
        fields = '__all__'


class QuestionDetailSerializer(QuestionSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)


class VoteSerializer(serializers.Serializer):
    choice_id = serializers.IntegerField()
