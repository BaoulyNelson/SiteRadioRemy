# Generated by Django 5.0.6 on 2024-08-14 00:31

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=100)),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('bio', models.TextField(blank=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='animateurs/logos/')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Le numéro de téléphone doit être au format : '+999999999'. Jusqu'à 15 chiffres autorisés.", regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Direct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('url', models.URLField()),
                ('date_publication', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parrain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Le numéro de téléphone doit être au format : '+999999999'. Jusqu'à 15 chiffres autorisés.", regex='^\\+?1?\\d{9,15}$')])),
                ('logo', models.ImageField(blank=True, null=True, upload_to='parrains/logos/')),
                ('type_parrainage', models.CharField(choices=[('or', 'Or'), ('argent', 'Argent'), ('bronze', 'Bronze')], default='bronze', max_length=200)),
                ('details', models.TextField(blank=True, null=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publicite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_annonceur', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('lien', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('contenu', models.TextField()),
                ('date_publication', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='articles/images/')),
                ('categorie', models.CharField(choices=[('Culture', 'Culture'), ('Découverte', 'Découverte'), ('Économie', 'Économie'), ('Sports', 'Sports'), ('Tendance', 'Tendance'), ('Liste de Lecture', 'Liste de Lecture'), ('Marque-Page', 'Marque-Page')], default='Culture', max_length=20)),
                ('auteur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Emission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('heure_debut', models.TimeField()),
                ('heure_fin', models.TimeField()),
                ('date', models.DateField()),
                ('en_direct', models.BooleanField(default=False)),
                ('animateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.animateur')),
            ],
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('url', models.URLField(blank=True, null=True)),
                ('audio_file', models.FileField(blank=True, null=True, upload_to='podcasts/')),
                ('date_publication', models.DateTimeField(auto_now_add=True)),
                ('auteur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_diffusion', models.DateField()),
                ('heure_debut', models.TimeField()),
                ('heure_fin', models.TimeField()),
                ('nom', models.CharField(blank=True, max_length=200, null=True)),
                ('emission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.emission')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('url', models.URLField(blank=True, null=True)),
                ('video_file', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('date_publication', models.DateTimeField(auto_now_add=True)),
                ('auteur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
