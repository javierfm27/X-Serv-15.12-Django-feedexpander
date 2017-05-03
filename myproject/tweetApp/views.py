from django.shortcuts import render
from django.http import *
from django.views.decorators.csrf import csrf_exempt
from urllib.request import urlopen
import feedparser

def obtainTitle(canal):
    titles = []
    for i in range(5):
        titles.append(canal.entries[i].title)
        titles[i] = "TWET Nº " + str(i + 1) + "<br>" +  titles[i] + "<br>"
    return titles
# Create your views here.
@csrf_exempt
def barra(request):
    if request.method == 'GET':
        bodyHtml = "Introduce el User del que quieras obtener sus 5 ultimos tweets<br>" \
            + "<form method='POST'>\n <input type='text' name='user'></form>"
        return HttpResponse(bodyHtml)
    elif request.method == 'POST':
        user = request.POST['user']
        url = "http://" + request.META['HTTP_HOST'] + "/feed/" + user
        return HttpResponseRedirect(url)


def feedUser(request, user):
    urlFeed = "https://twitrss.me/twitter_user_to_rss/?user="
    urlFeed = urlFeed + user
    stringRSS = urlopen(urlFeed)
    canalRSS = feedparser.parse(stringRSS) #Cada item es una entrada, asique para obtener 5 basta con hacer un bucle
    #Primero obtenemos el tuit
    twets = obtainTitle(canalRSS)
    return HttpResponse(twets)
