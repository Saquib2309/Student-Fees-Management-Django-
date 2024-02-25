# Generated by Django 5.0 on 2024-01-11 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_coursesdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_coursesdata',
            fields=[
                ('courses_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('courses_name', models.CharField(max_length=100)),
                ('fees', models.IntegerField()),
                ('duration', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('paid', models.IntegerField()),
                ('due', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='coursesdata',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
