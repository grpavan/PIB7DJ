from django.shortcuts import render,redirect
from .models import Employee
from .forms import employeeForm

# Create your views here.
def list(request):
    employees= Employee.objects.all()
    context= {'employees':employees}
    return render(request,'list.html',context)
def create(request):
    form=employeeForm
    if request.method == 'POST':
        form=employeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create.html')
    context = {'form':form}
    return render(request,'create.html',context)
def edit(request,pk):
    employee=Employee.objects.get(id=pk)
    form=employeeForm(instance=employee)
    if request.method =='POST':
        form=employeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect("list.html")
    context={'form':form}
    return render(request,'edit.html',context)
def delete(request):
    employee = Employee.objects.get(id=pk)
    form = employeeForm(instance=employee)
    if request.method == 'POST':
        form = employeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.delete()
            return redirect("list.html")
        context = {'form': form}
        return render(request, 'delete.html', context)


def home(request,pk):
    return render(request,'home.html')

