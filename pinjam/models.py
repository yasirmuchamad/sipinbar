from django.db import models

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
        return f"(self.nama_barang)-(self.stock)"


class Pinjam(models.Model):
    """Model definition for Pinjam."""

    # TODO: Define fields here
    karyawan    = models.ForeignKey(Users, on_delete = models.CASCADE)
    barang      = models.ForeignKey(Barang, on_delete = Models.CASCADE)
    tgl_pinjam  = models.DateTimeField(default=Timezone.now)
    
    class Meta:
        """Meta definition for Pinjam."""

        verbose_name = 'Pinjam'
        verbose_name_plural = 'Pinjams'

    def __str__(self):
        """Unicode representation of Pinjam."""
        pass
