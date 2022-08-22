from django.shortcuts import render
from django.http import HttpResponse
from .models import members,admin_table,student,faculty
# Create your views here.
def login(request):
    if request.method=="POST":

        uname=request.POST['username']
        pwd=request.POST['password']
        who=request.POST.get('login')
        p=members.objects.all()
        print("here -1")
        print(uname)
        print(pwd)
        flag=0
        if(who=="Admin"):
            if(uname=="admin" and pwd=="admin"):
                 return index(request)
        else:
            for i in p:
                print("here")
                if(uname==i.name and pwd==i.password):
                    print("hlo")
                    flag=1
                    break

            if(flag==1):
                return index_others(request)
            else:   
              
                return render(request,"login.html",{'message':'Invalid Credentials'})
    else:
        return render(request,"login.html")
   
# def register(request):
#    return render(request,"registration.html")


def register(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        pwd=request.POST['pass']
        cont=request.POST['contact']
        dept=request.POST['dept']
        password1=request.POST['re_pass']
       
        if(password1==pwd):
            if(len(cont)==10):
                t=members.objects.create(name=name,email=email,password=pwd,phno=cont,dept=dept)
                t.save()
                return render(request,"login.html")
            else: 
                return render(request,"registration.html",{'message':'contact number should be of length 10'})
        else:
            return render(request,"registration.html",{'message':'password not matching'})        
             
        
    else:
        return render(request,"registration.html")



def index(request):
    # st=student.objects.all()
    # ft=faculty.objects.all()
    m4 = student.objects.filter(year="4")
    m3 = student.objects.filter(year="3")
    m2 = student.objects.filter(year="2")
    m1 = student.objects.filter(year="1")
    ynow=m4.count()+m3.count()+m2.count()+m1.count()
    ybef=m4.count()+m3.count()+m2.count()+20
    yfirst=m4.count()+m3.count()+20+30
    print(yfirst)
    print(ybef)
    print(ynow)
    f1=faculty.objects.filter(date__gte="2021-07-01" )
    f2=faculty.objects.filter(date__gte="2020-07-01" )
    f3=faculty.objects.filter(date__gte="2019-07-01" )
    print(f1.count())
    c1=(ynow)//(f1.count())
    c2=(ybef)//(f2.count())
    c3=(yfirst)//(f3.count())

    u11f=faculty.objects.filter(qualify="PhD")
    u121=faculty.objects.filter(date__gte="2020-07-01",qualify="PhD")
    u131=faculty.objects.filter(date__gte="2019-07-01",qualify="PhD")
    u211=faculty.objects.filter(date__gte="2021-07-01",qualify="MTECH")
    u221=faculty.objects.filter(date__gte="2020-07-01",qualify="MTECH")
    u231=faculty.objects.filter(date__gte="2019-07-01",qualify="MTECH")
    u331=faculty.objects.filter(date__gte="2021-07-01",qualify="BTECH")
    u332=faculty.objects.filter(date__gte="2020-07-01",qualify="BTECH")
    u333=faculty.objects.filter(date__gte="2019-07-01",qualify="BTECH")
    print(u11f.count())
    print(u121.count())
    

    count1=student.objects.all()
    u11=u11f.count()
    u12=u121.count()
    u13=u131.count()
    u22=u221.count()
    u23=u231.count()
    u21=u211.count()
    u31=u331.count()
    u32=u332.count()
    u33=u333.count()
    s1=u11+u21+24
    s2=u21+u22+u32+23
    s3=u31+u32+u33+30
    u11=6
    u12=10
    u13=10
    u23=10
    u21=10
    u21=10
    u22=3
    u32=10
    u31=10
    u32=10
    u33=10

    t1=(u11+u12+u13)//3
    t2=(u21+u22+u23)//3
    t3=(u31+u32+u33)//3
    tt=t1+t2+t3
    
    
    y=3
    z=20

    yo=(count1.count())//20
    if(yo==0):
        yo=30
    f11=(2*(((10*u11)+(4*u21))//yo))
    f22=(2*(((10*u12)+(4*u22))//yo))
    f33=(2*(((10*u13)+(4*u23))//yo))
    ft=(f11+f22+f33)/3
    per1=(f1.count()//yo)*100
    per2=(f2.count()//yo)*100
    per3=(f3.count()//yo)*100

    data1={
        "m4":m4.count(),
        "m3":m3.count(),
        "m2":m2.count(),
        "m1":m1.count(),
        "ynow":ynow,
        "ybef":ybef,
        "yfirst":yfirst,
        "f1":f1.count(),
        "f3":f3.count(),
        "f2":f2.count(),
        "c1":c1,
        "c2":c2,
        "c3":c3,
        "u11":u11,
        "u12":u12,
        "u13":u13,
        "u21":u21,
        "u22":u22,
        "u23":u23,
        "f11":f11,
        "f22":f22,
        "f33":f33,
        "ft":ft,
        "yo":yo,
        "per1":per1,
        "per2":per2,
        "per3":per3,
        
        "u31":u31,
        "u32":u32,
        "u33":u33,
        "y":y,
        "z":z,
        "s1":s1,
        "s2":s2,
        "s3":s3,
        "t1":t1,
        "t2":t2,
        "t3":t3,
        "tt":tt,



    }

    return render(request,"index.html",data1)    



def index_others(request):
    # st=student.objects.all()
    # ft=faculty.objects.all()
    m4 = student.objects.filter(year="4")
    m3 = student.objects.filter(year="3")
    m2 = student.objects.filter(year="2")
    m1 = student.objects.filter(year="1")
    ynow=m4.count()+m3.count()+m2.count()+m1.count()
    ybef=m4.count()+m3.count()+m2.count()+20
    yfirst=m4.count()+m3.count()+20+30
    print(yfirst)
    print(ybef)
    print(ynow)
    f1=faculty.objects.filter(date__gte="2021-07-01" )
    f2=faculty.objects.filter(date__gte="2020-07-01" )
    f3=faculty.objects.filter(date__gte="2019-07-01" )
    print(f1.count())
    c1=(ynow)//(f1.count())
    c2=(ybef)//(f2.count())
    c3=(yfirst)//(f3.count())

    u11f=faculty.objects.filter(date__gte="2021-07-01",qualify="PhD")
    u121=faculty.objects.filter(date__gte="2020-07-01",qualify="PhD")
    u131=faculty.objects.filter(date__gte="2019-07-01",qualify="PhD")
    u211=faculty.objects.filter(date__gte="2021-07-01",qualify="MTECH")
    u221=faculty.objects.filter(date__gte="2020-07-01",qualify="MTECH")
    u231=faculty.objects.filter(date__gte="2019-07-01",qualify="MTECH")
    u331=faculty.objects.filter(date__gte="2021-07-01",qualify="BTECH")
    u332=faculty.objects.filter(date__gte="2020-07-01",qualify="BTECH")
    u333=faculty.objects.filter(date__gte="2019-07-01",qualify="BTECH")

    count1=student.objects.all()
    u11=u11f.count()
    u12=u121.count()
    u13=u131.count()
    u22=u221.count()
    u23=u231.count()
    u21=u211.count()
    u31=u331.count()
    u32=u332.count()
    u33=u333.count()
    

    s1=u11+u21+24
    s2=u21+u22+u32+23
    s3=u31+u32+u33+30
    u11=6
    u12=10
    u13=10
    u23=10
    u21=10
    u21=10
    u22=3
    u32=10
    u31=10
    u32=10
    u33=10


    t1=(u11+u12+u13)//3
    t2=(u21+u22+u23)//3
    t3=(u31+u32+u33)//3
    tt=t1+t2+t3
    
    
    y=3
    z=20

    yo=(count1.count())//20
    if(yo==0):
        yo=30
    f11=(2*(((10*u11)+(4*u21))//yo))
    f22=(2*(((10*u12)+(4*u22))//yo))
    f33=(2*(((10*u13)+(4*u23))//yo))
    ft=(f11+f22+f33)/3
    per1=(f1.count()//yo)*100
    per2=(f2.count()//yo)*100
    per3=(f3.count()//yo)*100

    data1={
        "m4":m4.count(),
        "m3":m3.count(),
        "m2":m2.count(),
        "m1":m1.count(),
        "ynow":ynow,
        "ybef":ybef,
        "yfirst":yfirst,
        "f1":f1.count(),
        "f3":f3.count(),
        "f2":f2.count(),
        "c1":c1,
        "c2":c2,
        "c3":c3,
        "u11":u11,
        "u12":u12,
        "u13":u13,
        "u21":u21,
        "u22":u22,
        "u23":u23,
        "f11":f11,
        "f22":f22,
        "f33":f33,
        "ft":ft,
        "yo":yo,
        "per1":per1,
        "per2":per2,
        "per3":per3,
        
        "u31":u31,
        "u32":u32,
        "u33":u33,
        "y":y,
        "z":z,
        "s1":s1,
        "s2":s2,
        "s3":s3,
        "t1":t1,
        "t2":t2,
        "t3":t3,
        "tt":tt,



    }

    return render(request,"index2.html",data1)    




def addstudent(request):
    name=request.POST['name']
    id1=request.POST['id']
    email=request.POST['email']
    year=request.POST.get('year')
    branch=request.POST.get('branch')
    print(branch)
    r=student.objects.create(name=name,rollid1=id1,email=email,year=year,dept=branch)
    r.save()
     
    return index(request)  

def addfaculty(request):
    name=request.POST['name']
    id1=request.POST['id']
    email=request.POST['email']
    year=request.POST.get('year')
    branch=request.POST.get('branch')
    date=request.POST.get('date')
    print(date)
    m=faculty.objects.create(name=name,rollid=id1,email=email,year=year,dept=branch,date=date)
    m.save()

    return index(request) 


        
