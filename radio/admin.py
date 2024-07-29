# radio/admin.py
from django.contrib import admin
from .models import Video, Podcast, Direct, Animateur, Emission, Programme, Auditeur, Publicite, Statistique, Article,Comment,Contact,Parrain

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_publication', 'auteur')
    list_filter = ('date_publication',)
    search_fields = ('titre', 'description')
    fields = ('titre', 'description', 'url', 'video_file', 'auteur', 'date_publication')
    readonly_fields = ('date_publication',)

@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_publication', 'auteur')
    list_filter = ('date_publication',)
    search_fields = ('titre', 'description')
    fields = ('titre', 'description', 'url', 'audio_file', 'auteur', 'date_publication')
    readonly_fields = ('date_publication',)

@admin.register(Direct)
class DirectAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_publication')
    search_fields = ('titre',)

@admin.register(Animateur)
class AnimateurAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'email')
    search_fields = ('nom', 'prenom')

@admin.register(Emission)
class EmissionAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date', 'en_direct', 'heure_debut', 'heure_fin')
    list_filter = ('en_direct',)
    search_fields = ('titre',)

@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('emission', 'date_diffusion', 'heure_debut', 'heure_fin')
    search_fields = ('emission__titre',)

@admin.register(Auditeur)
class AuditeurAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'date_inscription')
    search_fields = ('utilisateur__username',)

@admin.register(Publicite)
class PubliciteAdmin(admin.ModelAdmin):
    list_display = ('nom_annonceur', 'date_debut', 'date_fin')
    search_fields = ('nom_annonceur',)

@admin.register(Statistique)
class StatistiqueAdmin(admin.ModelAdmin):
    list_display = ('emission', 'auditeurs', 'date_statistique')
    search_fields = ('emission__titre',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'auteur', 'date_publication')  # Ajout de 'categorie'
    list_filter = ('categorie', 'date_publication')  # Ajout de 'categorie'
    search_fields = ('titre', 'contenu')
    readonly_fields = ('date_publication',)
    fieldsets = (
        (None, {
            'fields': ('titre', 'contenu', 'auteur', 'image', 'categorie')  # Ajout de 'categorie'
        }),
        ('Dates', {
            'fields': ('date_publication',),
        }),
    )
    
    admin.site.register(Comment)
    admin.site.register(Contact)
    admin.site.register(Parrain)
