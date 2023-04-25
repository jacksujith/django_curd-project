from django.shortcuts import render,HttpResponse,redirect
from blogapps.forms import StudentForm
from blogapps.models import Student

# Create your views here.
def index (request):
    obj = Student.objects.all()
    return render(request,'index.html',{'data':obj})

def create (request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
         form.save()
        return redirect('/')
        return redirect('create')
    else:
         form = StudentForm()
    context={'form':form}
    return render(request,'create.html',context)

def delete (request,id):
    obj = Student.objects.get(id=id)
    obj.delete()
    return redirect("/")
    return render(request,'delete.html')

def  update (request,id):
    obj = Student.objects.get(id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=obj)
        if form.is_valid():
          form.save()
        return redirect('/')
        return redirect('update ')
    else:
         form = StudentForm()
    context={'form':form}
    return render(request,'update.html',context) 
   