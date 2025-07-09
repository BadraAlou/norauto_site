# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('a_propos/', views.a_propos, name='a_propos'),
    path('nos_produits/', views.nos_produits, name='nos_produits'),
    path('panier/', views.panier, name='panier'),
    path('ajouter_au_panier/<int:produit_id>/', views.ajouter_au_panier, name='ajouter_au_panier'),
    path('modifier_quantite/<int:cart_item_id>/', views.modifier_quantite, name='modifier_quantite'),
    path('supprimer_du_panier/<int:cart_item_id>/', views.supprimer_du_panier, name='supprimer_du_panier'),
    path('commande/', views.commande, name='commande'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('caracteristiques/', views.caracteristiques, name='caracteristiques'),
    path('avis/', views.avis, name='avis'),
]