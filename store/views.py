from django.shortcuts import render
from store.models import Welcome
from store.models import Author, Articles

# Create your views here.
def welcome(request, lang):
    resultSet =  Welcome.objects.filter(lang=lang)
    if not resultSet:
        welcomeInstance = Welcome(lang=lang, welcomeText="NTM")
        welcomeInstance.save();
        resultSet = [welcomeInstance]
    return render(request, 'accueil.html', locals())

def author(request, author):
    resultSet =  Author.objects.filter(name=author)
    if not resultSet:
        authorInstance = Author(name=author, lastname="Jean")
        authorInstance.save();
        resultSet = [authorInstance]
    return render(request, 'author.html', locals())

def authorList(request):
    resultSet =  Author.objects.all()
    return render(request, 'authorList.html', locals())

def article(request, article):
    authorSet =  Author.objects.filter(name='Michel')
    resultSet =  Articles.objects.filter(title=article)
    if not resultSet:
        articleInstance = Articles(title=article, desc="Description de test", author=authorSet[0])
        articleInstance.save();
        resultSet = [articleInstance]
    return render(request, 'article.html', locals())

def articleList(request):
    resultSet =  Articles.objects.all()
    return render(request, 'articleList.html', locals())
