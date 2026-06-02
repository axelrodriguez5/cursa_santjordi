from django.db import models


class Categoria(models.Model):
    nom = models.CharField(max_length=50)
    edat_minima = models.IntegerField()
    edat_maxima = models.IntegerField()
    distancia_km = models.DecimalField(max_digits=4, decimal_places=1)

    class Meta:
        ordering = ['edat_minima']

    def __str__(self):
        return f"{self.nom} ({self.edat_minima}-{self.edat_maxima} anys)"


class Participant(models.Model):
    nom = models.CharField(max_length=50)
    cognoms = models.CharField(max_length=100)
    dorsal = models.IntegerField(unique=True)
    email = models.EmailField()
    data_naixement = models.DateField()
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='participants'
    )
    temps_segons = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['dorsal']

    def __str__(self):
        return f"#{self.dorsal} {self.nom} {self.cognoms}"

    def temps_format(self):
        """Retorna el temps en format mm:ss"""
        if self.temps_segons is None:
            return "-"
        minuts = self.temps_segons // 60
        segons = self.temps_segons % 60
        return f"{minuts:02d}:{segons:02d}"
