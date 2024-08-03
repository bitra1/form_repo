from django import forms
from testapp.models import StudentModel
class StudentForm(forms.ModelForm):
    name = forms.CharField()
    gmail = forms.EmailField()
    state = forms.CharField()
    phonenumber = forms.IntegerField()
    dob = forms.DateField()
    gender = forms.CharField()
    class Meta:
        model = StudentModel
        fields = '__all__'
