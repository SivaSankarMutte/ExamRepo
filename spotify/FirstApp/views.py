from django.shortcuts import render
from django.http import HttpResponse
from FirstApp.models import Songs
from FirstApp.models import Users

# Create your views here.
def home(request):
	return HttpResponse("HELLO")
def songs(request):
	dbdata=Songs.objects.all()
	data={}
	for row in dbdata: 
		new={}
		new['id1']=row.id 
		new['song']=row.song
		new['img']=row.album
		data[row.id]=new
	first_song=Songs.objects.all().first()
	last_song=Songs.objects.all().last()
	first_song_num=first_song.id
	last_song_num=last_song.id
	n=first_song_num
	dictToPass=data.get(n)
	if(request.method=="POST"):
		n=int(request.POST['currentSongNum'])
		if(request.method=="POST" and n!=last_song_num):
			n=n+1
			dictToPass=data.get(n)
			return render(request,'ht1/songs.html',dictToPass)
		elif(request.method=="POST" and n==last_song_num):
			n=first_song_num
			dictToPass=data.get(n)
			return render(request,'ht1/songs.html',dictToPass)


	return render(request,'ht1/songs.html',dictToPass)

def jqfun(request):
	return render(request,'ht1/jq.html')

def Registration(request):
	if request.method=="POST":
		name=request.POST['name']
		email=request.POST['email']
		phoneno=request.POST['phoneno']
		gender=request.POST['gender']
		dob=request.POST['dob']
		nickname=request.POST['nickname']
		psw=request.POST['psw']
		
		user=Users.objects.create(name=name,email=email,phoneno=phoneno,gender=gender,dob=dob,nickname=nickname,psw=psw)
		return render(request,'ht1/login.html')
	return render(request,'ht1/registration.html')

def Login(request):
	if request.method=="POST":
		email=request.POST['email']
		psw=request.POST['psw']

		dbdata=Users.objects.all()
		for row in dbdata:
			if(row.email==email and row.psw==psw):
				return display(request)
		return render(request,'ht1/login.html')
	return render(request,'ht1/login.html')

def music(request,sid):
	row=Songs.objects.get(id=sid)
	data={'song':row.song}

def display(request):
	data=Songs.objects.all()
	data={'data':data}
	return render(request,'ht1/display.html',data)

