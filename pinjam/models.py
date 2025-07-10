from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Barang(models.Model):
    """Model definition for Barang."""
    nama_barang     = models.CharField(max_length=64)
    stock           = models.IntegerField()
    # TODO: Define fields here

    class Meta:
        """Meta definition for Barang."""

        verbose_name = 'Barang'
        verbose_name_plural = 'Barangs'

    def __str__(self):
        """Unicode representation of Barang."""
        return f"{self.nama_barang}-{self.stock}"


class Pinjam(models.Model):
    """Model definition for Pinjam."""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('disetujui', 'Disetujui'),
        ('ditolak', 'Ditolak'),
        ('dikembalikan', "Dikembalikan"),
    ]

    # TODO: Define fields here
    karyawan    = models.ForeignKey(User, on_delete = models.CASCADE)
    barang      = models.ForeignKey(Barang, on_delete = models.CASCADE)
    tgl_pinjam  = models.DateTimeField(default=timezone.now)
    status      = models.CharField(
                        max_length=16, 
                        choices = STATUS_CHOICES,
                        default = 'pending' 
                    )

    class Meta:
        """Meta definition for Pinjam."""

        verbose_name = 'Pinjam'
        verbose_name_plural = 'Pinjams'


    def __str__(self):
        """Unicode representation of Pinjam."""
        return f"{self.karyawan}-{self.barang}-{self.status}"
