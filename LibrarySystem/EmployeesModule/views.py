from django.shortcuts import render, redirect

from .forms import EmployeeForm, RegistrationForm, Next_of_kinForm
from .models import Employee


# Create your views here.
def employee_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, 'employee_form.html', {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
            return redirect('/employee/employee_list/')


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, 'employee_list.html', context)


def registration_form(request):
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'registration_form.html', {'form': form})
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_form')


def next_of_kin_form(request):
    if request.method == 'GET':
        form = Next_of_kinForm()
        return render(request, 'next_of_kin_form.html', {'form': form})
    else:
        form = Next_of_kinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('next_of_kin_form')


def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('employee/ employee_list/')
