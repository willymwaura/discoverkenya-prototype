from django import forms
from .models import Map

class MeasurementModelForm(forms.ModelForm):
    class Meta:
        model = Map
        fields = ('destination',)