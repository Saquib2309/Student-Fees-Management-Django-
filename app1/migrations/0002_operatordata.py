# Generated by Django 5.0 on 2024-01-02 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='operatordata',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]
