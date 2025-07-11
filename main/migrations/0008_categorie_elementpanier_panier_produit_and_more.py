# Generated by Django 5.1.7 on 2025-05-22 23:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_gpschip_slug_delete_cartitem'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Catégorie',
                'verbose_name_plural': 'Catégories',
            },
        ),
        migrations.CreateModel(
            name='ElementPanier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField(default=1)),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Panier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(blank=True, max_length=100, null=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_modification', models.DateTimeField(auto_now=True)),
                ('complete', models.BooleanField(default=False)),
                ('utilisateur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('prix', models.DecimalField(decimal_places=0, max_digits=10)),
                ('modele', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='produits/')),
                ('stock', models.IntegerField(default=0)),
                ('actif', models.BooleanField(default=True)),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produits', to='main.categorie')),
            ],
            options={
                'verbose_name': 'Produit',
                'verbose_name_plural': 'Produits',
                'ordering': ['-date_ajout'],
            },
        ),
        migrations.DeleteModel(
            name='GPSChip',
        ),
        migrations.AddField(
            model_name='elementpanier',
            name='panier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='elements', to='main.panier'),
        ),
        migrations.AddField(
            model_name='elementpanier',
            name='produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.produit'),
        ),
        migrations.AlterUniqueTogether(
            name='elementpanier',
            unique_together={('panier', 'produit')},
        ),
    ]
