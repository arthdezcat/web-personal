# Generated by Django 4.2.7 on 2024-01-18 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stored', '0003_rename_localid_cliente_localidad_and_more'),
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalago',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stored.categ'),
        ),
    ]