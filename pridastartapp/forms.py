from django import forms
from .models import Patients


class PreeclampsiaForm(forms.ModelForm):
    class Meta:
        model = Patients
        # fields = ['patient_id', 'name', 'years']
        fields = ['patient_id', 'name', 'years', 'probe_date', 'birth_date', 'arterial_pressure', 'gw', 'baby_weight',
                  'erythrocytes', 'hemoglobin']

