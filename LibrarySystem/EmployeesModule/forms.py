from EmployeesModule.models import Employee, Registration, Next_of_kin
from django import forms


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['fullname', 'email', 'emp_code', 'mobile_no', 'position']


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['first_name', 'last_name', 'phone_no', 'password']


class Next_of_kinForm(forms.ModelForm):
    class Meta:
        model = Next_of_kin
        fields = ['fullname', 'employee_name', 'ID_no', 'phone_no']
