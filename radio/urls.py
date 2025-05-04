from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    # Ajoute cette ligne dans ton `urls.py`
    path('signup/', views.signup_view, name='signup'),
    # Page de connexion
    path('login/', views.login_view, name='login'),
    
    # Page de déconnexion
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Exemple de route pour le profil de l'utilisateur
    path('accounts/profile/', views.profile, name='user_profile'),
    # URL pour éditer le profil utilisateur
    path('edit_profile/', views.edit_profile, name='edit_profile'),  # URL pour modifier le profil


    # Changer de mot de passe
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # Réinitialisation de mot de passe
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html'
    ), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'
    ), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'
    ), name='password_reset_complete'),

    
    path('podcasts/', views.podcasts, name='podcasts'),
    path('video/', views.video, name='video'),
    path('animateurs/', views.animateurs, name='animateurs'),
    path('programmes/', views.programmes, name='programmes'),
    path('programme/<int:programme_id>/', views.programme_detail, name='programme_detail'),
    path('emissions/', views.emissions, name='emissions'),
    path('emission/<int:emission_id>/', views.emission_detail, name='emission_detail'),
 

    path('diffusion/', views.diffusion, name='diffusion'),
    # Page Contact
    path("contact/", views.contact_view, name="contact"),
    path('parrains/', views.parrains_list, name='parrains_list'),
    path('parrain/<int:id>/', views.parrain_detail, name='parrain_detail'),
    path('articles/', views.article_list, name='article_list'),

    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),
    path('direct/', views.direct, name='direct'),

    path('articles/categorie/<str:category_name>/', views.article_list_by_category, name='article_list_by_category'),
    path('404/', views.page_not_found, name='page_not_found'),
    path('500/', views.server_error, name='server_error'),
    path('search/', views.search, name='search'),
]


