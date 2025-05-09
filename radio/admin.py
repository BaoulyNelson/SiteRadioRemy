# radio/admin.py
from django.contrib import admin
from .models import Video, Podcast, Direct, Animateur, Emission, Programme, Publicite, Article,Contact,Parrain

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
    list_display = ('nom', 'prenom', 'email', 'logo')  # Mettre 'nom' avant 'prenom'
    search_fields = ('nom', 'prenom')
    list_filter = ('nom',)  # Optionnel : pour ajouter un filtre sur le nom

@admin.register(Emission)
class EmissionAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date', 'en_direct', 'heure_debut', 'heure_fin')
    list_filter = ('en_direct',)
    search_fields = ('titre',)

@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'jour', 'heure_debut', 'heure_fin')
    list_filter = ('jour',)
    
    
    
@admin.register(Publicite)
class PubliciteAdmin(admin.ModelAdmin):
    list_display = ('nom_annonceur', 'date_debut', 'date_fin')
    search_fields = ('nom_annonceur',)



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'auteur', 'date_publication')  # Ajout de 'categorie'
    list_filter = ('categorie', 'date_publication')  # Ajout de 'categorie'
    search_fields = ('titre', 'contenu')
    readonly_fields = ('date_publication',)
    
    # Définir l'ordre des champs dans le formulaire d'édition
    fieldsets = (
        (None, {
            'fields': ('titre', 'categorie', 'contenu', 'auteur', 'image')  # Ordre modifié pour correspondre à votre besoin
        }),
        ('Dates', {
            'fields': ('date_publication',),
        }),
    )
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'telephone')
    search_fields = ('nom', 'prenom', 'email', 'telephone')
    fieldsets = (
        (None, {
            'fields': ('nom', 'prenom', 'email', 'telephone')
        }),
    )

@admin.register(Parrain)
class ParrainAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type_parrainage', 'date_creation')
    list_filter = ('type_parrainage',)
    search_fields = ('nom', 'details')
    fields = ('nom', 'contact', 'logo', 'type_parrainage', 'details', 'date_creation')
    readonly_fields = ('date_creation',)
 
