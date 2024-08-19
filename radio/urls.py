from django.urls import path
from . import views

urlpatterns = [
    # Accueil devient la page d'accueil par défaut
    path('', views.accueil, name='accueil'),

    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # Page en direct
    path('direct/', views.direct, name='direct'),
    path('chat/<str:room_name>/', views.room, name='room'),
    # Podcasts
    path('podcasts/', views.podcasts, name='podcasts'),

    # page pour video
    path('video/', views.video, name='video'),

    # Liste des animateurs
    path('animateurs/', views.animateurs, name='animateurs'),

    # Liste des programmes
    path('programmes/', views.programmes, name='programmes'),

    # Détail d'un programme
    path('programme/<int:programme_id>/',
         views.programme_detail, name='programme_detail'),

    # Liste des émissions
    path('emissions/', views.emissions, name='emissions'),
    path('emission/<int:emission_id>/',
         views.emission_detail, name='emission_detail'),

    # Liste des publicités
    path('publicites/', views.publicites, name='publicites'),

    # langues a choisir
    path('set_language/', views.set_language, name='set_language'),

    # diffusion
    path('diffusion/', views.diffusion, name='diffusion'),
    path('contacts/', views.contact, name='contacts'),
    
 
    path('parrains/', views.parrains_list, name='parrains_list'),
    path('parrain/<int:id>/', views.parrain_detail, name='parrain_detail'),

    # Catégories spécifiques
    path('articles/', views.article_list, name='article_list'),
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),
    path('articles/categorie/<str:category_name>/', views.article_list_by_category, name='article_list_by_category'),
    
    # Gestion des erreurs
    path('404/', views.page_not_found, name='page_not_found'),
    path('500/', views.server_error, name='server_error'),

    path('search/', views.search, name='search'),
]
