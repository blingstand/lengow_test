from django.shortcuts import render

def home(request):

    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """

    return HttpResponse("""

        <h1>Bienvenue sur mon application Order !</h1>

        <p>Je vais mettre mon script ici !</p>

    """)

# Create your views here.
