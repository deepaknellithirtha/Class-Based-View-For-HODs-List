# Generated by Django 2.2 on 2020-12-12 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hod',
            name='dept',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='hod',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]