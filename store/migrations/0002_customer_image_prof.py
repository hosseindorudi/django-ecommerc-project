# Generated by Django 3.2.7 on 2021-09-27 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='image_prof',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
