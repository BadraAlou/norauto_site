# main/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Produit, Panier, CartItem
from django.conf import settings

def get_or_create_cart(request):
    """
    Récupère ou crée un panier pour l'utilisateur (connecté ou anonyme via session).
    """
    if request.user.is_authenticated:
        panier, created = Panier.objects.get_or_create(
            utilisateur=request.user,
            defaults={'session_id': request.session.session_key}
        )
    else:
        if not request.session.session_key:
            request.session.create()
        panier, created = Panier.objects.get_or_create(
            session_id=request.session.session_key,
            defaults={'utilisateur': None}
        )
    return panier

def home(request):
    return render(request, 'main/home.html')

def accessoires(request):
    return render(request, 'main/accessoires.html')

def contact(request):
    return render(request, 'main/contact.html')

def a_propos(request):
    return render(request, 'main/a_propos.html')

def nos_produits(request):
    """
    Affiche la liste des produits, filtrée par catégorie (Voiture, Moto, Personne, Enfant).
    """
    categorie = request.GET.get('categorie', 'VOITURE')  # Par défaut, catégorie Voiture
    produits = Produit.objects.filter(en_stock=True, categorie=categorie)
    categories = [choice[0] for choice in Produit.CATEGORIE_CHOICES]
    context = {
        'produits': produits,
        'categories': categories,
        'categorie_active': categorie,
    }
    return render(request, 'main/nos_produits.html', context)

def panier(request):
    """
    Affiche le panier de l'utilisateur avec les articles.
    """
    panier = get_or_create_cart(request)
    cart_items = panier.cartitem_set.all()
    context = {
        'cart_items': cart_items,
        'panier': panier,
    }
    return render(request, 'main/panier.html', context)

def ajouter_au_panier(request, produit_id):
    """
    Ajoute un produit au panier ou incrémente sa quantité.
    """
    produit = get_object_or_404(Produit, id=produit_id)
    panier = get_or_create_cart(request)

    cart_item, created = CartItem.objects.get_or_create(
        panier=panier,
        produit=produit,
        defaults={'quantite': 1}
    )
    if not created:
        cart_item.quantite += 1
        cart_item.save()

    messages.success(request, f"{produit.nom} a été ajouté à votre panier.")
    return redirect('panier')

def modifier_quantite(request, cart_item_id):
    """
    Met à jour la quantité d'un article dans le panier.
    """
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, id=cart_item_id)
        quantite = int(request.POST.get('quantite', 1))
        if quantite >= 1:
            cart_item.quantite = quantite
            cart_item.save()
            messages.success(request, f"Quantité mise à jour pour {cart_item.produit.nom}.")
        else:
            messages.error(request, "La quantité doit être au moins 1.")
    return redirect('panier')

def supprimer_du_panier(request, cart_item_id):
    """
    Supprime un article du panier.
    """
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    nom_produit = cart_item.produit.nom
    cart_item.delete()
    messages.success(request, f"{nom_produit} a été supprimé de votre panier.")
    return redirect('panier')


def commande(request):
    return render(request, 'main/commande.html')


def confirmation(request):
    return render(request, 'main/confirmation.html', {
        'message': 'Votre commande a été passée avec succès ! Vous recevrez une confirmation par email.'
    })




#def confirmation(request):
    #return render(request, 'main/confirmation.html')

#def commander(request):
    #return render(request, 'main/commander.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')

def caracteristiques(request):
    return render(request, 'main/caracteristiques.html')

def avis(request):
    return render(request, 'main/avis.html')