# Generated by Django 2.1.7 on 2019-04-07 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobber', '0004_recomendation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recomendation',
            name='content',
            field=models.CharField(max_length=4000, null=True),
        ),
        migrations.AlterField(
            model_name='recomendation',
            name='title',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='recomendation',
            name='type',
            field=models.CharField(max_length=100),
        ),
    ]
