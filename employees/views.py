from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Employee
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

#read function
@login_required(login_url='login')
def create(request):
    if request.method == "POST":
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        cnic = request.POST['cnic']
        email = request.POST['email']
        phone = request.POST['phone']

        Employee.objects.create(
            firstname=fname,
            lastname=lname,
            cnic=cnic,
            email=email,
            phone=phone
        )

        # Assuming the form is valid and the employee is added successfully
        messages.success(request, 'Employee added successfully.')
        return redirect("create")
    else:    
        return render(request, 'create.html')

#read function
@login_required(login_url='login')
def read(request):
    emp = Employee.objects.all()

    context = {
        "employees": emp
    }

    return render(request, 'read.html', context)

#edit function
@login_required(login_url='login')
def edit(request, pk):
    emp = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        cnic = request.POST['cnic']
        email = request.POST['email']
        phone = request.POST['phone']

        emp.firstname=fname
        emp.lastname=lname
        emp.cnic=cnic
        emp.email=email
        emp.phone=phone
    
        emp.save()

        return redirect("read")
    else:  
        context = {
            "emp": emp
        }
        return render(request, 'edit.html', context)
    
#delete function
@login_required(login_url='login')
def delete(request, pk):
    emp = get_object_or_404(Employee, pk=pk)
    emp.delete()
    messages.success(request, 'Employee deleted successfully.')

    return redirect("read")