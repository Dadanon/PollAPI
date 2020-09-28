from rest_framework import serializers
from polls.models import Question


class QuestionSerializer(serializers.Serializer):
    question_text = serializers.CharField(max_length=200)
    pub_date = serializers.DateTimeField()
    was_published_recently = serializers.BooleanField(read_only=True)
    verbose_question_text = serializers.CharField(read_only=True)

    def create(self, validated_data):
        return Question.objects.create(**validated_data)
