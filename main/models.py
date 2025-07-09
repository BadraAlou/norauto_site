import django.db.models.deletion
from django.db import migrations, models
from django.contrib.auth.models import User

class Produit(models.Model):
    CATEGORIE_CHOICES = [
        ('puce pour voiture', 'Puce Pour Voiture'),
        ('puce pour moto', 'Puce Pour Moto'),
        ('puce pour Personne', 'Puce Pour Personne'),
    ]

    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    categorie = models.CharField(max_length=100)
    en_stock = models.BooleanField(default=True)
    image = models.ImageField(upload_to='produits/', blank=True, null=True)
    cree_le = models.DateTimeField(auto_now_add=True)
    mis_a_jour_le = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

class Panier(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    session_id = models.CharField(max_length=100, blank=True, null=True)
    cree_le = models.DateTimeField(auto_now_add=True)
    mis_a_jour_le = models.DateTimeField(auto_now=True)

    def total(self):
        return sum(item.total() for item in self.cartitem_set.all())

    def nombre_articles(self):
        return self.cartitem_set.count()

    def __str__(self):
        return f"Panier #{self.pk}"

class CartItem(models.Model):
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)
    cree_le = models.DateTimeField(auto_now_add=True)

    def total(self):
        return self.produit.prix * self.quantite

    def __str__(self):
        return f"{self.quantite} x {self.produit.nom}"


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personnel_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('present', models.BooleanField()),
                ('motif', models.CharField(blank=True, max_length=255, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personnel_app.employee')),
            ],
            options={
                'verbose_name_plural': 'Présences',
                'unique_together': {('employee', 'date')},
            },
        ),
        ]
