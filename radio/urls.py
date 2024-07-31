from django.urls import path
from . import views
from .views import search

urlpatterns = [
    # Page d'accueil
    path('', views.accueil, name='accueil'),  # Accueil devient la page d'accueil par défaut
    
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    # Page en direct
    path('direct/', views.direct, name='direct'),
    path('chat/<str:room_name>/', views.room, name='room'),
    # Podcasts
    path('podcasts/', views.podcasts, name='podcasts'),
    
    #page pour video
    path('video/', views.video, name='video'),
    
    # Liste des animateurs
    path('animateurs/', views.animateurs, name='animateurs'),
    
    # Liste des programmes
    path('programmes/', views.programmes, name='programmes'),
    
    # Détail d'un programme
    path('programme/<int:programme_id>/', views.programme_detail, name='programme_detail'),
    
    # Liste des émissions
    path('emissions/', views.emissions, name='emissions'),
    path('emission/<int:emission_id>/', views.emission_detail, name='emission_detail'),

    # Liste des auditeurs
    path('auditeurs/', views.auditeurs, name='auditeurs'),
    
    # Liste des publicités
    path('publicites/', views.publicites, name='publicites'),
    
    # Statistiques
    path('statistiques/', views.statistiques, name='statistiques'),
    
    #langues a choisir
    path('set_language/', views.set_language, name='set_language'),
    
    #diffusion
    path('diffusion/', views.diffusion, name='diffusion'),
    path('contacts/', views.contact, name='contacts'),
    path('parrains/', views.parrains, name='parrains'),
    # Catégories spécifiques
    path('decouvrir/', views.decouvrir, name='decouvrir'),
    path('tendance/', views.tendance, name='tendance'),
    path('liste_de_lecture/', views.liste_de_lecture, name='liste_de_lecture'),
    path('marque_page/', views.marque_page, name='marque_page'),
    path('economie/', views.economie, name='economie'),
    path('culture/', views.culture, name='culture'),
    path('sports/', views.sports, name='sports'),
    path('articles/', views.article_list, name='article_list'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('live_comments/', views.live_comments, name='live_comments'),
    # Gestion des erreurs
    path('404/', views.page_not_found, name='page_not_found'),
    path('500/', views.server_error, name='server_error'),
    
    path('search/', search, name='search'),
    
    
]
