from django.shortcuts import render,HttpResponse,redirect
from msgapp1.models import Msg

# Create your views here.
def create(request):
    if request.method=="GET":
        return render(request,"create.html")
    else:
        n=request.POST['Uname']
        mail=request.POST['Email']
        mob=request.POST['mob']
        msg=request.POST['msg']
        print("Username is", n)
        print("UEmail id is", mail)
        print("Mobile number is", mob)
        print("Msg is", msg)
        m=Msg.objects.create(name=n,email=mail,mob=mob,msg=msg)
        m.save()
        #return HttpResponse("Data Inserted")
        return redirect('/dashboard')

def Dashboard(request):
    m=Msg.objects.all()
    #print(m)
    context={}
    context['data']=m
    return render(request,'dashboard.html',context)


def delete(request,rid):
    #print("ID is to be deleteed",rid)
    #return HttpResponse(""ID is to be deleteed"+rid")
    m=Msg.objects.filter(id=rid)
    m.delete()
    return redirect('/dashboard')



def edit(request,rid):
    if request.method=='GET':
        m=Msg.objects.get(id=rid)
        context={}
        context['data']=m
        return render(request,'edit.html',context)
    else:
        n=request.POST['Uname']
        mail=request.POST['Email']
        mob=request.POST['mob']
        msg=request.POST['msg']
        print("Username is", n)
        print("UEmail id is", mail)
        print("Mobile number is", mob)
        print("Msg is", msg)
        m=Msg.objects.create(name=n,email=mail,mob=mob,msg=msg)
        m.save()
        m=Msg.objects.filter(id=rid)
        m.delete()
        #return HttpResponse("Data Inserted")
        return redirect('/dashboard')
