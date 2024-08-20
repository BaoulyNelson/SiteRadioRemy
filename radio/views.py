from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Emission, Direct, Podcast, Video, Animateur, Emission, Programme, Publicite, Article, Contact, Parrain
from django.db.models import Q
from django.utils import translation
from django.conf import settings


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
    })


def index(request):
    # Déterminez si l'émission en direct est en cours
    direct_is_live = Direct.objects.filter(en_direct=True).exists()
    return render(request, 'radio/index.html', {
        'direct_is_live': direct_is_live,
    })

# Vue pour la page d'accueil


def accueil(request):
    emissions = Emission.objects.all()
    return render(request, 'radio/accueil.html', {'emissions': emissions})

# Vue pour la page en direct


def direct(request):
    directs = Direct.objects.all().order_by('-date_publication')
    return render(request, 'radio/direct.html', {'directs': directs})


def room(request, room_name):
    return render(request, 'radio/room.html', {
        'room_name': room_name
    })


# Vue pour les podcasts
def podcasts(request):
    podcasts = Podcast.objects.all().order_by('-date_publication')
    return render(request, 'radio/podcasts.html', {'podcasts': podcasts})


# Vue pour la page vidéo
def video(request):
    videos = Video.objects.all().order_by('-date_publication')
    return render(request, 'radio/video.html', {'videos': videos})


# Vue pour afficher la liste des animateurs
def animateurs(request):
    animateurs = Animateur.objects.all()
    return render(request, 'radio/animateurs.html', {'animateurs': animateurs})

# Vue pour afficher la liste des émissions


def emissions(request):
    emissions = Emission.objects.all()
    return render(request, 'radio/emissions.html', {'emissions': emissions})

# Vue pour afficher les détails d'une émission


def emission_detail(request, emission_id):
    emission = get_object_or_404(Emission, id=emission_id)
    return render(request, 'radio/emission_detail.html', {'emission': emission})

# Vue pour afficher la liste des articles


def article_list(request):
    articles = Article.objects.all().order_by('-date_publication')
    return render(request, 'radio/article_list.html', {'articles': articles})


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'radio/article_detail.html', {'article': article})


def article_list_by_category(request, category_name):
    articles = Article.objects.filter(
        categorie=category_name).order_by('-date_publication')
    return render(request, 'radio/article_list.html', {'articles': articles, 'category_name': category_name})


# Vue pour afficher la liste des programmes
def programmes(request):
    programmes = Programme.objects.all().order_by('-date_diffusion')
    return render(request, 'radio/programmes.html', {'programmes': programmes})


# Vue pour afficher les détails d'un programme
def programme_detail(request, programme_id):
    programme = get_object_or_404(Programme, id=programme_id)
    # Correction ici
    return render(request, 'radio/programme_detail.html', {'programme': programme})


# Vue pour afficher la liste des publicités
def publicites(request):
    publicites = Publicite.objects.all()
    return render(request, 'radio/publicites.html', {'publicites': publicites})


# Vue pour afficher la diffusion
def diffusion(request):
    return render(request, 'radio/diffusion.html')


def parrains_list(request):
    parrains = Parrain.objects.all()
    return render(request, 'radio/parrains.html', {'parrains': parrains})


def parrain_detail(request, id):
    parrain = get_object_or_404(Parrain, id=id)
    parrain.valid_contact = parrain.contact and parrain.contact.startswith(
        'http')
    return render(request, 'radio/parrain_detail.html', {'parrain': parrain})


def set_language(request):
    user_language = request.GET.get('language', 'fr')
    translation.activate(user_language)
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    return response


def contact(request):
    contacts = Contact.objects.all()
    return render(request, 'radio/contact.html', {'contacts': contacts})


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

    return render(request, 'radio/search_results.html', {'query': query, **results})
