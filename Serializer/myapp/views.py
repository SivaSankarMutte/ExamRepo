from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework .response import Response
 

# Create your views here.

def home(request):
	return HttpResponse("<h1>welcome</h1>")

def article_list(request):
	if request.method=="GET":
		articles=Article.objects.all()
		print(articles)
		serializer=ArticleSerializer(articles,many=True)
		return JsonResponse(serializer.data,safe=False)

	elif request.method=="POST":
		data=JSONParser().parse(request)
		serializer=ArticleSerializer(data=data)

		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data,status=201)
		else:
			return JsonResponse(serializer.errors,status=400)
 
#class ArticleViewSet(viewsets.ViewSet):
#	def list(self,request):
#		articles=Article.objects.all()
#		serializer=ArticleSerializer(articles,many=True)
#		return Response(serializer.data)


class ArticleViewSet(viewsets.ModelViewSet):
	serializer_class=ArticleSerializer
	queryset=Article.objects.all()