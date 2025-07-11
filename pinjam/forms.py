from django import forms
from .models import *

class BarangForm(forms.ModelForm):
    """Form definition for Barang."""

    class Meta:
        """Meta definition for Barangform."""

        model = Barang
        fields = '__all__'

class PinjamForm(forms.ModelForm):
    """Form definition for Pinjam."""

    class Meta:
        """Meta definition for Pinjamform."""

        model = Pinjam
        fields = ['barang']

    def __init__(self, *args, **kwargs):
        super(PinjamForm, self).__init__(*args, **kwargs)
        # self.fields['karyawan'].widget.attrs.update({'id':'karyawan', 'name':'karyawan', 'class':'form-control'})
        self.fields['barang'].widget.attrs.update({'id':'barang', 'name':'barang', 'class':'form-control'})
        # self.fields['tgl_pinjam'].widget.attrs.update({'id':'tgl_pinjam', 'name':'tgl_pinjam', 'class':'form-control'})
        # self.fields['status'].widget.attrs.update({'id':'status', 'name':'status', 'class':'form-control'})

