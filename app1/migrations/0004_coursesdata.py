# Generated by Django 5.0 on 2024-01-10 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_photodata'),
    ]

    operations = [
        migrations.CreateModel(
            name='coursesdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses_name', models.CharField(max_length=100)),
                ('fees', models.IntegerField()),
                ('duration', models.CharField(max_length=100)),
            ],
        ),
    ]
