# main/admin.py
from django.contrib import admin
from .models import Produit, Panier, CartItem

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'categorie', 'en_stock', 'cree_le', 'mis_a_jour_le')
    list_filter = ('categorie', 'en_stock', 'cree_le')
    search_fields = ('nom', 'description')
    list_editable = ('prix', 'categorie', 'en_stock')
    prepopulated_fields = {'description': ('nom',)}

@admin.register(Panier)
class PanierAdmin(admin.ModelAdmin):
    list_display = ('id', 'utilisateur', 'session_id', 'total', 'nombre_articles', 'cree_le')
    list_filter = ('utilisateur', 'cree_le')
    search_fields = ('utilisateur__username', 'session_id')
    readonly_fields = ('cree_le', 'mis_a_jour_le')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('panier', 'produit', 'quantite', 'total', 'cree_le')
    list_filter = ('panier', 'produit')
    search_fields = ('produit__nom',)