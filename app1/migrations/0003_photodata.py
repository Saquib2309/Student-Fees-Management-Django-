# Generated by Django 5.0 on 2024-01-03 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_operatordata'),
    ]

    operations = [
        migrations.CreateModel(
            name='photodata',
            fields=[
                ('email', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('photo', models.CharField(max_length=100)),
            ],
        ),
    ]