from.models import Users
from django import forms

class ClientForm(forms.ModelForm):
    class Meta:
        model=Users
        fields=('name','birthday','phone')

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Users
        fields=('name','birthday','phone','position')