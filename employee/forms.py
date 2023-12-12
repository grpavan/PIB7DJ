from django import forms
from django.forms import ModelForm
from .models import Employee
class employeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ('emp_name','emp_email','emp_contact','emp_role','emp_salary')


