from django.urls import path,include
from . import views
from .views import article_list
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('article',ArticleViewSet,basename='article')

urlpatterns = [
    path('',views.home),
    path('article/',article_list),
    path('viewset/',include(router.urls)),
    #path('art/',ArticleViewSet),
]