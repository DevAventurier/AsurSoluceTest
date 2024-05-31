from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore

class Person(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="Prénom")
    last_name = models.CharField(max_length=255, verbose_name="Nom de famille")
    email = models.EmailField(unique=True, null=True, blank=True, verbose_name="Adresse email")
    phone_number = models.CharField(max_length=255, unique=True, verbose_name="Numéro de téléphone")
    SEXE_CHOICES = [
        ('F', 'Féminin'),
        ('M', 'Masculin')
    ]
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES, verbose_name="Sexe")
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Date de naissance")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Créé à")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Mis à jour à")
    delete_at = models.DateTimeField(null=True, blank=True, verbose_name="Supprimé à")
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        abstract = True
        verbose_name = "Personne"
        verbose_name_plural = "Personnes"

class CustomUser(Person):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.user = User.objects.create_user(username=self.phone_number, password="123456789")        
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Utilisateur personnalisé"
        verbose_name_plural = "Utilisateurs personnalisés"

class Agent(CustomUser):
    matricule = models.CharField(max_length=255, verbose_name="Matricule")

    class Meta:
        verbose_name = "Agent"
        verbose_name_plural = "Agents"

class Driver(Person):
    license_number = models.CharField(max_length=255, verbose_name="Numéro du permis")

    class Meta:
        verbose_name = "Conducteur"
        verbose_name_plural = "Conducteurs"

class Criteria(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nom")
    description = models.CharField(max_length=255, verbose_name="Description")

    class Meta:
        verbose_name = "Critère"
        verbose_name_plural = "Critères"

class Almond(models.Model):
    montant = models.CharField(max_length=255, verbose_name="Montant")
    paid = models.BooleanField(default=False, verbose_name="Payé")

    class Meta:
        verbose_name = "Amande"
        verbose_name_plural = "Amandes"

class ControlPoint(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nom")
    gps_location = models.CharField(max_length=255, verbose_name="Localisation GPS")
    agents = models.ManyToManyField(Agent, through="ControlPointByAgent")

    class Meta:
        verbose_name = "Point de contrôle"
        verbose_name_plural = "Points de contrôle"

class ControlPointByAgent(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    control_point = models.ForeignKey(ControlPoint, on_delete=models.CASCADE)
    state = models.BooleanField(max_length=255, verbose_name="État")
    
    class Meta:
        verbose_name = "Point de contrôle par agent"
        verbose_name_plural = "Points de contrôle par agents"
        unique_together = ('agent', 'control_point')

class RoadControl(models.Model):
    date = models.DateField(verbose_name="Date")
    criteria = models.ManyToManyField(Criteria, through="CriteriaByControl")
    control_point = models.ForeignKey(ControlPoint, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Contrôle routier"
        verbose_name_plural = "Contrôles routiers"

class CriteriaByControl(models.Model):
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)
    road_control = models.ForeignKey(RoadControl, on_delete=models.CASCADE)
    state = models.CharField(max_length=255, verbose_name="État")
    almond = models.ForeignKey(Almond, on_delete=models.CASCADE, verbose_name="Amande", null=True, blank=True)
    
    class Meta:
        verbose_name = "Critère par contrôle"
        verbose_name_plural = "Critères par contrôle"
        unique_together = ('criteria', 'road_control')

class Vehicle(models.Model):
    immatriculation = models.CharField(max_length=255, verbose_name="Immatriculation")

    class Meta:
        verbose_name = "Véhicule"
        verbose_name_plural = "Véhicules"


