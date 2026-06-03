"""
Models de l'aplicació Cursa Sant Jordi.
Defineix les taules de la base de dades com a classes de Python (ORM de Django).
"""
from django.db import models


# ============================================================
# MODEL CATEGORIA
# Representa una categoria de la cursa (Infantil, Juvenil, Adult...)
# Cada categoria té un rang d'edats i una distància concreta.
# ============================================================
class Categoria(models.Model):
    nom = models.CharField(max_length=50)          # Nom de la categoria
    edat_minima = models.IntegerField()            # Edat mínima per participar
    edat_maxima = models.IntegerField()            # Edat màxima per participar
    distancia_km = models.DecimalField(max_digits=4, decimal_places=1)  # Distància en km

    class Meta:
        # Ordena automàticament les categories per edat mínima
        ordering = ['edat_minima']

    def __str__(self):
        # Com es veu l'objecte al panell d'admin i als formularis
        return f"{self.nom} ({self.edat_minima}-{self.edat_maxima} anys)"


# ============================================================
# MODEL PARTICIPANT
# Representa una persona inscrita a la cursa.
# Té una ForeignKey a Categoria -> relació 1:N (1 categoria, N participants).
# ============================================================
class Participant(models.Model):
    nom = models.CharField(max_length=50)
    cognoms = models.CharField(max_length=100)
    dorsal = models.IntegerField(unique=True)      # Dorsal únic per participant
    email = models.EmailField()
    data_naixement = models.DateField()

    # Relació amb Categoria: si s'esborra una categoria, s'esborren els seus participants (CASCADE)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='participants'  # Permet fer categoria.participants.all()
    )

    # Temps en segons; pot ser null perquè abans de córrer encara no en té
    temps_segons = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['dorsal']  # Ordena per dorsal per defecte

    def __str__(self):
        return f"#{self.dorsal} {self.nom} {self.cognoms}"

    def temps_format(self):
        """Converteix els segons a format mm:ss per mostrar-ho bonic a les plantilles."""
        if self.temps_segons is None:
            return "-"
        minuts = self.temps_segons // 60
        segons = self.temps_segons % 60
        return f"{minuts:02d}:{segons:02d}"
