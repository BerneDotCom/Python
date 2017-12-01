from django.shortcuts import render

# Create your views here.
def welcome(request, lang):
    if lang == 'fr':
        welcomeText = 'Bienvenue'
    elif lang == 'en':
        welcomeText = 'Welcome'
    elif lang == 'de':
        welcomeText= 'Wilkommen'
    else:
        from store.models import Welcome
        welcomeInstance = Welcome(lang=lang)
        welcomeInstance.save();
    return render(request, 'accueil.html', locals())

def liste(request):
    maListe = [{'name' : 'Bernard'},{'name' : 'Michel'},{'name' : 'Simone'},{'name' : 'Josette'},{'name' : 'Celestin'}]

    return render(request, 'liste.html', locals())
