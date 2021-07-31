"""FirstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
""" 
from django.contrib import admin
from django.urls import path
from FirstApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('ht/',views.htmltag),
    path('usr/<str:uname>/',views.usernameprint),
    path('usrnum/<int:n>/',views.favnum),
    path('usag/<str:un>/<int:ag>/',views.usernameage),
    path('emp/<str:eid>/<int:eage>/<str:ename>/',views.empdetails),
    path('qw/',views.htm),
    path('yt/<str:name>/',views.ytname),
    path('pt/<int:id>/<str:ename>/',views.empname),
    path('stud/',views.studentsdetails),
    path('alert/',views.alertfun),
    path('myform/',views.myform,name='myform'),
    path('myform2/',views.myform2,name='myform2'),
    path('login/',views.login,name='login'),
    path('btstrp/',views.bootstrapfun),
    path('btrg/',views.btregi,name="btr"),
    path('sankar/',views.sankarfun),
    path('bringer/',views.bringerfun,name="output"),
    path('songs/',views.PlayList,name="songs"),
    path('tour/',views.TourFun),
    path('register1/',views.register1),
    path('register2/',views.register2,name="register2"),
    path('display/',views.display,name="display"),
    path('viw/<int:y>/',views.sview,name="sv"),
    path('update/<int:y>/',views.updateFun,name="update"),
    path('delete/<int:y>/',views.deleteFun,name="delete"),
    path('saveDetails/<int:y>/',views.saveDetails,name="saveDetails"),
    

] 
