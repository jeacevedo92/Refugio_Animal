from django import forms

from apps.mascota.models import Mascota

class MascotaForm(forms.ModelForm):

    #def __init__(self, *args, **kwargs):
     #   super(MascotaForm, self).__init__(*args, **kwargs)
      #  self.fields['nombre'].widget.attrs['class'] = 'form-control'



    class Meta:
        model = Mascota

        fields = [
            'nombre',
            'sexo',
            'edad',
            'fecha_rescate',
            'persona',
            'vacuna',
        ]

        labels = {
            'nombre': 'Nombre',
            'sexo': 'Sexo',
            'edad': 'Edad Aproximada',
            'fecha_rescate': 'Fecha de rescate',
            'persona': 'Adoptante',
            'vacuna': 'Vacunas',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_rescate': forms.TextInput(attrs={'class': 'form-control'}),
            'persona': forms.Select(attrs={'class': 'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple(),
        }
