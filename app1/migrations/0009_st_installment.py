# Generated by Django 5.0 on 2024-01-16 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_st_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='st_installment',
            fields=[
                ('t_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100)),
                ('course_id', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('t_date', models.DateField()),
                ('remark', models.CharField(max_length=100)),
            ],
        ),
    ]
