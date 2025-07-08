from django import forms
from .models import *

class BarangForm(forms.ModelForm):
    """Form definition for Barang."""

    class Meta:
        """Meta definition for Barangform."""

        model = Barang
        fields = '__all__'

