from django import forms
from .models import Patients
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PreeclampsiaForm(forms.ModelForm):
    class Meta:
        model = Patients
        # fields = ['patient_id', 'name', 'years']
        fields = ['patient_id', 'name', 'years', 'probe_date', 'birth_date', 'arterial_pressure', 'gw', 'baby_weight',
                  'erythrocytes', 'hemoglobin']


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

