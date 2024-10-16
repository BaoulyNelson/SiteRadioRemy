from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),  # Ajoutez cela si nécessaire
    path('profile/', views.account_profile, name='account_profile'),  # Assurez-vous que le nom correspond
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    path('stats_dashboard/', views.stats_dashboard, name='stats_dashboard'),

    path('logout/', LogoutView.as_view(), name='logout'),

    path('direct/', views.direct, name='direct'),
    
    path('podcasts/', views.podcasts, name='podcasts'),
    path('video/', views.video, name='video'),
    path('animateurs/', views.animateurs, name='animateurs'),
    path('programmes/', views.programmes, name='programmes'),
    path('programme/<int:programme_id>/', views.programme_detail, name='programme_detail'),
    path('emissions/', views.emissions, name='emissions'),
    path('emission/<int:emission_id>/', views.emission_detail, name='emission_detail'),
    path('publicites/', views.publicites, name='publicites'),
    path('set_language/', views.set_language, name='set_language'),
    path('diffusion/', views.diffusion, name='diffusion'),
    path('contacts/', views.contact, name='contacts'),
    path('parrains/', views.parrains_list, name='parrains_list'),
    path('parrain/<int:id>/', views.parrain_detail, name='parrain_detail'),
    path('articles/', views.article_list, name='article_list'),
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),
    path('articles/categorie/<str:category_name>/', views.article_list_by_category, name='article_list_by_category'),
    path('404/', views.page_not_found, name='page_not_found'),
    path('500/', views.server_error, name='server_error'),
    path('search/', views.search, name='search'),
]

