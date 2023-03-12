from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse

from json import dumps

from .models import *
from . import serializers

from rest_framework.decorators import api_view


@api_view(['GET'])
def get_all_posts(request):
    qs = Post.objects.all()
    serializer = serializers.PostSerializer(qs, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def get_one_post(request, pk):
    try:
        qs = Post.objects.get(id=pk)
        serializer = serializers.PostSerializer(qs)
        return Response(serializer.data, status=200)
    except Post.DoesNotExist:
        return Response(f'Post with that "ID={pk}" does not exist!', status=404)


@api_view(['GET'])
def get_all_users(request):
    qs = Person.objects.all()
    serializer = serializers.PersonSerializer(qs, many=True)
    return Response(serializer.data, status=200)


@api_view(['POST'])
def create_person(request):
    serializer = serializers.PersonCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)


@api_view(['POST'])
def create_comment(request):
    serializer = serializers.CommentSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)


@api_view(['POST'])
def create_post(request):
    serializer = serializers.PostCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)
