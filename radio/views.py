from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Emission, Direct, Podcast, Video, Animateur, Emission, Programme, Publicite, Article, Contact, Parrain
from django.db.models import Q
from django.utils import translation
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm  
from django.http import HttpResponse


# Vue pour la page d'accueil
def accueil(request):
    emissions = Emission.objects.all()
    return render(request, 'accueil.html', {'emissions': emissions})

def custom_admin_index(request):
    return render(request, 'admin/index.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connexion de l'utilisateur après l'enregistrement
            return redirect('accueil')  # Rediriger vers la page d'accueil ou autre
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('accueil')  # Redirige vers la page d'accueil ou une autre page
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def account_profile(request):
    return render(request, 'registration/account_profile.html', {'user': request.user})


@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    animateurs = Animateur.objects.all()
    articles = Article.objects.all()
    directs = Direct.objects.all()
    emissions = Emission.objects.all()
    podcasts = Podcast.objects.all()
    programmes = Programme.objects.all()
    publicites = Publicite.objects.all()
    videos = Video.objects.all()
    contacts = Contact.objects.all()
    parrains = Parrain.objects.all()
    users = User.objects.all()  # Récupérer tous les utilisateurs

    return render(request, 'admin/admin_dashboard.html', {
        'animateurs': animateurs,
        'articles': articles,
        'directs': directs,
        'emissions': emissions,
        'podcasts': podcasts,
        'programmes': programmes,
        'publicites': publicites,
        'videos': videos,
        'contacts': contacts,
        'parrains': parrains,
        'users': users,  # Passer la liste des utilisateurs au template
    })
    
    
@login_required
@user_passes_test(lambda u: u.is_staff or u.is_superuser)  # Permet aux utilisateurs du personnel et aux superutilisateurs d'accéder aux statistiques
def stats_dashboard(request):
    # Récupérer les statistiques
    total_users = User.objects.count()
    total_animateurs = Animateur.objects.count()
    total_articles = Article.objects.count()
    total_directs = Direct.objects.count()
    total_emissions = Emission.objects.count()
    total_podcasts = Podcast.objects.count()
    total_programmes = Programme.objects.count()
    total_publicites = Publicite.objects.count()
    total_videos = Video.objects.count()
    total_contacts = Contact.objects.count()
    total_parrains = Parrain.objects.count()

    # Renvoyer les statistiques au template
    return render(request, 'admin/stats_dashboard.html', {
        'total_users': total_users,
        'total_animateurs': total_animateurs,
        'total_articles': total_articles,
        'total_directs': total_directs,
        'total_emissions': total_emissions,
        'total_podcasts': total_podcasts,
        'total_programmes': total_programmes,
        'total_publicites': total_publicites,
        'total_videos': total_videos,
        'total_contacts': total_contacts,
        'total_parrains': total_parrains,
    })

def index(request):
    # Déterminez si l'émission en direct est en cours
    direct_is_live = Direct.objects.filter(en_direct=True).exists()
    return render(request, 'index.html', {
        'direct_is_live': direct_is_live,
    })



# Vue pour la page en direct
def direct(request):
    directs = Direct.objects.all().order_by('-date_publication')
    return render(request, 'direct.html', {'directs': directs})




# Vue pour les podcasts
def podcasts(request):
    podcasts = Podcast.objects.all().order_by('-date_publication')
    return render(request, 'podcasts.html', {'podcasts': podcasts})


# Vue pour la page vidéo
def video(request):
    videos = Video.objects.all().order_by('-date_publication')
    return render(request, 'video.html', {'videos': videos})


# Vue pour afficher la liste des animateurs
def animateurs(request):
    animateurs = Animateur.objects.all()
    return render(request, 'animateurs.html', {'animateurs': animateurs})

# Vue pour afficher la liste des émissions
def emissions(request):
    emissions = Emission.objects.all()
    return render(request, 'emissions.html', {'emissions': emissions})

# Vue pour afficher les détails d'une émission
def emission_detail(request, emission_id):
    emission = get_object_or_404(Emission, id=emission_id)
    return render(request, 'emission_detail.html', {'emission': emission})

# Vue pour afficher la liste des articles
def article_list(request):
    articles = Article.objects.all().order_by('-date_publication')
    return render(request, 'article_list.html', {'articles': articles})


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'article_detail.html', {'article': article})


def article_list_by_category(request, category_name):
    articles = Article.objects.filter(
        categorie=category_name).order_by('-date_publication')
    return render(request, 'article_list.html', {'articles': articles, 'category_name': category_name})


# Vue pour afficher la liste des programmes
def programmes(request):
    programmes = Programme.objects.all().order_by('-date_diffusion')
    return render(request, 'programmes.html', {'programmes': programmes})


# Vue pour afficher les détails d'un programme
def programme_detail(request, programme_id):
    programme = get_object_or_404(Programme, id=programme_id)
    # Correction ici
    return render(request, 'programme_detail.html', {'programme': programme})


# Vue pour afficher la liste des publicités
def publicites(request):
    publicites = Publicite.objects.all()
    return render(request, 'publicites.html', {'publicites': publicites})


# Vue pour afficher la diffusion
def diffusion(request):
    return render(request, 'diffusion.html')


def parrains_list(request):
    parrains = Parrain.objects.all()
    return render(request, 'parrains.html', {'parrains': parrains})


def parrain_detail(request, id):
    parrain = get_object_or_404(Parrain, id=id)
    parrain.valid_contact = parrain.contact and parrain.contact.startswith(
        'http')
    return render(request, 'parrain_detail.html', {'parrain': parrain})


def set_language(request):
    user_language = request.GET.get('language', 'fr')
    translation.activate(user_language)
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    return response


def contact(request):
    contacts = Contact.objects.all()
    return render(request, 'contact.html', {'contacts': contacts})


# Gestion des erreurs
def page_not_found(request, exception=None):
    return render(request, '404.html', status=404)


def server_error(request):
    return render(request, '500.html', status=500)


def search(request):
    query = request.GET.get('q', '').strip().lower()
    results = {}

    if query:
        if query == "animateurs":
            results['animateurs'] = Animateur.objects.all()

        elif query == "emissions":
            results['emissions'] = Emission.objects.all()

        elif query == "podcasts":
            results['podcasts'] = Podcast.objects.all()

        elif query == "videos":
            results['videos'] = Video.objects.all()

        elif query == "programmes":
            results['programmes'] = Programme.objects.all()

        elif query == "publicites":
            results['publicites'] = Publicite.objects.all()

        elif query == "contacts":
            results['contacts'] = Contact.objects.all()

        elif query == "parrains":
            results['parrains'] = Parrain.objects.all()

        elif query == "articles":
            # Récupère tous les articles si "articles" est recherché
            results['articles'] = Article.objects.all()

        elif query in [categorie[0].lower() for categorie in Article.CATEGORIE_CHOICES]:
            # Si la recherche correspond à une catégorie spécifique d'articles
            results['articles'] = Article.objects.filter(categorie__iexact=query.capitalize())

        else:
            # Recherche générique si le mot-clé ne correspond à aucune catégorie ou terme spécifique
            results['articles'] = Article.objects.filter(
                Q(titre__icontains=query) | 
                Q(contenu__icontains=query) | 
                Q(categorie__iexact=query.capitalize())
            )

    return render(request, 'search_results.html', {'query': query, **results})
