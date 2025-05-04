from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Emission, Direct, Podcast, Video, Animateur, Emission, Programme, Publicite, Article, Contact, Parrain
from django.db.models import Q

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

from django.http import Http404
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.core.mail import send_mail
from .forms import ProfileForm ,ContactForm # Assurez-vous d'utiliser le bon formulaire
from django.contrib import messages
from django.contrib.messages import get_messages


# Vue pour la page d'accueil
def accueil(request):
    emissions = Emission.objects.all()
    return render(request, 'accueil.html', {'emissions': emissions})

def index(request):
    # Déterminez si l'émission en direct est en cours
    direct_is_live = Direct.objects.filter(en_direct=True).exists()
    return render(request, 'accueil.html', {
        'direct_is_live': direct_is_live,
    })



def login_view(request):
    # Supprime les anciens messages avant d'afficher un nouveau
    storage = get_messages(request)
    for _ in storage:
        pass  # Cette boucle vide supprime tous les anciens messages

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenue {username} ! 😊 Vous êtes connecté.")

                if request.POST.get("remember_me"):
                    request.session.set_expiry(1209600)  # 2 semaines

                return redirect("user_profile")
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
        else:
            messages.error(request, "Veuillez vérifier vos informations.")
    else:
        form = AuthenticationForm()

    return render(request, "registration/login.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Inscription réussie ! 🎉 Bienvenue sur notre plateforme.")
            return redirect("index")  # Redirection après succès
        else:
            messages.error(request, "Une erreur est survenue lors de l'inscription. Vérifiez les informations.")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})




@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirige vers la page d'accueil ou une autre page après la mise à jour
    else:
        form = ProfileForm(instance=request.user)
    
    return render(request, 'registration/edit_profile.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'registration/profile.html', {'user': request.user})



def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            # 📩 Envoyer un email (optionnel)
            send_mail(
                f"Nouveau message de {name}",
                message,
                email,
                ["admin@example.com"],  # Remplace avec l'email de ton admin
                fail_silently=False,
            )

            return redirect("contact_success")  # Redirige vers une page de succès
    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {"form": form})


def contact_success_view(request):
    return render(request, "contact/contact_success.html")



  



# Vue pour la page en direct
def direct(request):
    directs = Direct.objects.all().order_by('-date_publication')
    return render(request, 'emissions/direct.html', {'directs': directs})




# Vue pour les podcasts
def podcasts(request):
    podcasts = Podcast.objects.all().order_by('-date_publication')
    return render(request, 'emissions/podcasts.html', {'podcasts': podcasts})


# Vue pour la page vidéo
def video(request):
    videos = Video.objects.all().order_by('-date_publication')
    return render(request, 'emissions/video.html', {'videos': videos})


# Vue pour afficher la liste des animateurs
def animateurs(request):
    animateurs = Animateur.objects.all()
    return render(request, 'animateurs/animateurs.html', {'animateurs': animateurs})

# Vue pour afficher la liste des émissions
def emissions(request):
    emissions = Emission.objects.all()
    return render(request, 'emissions/emissions.html', {'emissions': emissions})

# Vue pour afficher les détails d'une émission
def emission_detail(request, emission_id):
    emission = get_object_or_404(Emission, id=emission_id)
    return render(request, 'emissions/emission_detail.html', {'emission': emission})



def article_list(request):
    articles = Article.objects.all().order_by('-date_publication')
    articles_suggeres = Article.objects.all().order_by('-date_publication')[:5]
    publicites = Publicite.objects.all()[:3]  # Par exemple, les 3 dernières pubs

    return render(request, 'articles/article_list.html', {
        'articles': articles,
        'articles_suggeres': articles_suggeres,
        'publicites': publicites  # Envoie les publicités au template
    })



def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    
    articles_suggeres = Article.objects.filter(
        categorie=article.categorie
    ).exclude(id=article.id).order_by('-date_publication')[:5]

    publicites = Publicite.objects.all()[:3]  # Ajout des publicités

    return render(request, 'articles/article_detail.html', {
        'article': article,
        'articles_suggeres': articles_suggeres,
        'publicites': publicites,  # Envoie les pubs
    })



def article_list_by_category(request, category_name):
    categorie_valide = dict(Article.CATEGORIE_CHOICES).get(category_name)
    if not categorie_valide:
        raise Http404("Cette catégorie n'existe pas.")

    articles = Article.objects.filter(
        categorie=category_name
    ).order_by('-date_publication')

    articles_suggeres = Article.objects.all().order_by('-date_publication')[:5]
    publicites = Publicite.objects.all()[:3]  # Ajout des publicités

    return render(request, 'articles/article_list.html', {
        'articles': articles,
        'articles_suggeres': articles_suggeres,
        'publicites': publicites,
        'category_name': category_name,
    })


# Vue pour afficher la liste des programmes
def programmes(request):
    jours = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    programmes_par_jour = {
        jour: Programme.objects.filter(jour=jour).order_by('heure_debut')
        for jour in jours
    }
    return render(request, 'programmes/programmes.html', {
        'programmes_par_jour': programmes_par_jour
    })

# Vue pour afficher les détails d'un programme
def programme_detail(request, programme_id):
    programme = get_object_or_404(Programme, id=programme_id)
    # Correction ici
    return render(request, 'programmes/programme_detail.html', {'programme': programme})




# Vue pour afficher la diffusion
def diffusion(request):
    return render(request, 'emissions/diffusion.html')


def parrains_list(request):
    parrains = Parrain.objects.all()
    return render(request, 'parrains/parrains.html', {'parrains': parrains})


def parrain_detail(request, id):
    parrain = get_object_or_404(Parrain, id=id)
    parrain.valid_contact = parrain.contact and parrain.contact.startswith(
        'http')
    return render(request, 'parrains/parrain_detail.html', {'parrain': parrain})




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

    return render(request, 'search/search_results.html', {'query': query, **results})
