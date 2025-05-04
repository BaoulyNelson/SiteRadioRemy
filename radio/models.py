from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


# Modèle pour les directs (émissions en direct)
class Direct(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    url = models.URLField()  # Lien vers le direct
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre


# Modèle pour les podcasts
class Podcast(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    # URL pour les audios externes
    url = models.URLField(blank=True, null=True)
    audio_file = models.FileField(
        upload_to='podcasts/', blank=True, null=True)  # Fichier audio local
    auteur = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre


class Video(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    # URL pour les vidéos externes
    url = models.URLField(blank=True, null=True)
    video_file = models.FileField(
        upload_to='videos/', blank=True, null=True)  # Fichier vidéo local
    auteur = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

# Modèle pour les animateurs


class Animateur(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField(blank=True)
    # Ajout du champ image
    logo = models.ImageField(
        upload_to='animateurs/logos/', blank=True, null=True)
    role = models.CharField(max_length=100, blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)


    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Emission(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    animateur = models.ForeignKey(Animateur, on_delete=models.CASCADE)
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    date = models.DateField()
    en_direct = models.BooleanField(default=False)

    def __str__(self):
        return self.titre


class Programme(models.Model):
    JOURS_SEMAINE = [
        ('monday', 'Lundi'),
        ('tuesday', 'Mardi'),
        ('wednesday', 'Mercredi'),
        ('thursday', 'Jeudi'),
        ('friday', 'Vendredi'),
        ('saturday', 'Samedi'),
        ('sunday', 'Dimanche'),
    ]

    emission = models.ForeignKey(Emission, on_delete=models.CASCADE)
    jour = models.CharField(max_length=10, choices=JOURS_SEMAINE)
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    nom = models.CharField(max_length=200, blank=True, null=True)  # Nom alternatif de l'émission

    def __str__(self):
        return f"{self.nom or self.emission.titre} ({self.jour})"

# Modèle pour les publicités


class Publicite(models.Model):
    nom_annonceur = models.CharField(max_length=200)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    lien = models.URLField(blank=True)

    def __str__(self):
        return self.nom_annonceur


class Contact(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, default="")
    email = models.EmailField()
    telephone = models.CharField(max_length=15, validators=[
        RegexValidator(
            regex=r'^\+?1?\d{9,15}$', message="Le numéro de téléphone doit être au format : '+999999999'. Jusqu'à 15 chiffres autorisés.")
    ])
    sujet = models.CharField(max_length=255)  # Ajout du champ sujet
    message = models.TextField()

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.email}"


class Parrain(models.Model):
    nom = models.CharField(max_length=100)
    contact = models.CharField(max_length=15, validators=[
        RegexValidator(
            regex=r'^\+?1?\d{9,15}$', message="Le numéro de téléphone doit être au format : '+999999999'. Jusqu'à 15 chiffres autorisés.")
    ])
    logo = models.ImageField(upload_to='parrains/logos/',
                             blank=True, null=True)  # Ajout du champ image
    type_parrainage = models.CharField(max_length=200, choices=[(
        'or', 'Or'), ('argent', 'Argent'), ('bronze', 'Bronze')], default='bronze')
    details = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom



class Article(models.Model):
    CATEGORIE_CHOICES = [
        ('Culture', 'Culture'),
        ('Découverte', 'Découverte'),
        ('Économie', 'Économie'),
        ('Sports', 'Sports'),
        ('Tendance', 'Tendance'),
        ('Liste de Lecture', 'Liste de Lecture'),
        ('Marque-Page', 'Marque-Page'),
    ]
    
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    auteur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='articles/images/', blank=True, null=True)
    categorie = models.CharField(max_length=20, choices=CATEGORIE_CHOICES, default='Culture')

    def save(self, *args, **kwargs):
        if not self.auteur:  # Si aucun auteur n'est défini
            self.auteur, _ = User.objects.get_or_create(username="MFM", defaults={"is_active": False})
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titre

