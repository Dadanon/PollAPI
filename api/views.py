from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404

from polls.models import Question, Choice
from .serializers import (
    QuestionListSerializer,
    QuestionDetailSerializer,
    ChoiceSerializer,
    ChoiceListSerializer,
    VoteSerializer,
)


@api_view(['GET', 'POST'])
def questions_view(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionListSerializer(questions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = QuestionListSerializer(data=request.data)

        if serializer.is_valid():
            Question.objects.create(**serializer.validated_data)
            return Response('Question Created', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def question_detail_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'GET':
        serializer = QuestionDetailSerializer(question)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = QuestionDetailSerializer(question, data=request.data, partial=True)

        if serializer.is_valid():
            question = serializer.save()
            return Response(QuestionDetailSerializer(question).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        question.delete()
        return Response('Question deleted', status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def choices_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'GET':
        choices = Choice.objects.filter(question=question)
        serializer = ChoiceListSerializer(choices, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ChoiceSerializer(data=request.data)

        if serializer.is_valid():
            choice = serializer.save(question=question)
            return Response(ChoiceSerializer(choice).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def vote_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    serializer = VoteSerializer(data=request.data)

    if serializer.is_valid():
        choice = get_object_or_404(Choice, pk=serializer.validated_data['choice_id'], question=question)
        choice.votes += 1
        choice.save()
        return Response('Voted')
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
