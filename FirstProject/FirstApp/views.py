from django.shortcuts import render,redirect
from django.http import HttpResponse
from FirstApp.models import Tour
from .models import Register

# Create your views here.
def home(request):
	return HttpResponse("Hi Welcome")

def htmltag(request):
	return HttpResponse("<h1>This is a heading</h1>")

def usernameprint(request,uname):
	return HttpResponse("<h1>Hi Welcome <span style='color:green'>{}</span></h1>".format(uname))
 
def favnum(request,n):
	return HttpResponse("<h1>Your Favourite number is:<span style='color:red'>{}</span></h2>".format(n))

def usernameage(request,un,ag):
	return HttpResponse("<h3 style='text-align:center; background-color:cyan; padding:23px;font-size:25px'>Name:<span style='color:orange'>{}</span> and Age:<span style='color:red'>{}</span></h3>".format(un,ag))

def empdetails(request,eid,eage,ename):
	return HttpResponse("<script>alert('Hi, Welcome {}')</script> Hi, Welcome {} and your age is:{} and your id is:{}</h3>".format(ename,ename,eage,eid))

def htm(request):
	return render(request,'ht1/first.html')

def ytname(request,name):
	return render(request,'ht1/ytname.html',{'n':name})

def empname(request,id,ename):
	d={'i':id,'n':ename}
	return render(request,'ht1/e.html',d)

def ownfun(request,nums):
	d={'numslist':nums}
	return render(request,'ht1/own.html',d)

def studentsdetails(request):
	return render(request,'ht1/std.html')

def alertfun(request):
	return render(request,'ht1/internaljs.html')

def myform(request):
	if request.method=="POST":
		#uname=request.POST['name']
		#print(uname)
		#print(request.POST)  this prints data in cmd 
		name=request.POST['name']
		regdno=request.POST['regdno']
		#email=request.POST['email'] or we can write using get() method POST is just a dictionary
		email=request.POST.get('email')
		#print(name,regdno,email)
		data={'name':name,'regdno':regdno,'email':email}
		return render(request,'ht1/formdetails.html',data)
	return render(request,'ht1/myform.html')

def myform2(request):
	if request.method=="POST":
		fname=request.POST['fname']
		lname=request.POST['lname']
		email=request.POST['email']
		phoneno=request.POST['phoneno']
		gender=request.POST['gender']
		address=request.POST['address']
		languages = request.POST.getlist('checks[]')
		sport=request.POST['sport']

		data={'fname':fname,'lname':lname,'email':email,'phoneno':phoneno,'gender':gender,'address':address,'languages':languages,'sport':sport}
		return render(request,'ht1/form2details.html',data)
	return render(request,'ht1/myform2.html')

def login(request):
	if request.method=='POST':
		if(request.POST['uname']=='siva' and request.POST['psw']=='siva'):
			uname=request.POST['uname']
			data={'uname':uname}
			return render(request,'ht1/success.html',data)
		else:
			return render(request,'ht1/error.html')
	return render(request,'ht1/login.html')

def bootstrapfun(request):
	return render(request,'ht1/usingbootstrap.html')

def btregi(request):
	return render(request,'ht1/btregst.html')

def sankarfun(request):
	return render(request,'ht1/sankar.html')

def bringerfun(request):
	if request.method=='POST':
		units=request.POST['inp']
		units=int(units)
		if(units<0):
		    rate=0 #Don't consider those case
		if(units<=100):
		    rate=1
		elif(units<=200):
		    rate=2
		elif(units<=300):
		    rate=3
		elif(units<=400):
		    rate=4
		else:
		    rate=5
		bill=units*rate
		data={'output':bill}
		return render(request,'ht1/output.html',data)
	return render(request,'ht1/bringer.html')

def PlayList(request):
	if request.method=="POST":
		if(request.POST['<']=='<'):
			return render(request,'ht1/song1.html')
		elif(request.POST['>']=='>'):
			return render(request,'ht1/song3.html')
	return render(request,'ht1/song2.html')

def TourFun(request):
	data=Tour.objects.all()
	return render("ht1/tour.html",{'data':data})

def register1(request):
	reg=Register(name=name,email=email)
	reg.save()
	return HttpResponse("<h1>Row inserted Successfully</h1>")

def register2(request):
	if request.method=="POST":
		name=request.POST['name']
		email=request.POST['email']
		reg=Register(name=name,email=email)
		reg.save()
		return display(request)
	return render(request,'ht1/registration.html')

def display(request):
	data=Register.objects.all()
	return render(request,'ht1/display.html',{'data':data})

def sview(request,y):
	row=Register.objects.get(id=y)
	#data={"id":row.id,"name":row.name,"email":row.email}
	#data={'data':row}
	return render(request,'ht1/displayRow.html',{'row':row})

def updateFun(request,y):
	row=Register.objects.get(id=y)
	if request.method=="POST":
		name=request.POST['name']
		email=request.POST['email']
		row.name=name
		row.email=email
		row.save()
		#Register.objects.update(row.name=request.POST['name'],row.email=request.POST['email'])
		#return display(request)
		return redirect('/display')
	#data={'name':row.name,'email':row.email}
	return render(request,'ht1/updating.html',{'row':row})

def saveDetails(request,y):
	if(request.method=="POST"):
		name=request.POST['name']
		email=request.POST['email']
		row=Register.objects.get(id=y)
		row.name=name
		row.email=email
		row.save()
		return display(request)

def deleteFun(request,y):
	row=Register.objects.get(id=y)
	if request.method=="POST":
		row.delete()
		return redirect('/display')
	return render(request,'ht1/deletesure.html',{'row':row})
