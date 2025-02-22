# Generated by Django 5.1.6 on 2025-02-22 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.CharField(blank=True, choices=[('Furniture', 'Furniture'), ('IT Equipment', 'IT Equipment'), ('Phone', 'Phone'), ('Electronic', 'Electronic')], max_length=50, null=True),
        ),
    ]
