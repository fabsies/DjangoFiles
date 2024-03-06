from django.contrib import admin

from EmployeesModule.models import Employee, Registration, Next_of_kin

# Register your models here.
admin.site.register(Employee)
admin.site.register(Registration)
admin.site.register(Next_of_kin)
